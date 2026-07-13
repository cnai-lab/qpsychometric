# #!/usr/bin/env python
# # coding: utf-8

# """
# General Questionnaire Validation Module (CLM version)

# Parallel of questionnaire_validator.py for Causal Language Model (CLM) questions.
# Provides validation capabilities for psychometric questionnaires including
# linguistic acceptability, internal consistency, Cronbach's alpha, and
# correlation analysis -- evaluated against causal LMs via QCLM.

# Usage:
#     from questionnaire_clm_validator import QuestionnaireCLMValidator

#     validator = QuestionnaireCLMValidator(
#         questionnaire_name="PHQ9",
#         questions=phq9_questions,
#         factors=["Q"],
#         index=["question"],
#         scales=["answer"],
#         result_path="results/",
#         clm_pipelines=["Qwen/Qwen3-1.7B", "gpt2"]
#     )

#     validator.run_validation()
# """

# import torch
# import pandas as pd
# from pathlib import Path
# import gc
# import json
# import os
# import time
# import numpy as np
# from tqdm.auto import tqdm
# import warnings
# import pingouin as pg
# from functools import partial
# from sentence_transformers import SentenceTransformer, util
# from transformers import pipeline
# from collections import defaultdict
# from qlatent.qclm.qclm import *
# from qlatent.qclm.qclm import QCLM


# class QuestionnaireCLMValidator:
#     """
#     Validation framework for psychometric questionnaires evaluated with
#     causal language models (QCLM).

#     Parameters
#     ----------
#     questionnaire_name : str
#         Short name/abbreviation (e.g., "PHQ9", "GAD7").
#     questions : list
#         List of QCLM-subclass question constructors.
#     factors : list
#         List of factor names in the questionnaire.
#     index : list, optional
#         Index dimensions (default: ["question"]).
#     scales : list, optional
#         Scale dimensions (default: ["answer"]).
#     result_path : str or Path, optional
#         Path to save results (default: "results/").
#     clm_pipelines : list, optional
#         List of causal LM model identifiers to validate against.
#     softmax_settings : list, optional
#         Softmax settings (default: [True, False]).
#     filters : dict, optional
#         Filter configurations.
#     device : int or str, optional
#         Device for computation (default: auto-detect GPU).
#     q_range : list, optional
#         Question score range (default: [5, 0]).
#     update : bool, optional
#         Whether to re-evaluate already-scored questions.
#     """

#     def __init__(
#         self,
#         questionnaire_name,
#         questions,
#         factors,
#         index=None,
#         scales=None,
#         result_path="results/",
#         clm_pipelines=None,
#         softmax_settings=None,
#         filters=None,
#         device=None,
#         q_range=None,
#         update=True,
#     ):
#         self.questionnaire_name = questionnaire_name
#         self.raw_questions = questions
#         self.factors = factors
#         self.index = index if index is not None else ["question"]
#         self.scales = scales if scales is not None else ["answer"]
#         self.result_path = Path(result_path)
#         self.update = update

#         # Default causal LM pipelines if not provided.
#         # Keep this short by default -- CLM eval is heavier than MNLI.
#         if clm_pipelines is None:
#             self.clm_pipelines = [
#                 "google/gemma-2-2b",
#                 "google/gemma-2-9b",
#                 # "google/gemma-3-1b-it",
#                 "google/gemma-3-270m",
#                 # "google/gemma-3-270m-it",
#                 "meta-llama/Llama-3.2-1B",
#                 # "meta-llama/Llama-3.2-1B-Instruct",
#                 "meta-llama/Llama-3.2-3B",
#                 # "meta-llama/Llama-3.2-3B-Instruct",
#                 "microsoft/MediPhi",
#                 # "microsoft/MediPhi-Instruct",
#                 "microsoft/MediPhi-PubMed",
#                 # "microsoft/Phi-4-mini-instruct",
#                 # "Qwen/Qwen3-1.7B",
#                 # "Qwen/Qwen3-4B",
#                 "Qwen/Qwen2.5-3B",

                
#                 # "meta-llama/Meta-Llama-3-8B",
#                 # "meta-llama/Llama-3.1-8B",
#                 # # "meta-llama/Llama-3.1-8B-Instruct",
#                 # # "meta-llama/Meta-Llama-3-8B-Instruct",
#             ]
#         else:
#             self.clm_pipelines = clm_pipelines

#         self.softmax_settings = softmax_settings if softmax_settings is not None else [True, False]

#         if filters is None:
#             self.filters = self._get_default_filters()
#         else:
#             self.filters = filters

#         if device is None:
#             self.device = 0 if torch.cuda.is_available() else -1
#         else:
#             self.device = device

#         self.q_range = q_range if q_range is not None else [5, 0]

#         self._init_models()

#         if not self.result_path.exists():
#             os.makedirs(self.result_path)

#         self.split_questions = self._split_all_questions()

#         print(f"Initialized {questionnaire_name} CLM Validator:")
#         print(f"  - Questions: {len(self.raw_questions)}")
#         print(f"  - Factors: {self.factors}")
#         print(f"  - Scales: {self.scales}")
#         print(f"  - Index: {self.index}")
#         print(f"  - Device: {self.device}")
#         print(f"  - Result path: {self.result_path}")

#     def _get_default_filters(self):
#         return {
#             'unfiltered': {},
#             'positiveonly': lambda q: q.get_filter_for_postive_keywords(self.scales),
#         }

#     def _init_models(self):
#         """Initialize sentence embedding and COLA models (for linguistic metrics)."""
#         print("Loading validation models...")
#         self.sentence_embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
#         self.cola = pipeline(
#             "text-classification",
#             "mrm8488/deberta-v3-small-finetuned-cola",
#             device=self.device,
#         )
#         print("Models loaded successfully.")

#     def _split_question(self, Q, verbose=False):
#         """Split a question into multiple variants with different softmax strategies and filters."""
#         result = []
#         for s in self.scales:
#             q = QCACHE(Q())
#             for sf in self.softmax_settings:
#                 for filter_name, filter_func in self.filters.items():
#                     filter_val = filter_func(Q()) if callable(filter_func) else filter_func

#                     if sf:
#                         qsf = QSOFTMAX(q, dim=[self.index[0], s])
#                         qsf_f = QFILTER(qsf, filter_val, filtername=filter_name)
#                         if verbose:
#                             print((self.index, s), sf, filter_name)
#                         result.append(qsf_f)

#                         qsf = QSOFTMAX(q, dim=s)
#                         qsf_f = QFILTER(qsf, filter_val, filtername=filter_name)
#                         if verbose:
#                             print(s, sf, filter_name)
#                         result.append(qsf_f)

#                         qsf = QSOFTMAX(q, dim=self.index[0])
#                         qsf_f = QFILTER(qsf, filter_val, filtername=filter_name)
#                         if verbose:
#                             print(self.index[0], sf, filter_name)
#                         result.append(qsf_f)
#                     else:
#                         qsf = QPASS(q, descupdate={'softmax': ''})
#                         qsf_f = QFILTER(qsf, filter_val, filtername=filter_name)
#                         if verbose:
#                             print(s, sf, filter_name)
#                         result.append(qsf_f)
#         return result

#     def _split_all_questions(self, verbose=False):
#         print(f"Splitting {len(self.raw_questions)} questions...")
#         all_split = []
#         for Q in self.raw_questions:
#             all_split.append(self._split_question(Q, verbose=verbose))
#         print(f"Generated {sum(len(qs) for qs in all_split)} question variants.")
#         return all_split

#     # ---- Per-question rendering -----------------------------------------

#     @staticmethod
#     def _render(q, kmap):
#         """Render a QCLM question's template with a keyword map."""
#         return q._template.format_map(kmap)

#     @staticmethod
#     def _clean_original(description):
#         """Strip the factor/ordinal prefix off the 'Original' descriptor field."""
#         strFactor = description['Factor']
#         strOrdinal = str(description.get('Ordinal', 0))
#         s = description['Original']
#         s = 'none' if s is None else s
#         s = s.replace(strFactor, '', 1)
#         s = s.replace(strOrdinal, '', 1)
#         s = s.replace('.', '', 1)
#         return s.strip()

#     # ---- Linguistic acceptability ---------------------------------------

#     def _linguistic_acceptabilities(self, q, index, scale, question_name,
#                                     student_id, output_path=None, save_to_file=False):
#         if output_path is None:
#             output_path = self.result_path
#         else:
#             output_path = Path(output_path)

#         description = q._descriptor
#         strOriginal = self._clean_original(description)

#         rows = []

#         partial_internal_consistency = partial(
#             q.internal_consistency,
#             filter={},
#             index=index,
#             scale=scale,
#         )
#         try:
#             silhouette_score = partial_internal_consistency(
#                 measure='silhouette_score',
#                 metric='correlation',
#             )
#         except Exception as e:
#             print(e)
#             print('silhouette_score is set to -1')
#             silhouette_score = -1

#         if hasattr(q, 'linguistic_acceptability'):
#             q.linguistic_acceptability['silhouette_score'] = silhouette_score
#             return q.linguistic_acceptability

#         for kmap in q._keywords_map:
#             score = {}
#             score['question_name'] = question_name
#             strPermutation = self._render(q, kmap)
#             score['original_question'] = strOriginal

#             cola_result = self.cola(strPermutation)[0]
#             score['cola_score'] = cola_result.get('score')
#             score['param'] = kmap
#             score['question_permutation'] = strPermutation

#             embeddings1 = self.sentence_embedding_model.encode(strOriginal, convert_to_tensor=True)
#             embeddings2 = self.sentence_embedding_model.encode(strPermutation, convert_to_tensor=True)
#             cosine_scores = util.cos_sim(embeddings1, embeddings2)
#             score['semantic_similarity'] = cosine_scores.item()

#             score['silhouette_score'] = silhouette_score
#             rows.append(score)

#         filename = output_path / 'linguistic_acceptabilities.csv'
#         df = pd.DataFrame(rows)
#         df['student_id'] = student_id
#         df = df[[
#             'student_id', 'question_name', 'original_question', 'param',
#             'question_permutation', 'cola_score', 'semantic_similarity', 'silhouette_score',
#         ]]

#         if save_to_file:
#             if filename.exists():
#                 df.to_csv(filename, index=False, header=None, mode='a', encoding='utf-8-sig')
#             else:
#                 df.to_csv(filename, index=False, encoding='utf-8-sig')

#         q.linguistic_acceptability = df
#         return df

#     def _question_attributes(self, q):
#         """Extract attributes from a QCLM question (single template, not context+answer)."""
#         score = {}
#         score['questionnair'] = q._descriptor['Questionnair']
#         score['factor'] = q._descriptor['Factor']
#         score['ordinal'] = q._descriptor['Ordinal']
#         score['scale'] = q._descriptor['scale']
#         score['index'] = q._descriptor['index']
#         score['filter'] = q._descriptor['filter']
#         score['softmax'] = q._descriptor['softmax']
#         score['original'] = q._descriptor['Original']
#         score['Q'] = f"{score['questionnair']}{score['factor']}{score['ordinal']}"
#         score['template'] = q._template
#         score['dimensions'] = q._dimensions
#         score['model'] = q.model.model_identifier if q.model else ""
#         return score

#     def _get_question_features(self, q, student_id='student_id', output_path=None, save_to_file=False):
#         if output_path is None:
#             output_path = self.result_path

#         score = self._question_attributes(q)
#         score['mean_score'] = q.mean_score().detach().cpu().item()
#         index = q._index
#         scale = q._scale
#         linguistic_df = self._linguistic_acceptabilities(
#             q, index=index, scale=scale, question_name=score['Q'],
#             student_id=student_id, output_path=output_path, save_to_file=save_to_file,
#         )
#         row = linguistic_df[['cola_score', 'silhouette_score']].mean(axis=0)
#         row_dict = dict(row)
#         row_dict['semantic_similarity'] = linguistic_df['semantic_similarity'].quantile(0.75)
#         score = score | row_dict
#         return score

#     # ---- Path helpers (unchanged) ---------------------------------------

#     @staticmethod
#     def _extract_epoch(model_path):
#         if 'epoch-' in model_path.name:
#             i = model_path.name.find('epoch-')
#             j = model_path.name.find('_', i)
#             if j > 0:
#                 epoch = int(model_path.name[i + len('epoch-'):j])
#             else:
#                 epoch = int(model_path.name[i + len('epoch-'):])
#         elif 'checkpoint-' in model_path.name:
#             i = model_path.name.find('checkpoint-')
#             j = model_path.name.find('_', i)
#             if j > 0:
#                 epoch = int(model_path.name[i + len('checkpoint-'):j])
#             else:
#                 epoch = int(model_path.name[i + len('checkpoint-'):])
#         else:
#             epoch = 0
#         return epoch

#     @staticmethod
#     def _extract_run(model_path):
#         try:
#             if 'run' in model_path.name:
#                 for part in model_path.name.split('_'):
#                     if 'run' in part:
#                         return int(part.replace('run', ''))
#             else:
#                 return -1
#         except Exception as e:
#             print(e)
#             return -1

#     @staticmethod
#     def _get_clm_score(checkpoint_path):
#         """Read an eval score from checkpoint metadata if available."""
#         score_path = checkpoint_path / 'all_results.json'
#         if not score_path.exists():
#             score_path = checkpoint_path.parent / (checkpoint_path.name + '_clm_eval') / 'all_results.json'
#         if score_path.exists():
#             with open(score_path) as f:
#                 data = json.load(f)
#                 # Try a few likely keys; fall back to -1.
#                 for key in ('eval_accuracy', 'eval_loss', 'perplexity'):
#                     if key in data:
#                         return data[key]
#                 return -1
#         return -1

#     # ---- Run loop -------------------------------------------------------

#     def _run_questions(self, questions, clm_checkpoint, train_process, finetune_dataset):
#         rows = []
#         checkpoint = Path(clm_checkpoint.model_identifier)
#         for q_raw in tqdm(questions, desc="Processing questions"):
#             # training=False; scoring uses QCLM's default (geometric_mean)
#             q = q_raw.run(clm_checkpoint, mode="raw")
#             score = self._get_question_features(q)
#             score['epoch'] = self._extract_epoch(checkpoint)
#             score['train_process'] = train_process
#             score['dataset'] = finetune_dataset
#             score['run'] = self._extract_run(checkpoint.parent)
#             score['clm_score'] = self._get_clm_score(checkpoint)
#             score['range'] = (q._weights_flat.min(), q._weights_flat.max())
#             score['score'] = np.interp(
#                 score['mean_score'],
#                 [q._weights_flat.min(), q._weights_flat.max()],
#                 self.q_range,
#             )
#             rows.append(score)
#             gc.collect()
#             if torch.cuda.is_available():
#                 torch.cuda.empty_cache()
#         return rows

#     def _calc_scores(self, questions, checkpoint, train_process, finetune_dataset):
#         clm_checkpoint = pipeline("text-generation", str(checkpoint), device=self.device)
#         clm_checkpoint.model_identifier = str(checkpoint)
#         return self._run_questions(questions, clm_checkpoint, train_process, finetune_dataset)

#     @staticmethod
#     def _add_epochs_to_rows(rows, mlm_epoch, clm_checkpoint):
#         for score in rows:
#             score['mlm_epoch'] = mlm_epoch
#             score['clm_checkpoint'] = clm_checkpoint
#         return rows

#     @staticmethod
#     def _write_to_csv(rows, output_path):
#         df = pd.DataFrame(rows)
#         if output_path.exists():
#             df.to_csv(output_path, index=False, header=None, mode='a')
#         else:
#             df.to_csv(output_path, index=False)

#     def run_model_evaluation(self, output_filename=None):
#         """
#         Run the questionnaire evaluation on all configured CLM pipelines.

#         Parameters
#         ----------
#         output_filename : str, optional
#             Name of the output CSV (default: "{questionnaire_name}_clm_results.csv").

#         Returns
#         -------
#         Path
#             Path to the output CSV file.
#         """
#         if output_filename is None:
#             output_filename = f'{self.questionnaire_name.lower()}_clm_results.csv'

#         output_path = self.result_path / output_filename

#         questions = []
#         for qs in self.split_questions:
#             questions.extend(qs)

#         print(f"\nRunning model evaluation with {len(questions)} question variants...")

#         if output_path.exists():
#             temp_df = pd.read_csv(output_path)
#             indexes = temp_df.groupby(['model', 'Q']).count().index.values
#             used_models = defaultdict(set)
#             for k, v in indexes:
#                 used_models[k].add(v)
#         else:
#             used_models = {}

#         for p in tqdm(self.clm_pipelines, desc="Evaluating models"):
#             print(f"\nEvaluating model: {p}")
#             with warnings.catch_warnings():
#                 try:
#                     warnings.simplefilter("ignore")

#                     if p in used_models and not self.update:
#                         pipeline_questions = []
#                         for q in questions:
#                             if self._question_attributes(q)['Q'] not in used_models[p]:
#                                 pipeline_questions.append(q)
#                             else:
#                                 print('skip', p, self._question_attributes(q)['Q'])
#                     else:
#                         pipeline_questions = questions

#                     if len(pipeline_questions) == 0:
#                         print(f"All questions already evaluated for {p}, skipping...")
#                         continue

#                     rows = self._calc_scores(
#                         pipeline_questions,
#                         Path(p),
#                         'base',
#                         'evaluation',
#                     )
#                     rows = self._add_epochs_to_rows(rows, 0, 0)
#                     self._write_to_csv(rows, output_path)

#                     gc.collect()
#                     if torch.cuda.is_available():
#                         torch.cuda.empty_cache()
#                 except Exception as e:
#                     print(f"Error evaluating {p}: {e}")

#         df = pd.read_csv(output_path)
#         df = df.drop_duplicates(subset=['filter', 'softmax', 'model', 'Q'], keep='last')
#         df.to_csv(output_path, index=False)

#         print(f"\n✓ Model evaluation complete. Results saved to: {output_path}")
#         return output_path

#     # ---- Analysis methods (unchanged) -----------------------------------

#     def load_results(self, csv_path, softmax, positiveonly, value='score', index='model', columns='Q'):
#         df = pd.read_csv(csv_path)

#         if df['softmax'].isna().sum() > 0:
#             softmax_filter = df['softmax'].isna()
#         else:
#             softmax_filter = df['softmax'] == ''

#         if softmax:
#             df = df[df['softmax'] == str(softmax)]
#         else:
#             df = df[softmax_filter]

#         if value == 'silhouette_score':
#             df = df[df['silhouette_score'] > -1]

#         if positiveonly:
#             df = df[df['filter'] == "positiveonly"]
#         else:
#             df = df[df['filter'] == "unfiltered"]

#         return pd.pivot_table(df, values=value, index=index, columns=columns, aggfunc='mean')

#     def calc_content_validity(self, results_csv, softmax=None, output_filename=None):
#         if softmax is None:
#             softmax = self.index + self.scales
#         if output_filename is None:
#             output_filename = "linguistic_acceptability.csv"

#         cols = ['semantic_similarity', 'cola_score', 'silhouette_score']

#         results = []
#         for softmax_filter in [softmax]:
#             q_res = [
#                 self.load_results(results_csv, softmax=softmax_filter, positiveonly=False, value=v).mean(axis=0)
#                 for v in cols
#             ]
#             results.append(pd.concat(q_res, axis=1))

#         linguistic_acceptability_df = pd.concat(results, axis=0)
#         linguistic_acceptability_df.columns = ['semantic_similarity', 'cola_score', 'silhouette_score']

#         output_path = self.result_path / output_filename
#         linguistic_acceptability_df.to_csv(output_path, index=True)

#         print(f"\n✓ Content validity metrics saved to: {output_path}")
#         return linguistic_acceptability_df.sort_values('silhouette_score')

#     def calc_cronbach_alpha(self, results_csv, softmax=None, positiveonly=True):
#         if softmax is None:
#             softmax = self.index + self.scales

#         value = 'mean_score'
#         results = []
#         for softmax_filter in [softmax]:
#             results.append(
#                 self.load_results(results_csv, softmax=softmax_filter, positiveonly=positiveonly, value=value)
#             )

#         data_df = pd.concat(results, axis=1)

#         print('\nCronbach Alpha:')
#         factor_alphas = {}
#         for subset in self.factors:
#             feature_subset = [c for c in data_df.columns if subset in c]
#             if len(feature_subset) > 1:
#                 alpha = pg.cronbach_alpha(data=data_df[feature_subset])
#                 print(f'{subset}: {alpha}')
#                 factor_alphas[subset] = alpha
#             else:
#                 print(f'{subset}: Insufficient items (n={len(feature_subset)})')

#         all_feature_subset = self._get_factor_sub_features(self.factors, data_df)
#         if len(all_feature_subset) > 1:
#             alpha = pg.cronbach_alpha(data=data_df[all_feature_subset])
#             print(f'\n{self.questionnaire_name} Overall: {alpha}')
#             overall_alpha = alpha
#         else:
#             print(f'\n{self.questionnaire_name} Overall: Insufficient items')
#             overall_alpha = None

#         return {
#             'data_df': data_df,
#             'overall': overall_alpha,
#             'factors': factor_alphas,
#         }

#     def test_question_affect_on_cronbach_alpha(self, data_df, specific_factors=None):
#         if specific_factors is None:
#             subset_df = data_df
#             alpha = pg.cronbach_alpha(data=subset_df)
#             print('All Questions Alpha:', alpha)
#             for feature in subset_df.columns:
#                 sub = [c for c in subset_df.columns if c != feature]
#                 alpha = pg.cronbach_alpha(data=subset_df[sub])
#                 print('without:', feature, 'Alpha:', alpha)
#         else:
#             if specific_factors == "all":
#                 specific_factors = self.factors
#             for subset in specific_factors:
#                 feature_subset = [c for c in data_df.columns if subset in c]
#                 subset_df = data_df[feature_subset]
#                 alpha = pg.cronbach_alpha(data=subset_df)
#                 print(subset, 'Alpha:', alpha)
#                 for feature in subset_df.columns:
#                     sub = [c for c in subset_df.columns if c != feature]
#                     alpha = pg.cronbach_alpha(data=subset_df[sub])
#                     print('without:', feature, 'Alpha:', alpha)

#     def get_semantic_similarity(self, q=None):
#         """Calculate semantic similarity for a question or all raw questions."""
#         if q is None:
#             results = {}
#             for Q in tqdm(self.raw_questions, desc="Calculating semantic similarity"):
#                 q_instance = Q()
#                 description = q_instance._descriptor
#                 strOriginal = self._clean_original(description)

#                 scores = []
#                 for kmap in q_instance._keywords_map:
#                     strPermutation = self._render(q_instance, kmap)
#                     embeddings1 = self.sentence_embedding_model.encode(strOriginal, convert_to_tensor=True)
#                     embeddings2 = self.sentence_embedding_model.encode(strPermutation, convert_to_tensor=True)
#                     cosine_scores = util.cos_sim(embeddings1, embeddings2)
#                     scores.append(cosine_scores.item())

#                 question_name = f"{description['Questionnair']}{description['Factor']}{description['Ordinal']}"
#                 results[question_name] = np.percentile(scores, 75)

#             return pd.DataFrame.from_dict(results, orient='index', columns=['semantic_similarity'])

#         description = q._descriptor
#         strOriginal = self._clean_original(description)

#         scores = []
#         for kmap in q._keywords_map:
#             strPermutation = self._render(q, kmap)
#             embeddings1 = self.sentence_embedding_model.encode(strOriginal, convert_to_tensor=True)
#             embeddings2 = self.sentence_embedding_model.encode(strPermutation, convert_to_tensor=True)
#             cosine_scores = util.cos_sim(embeddings1, embeddings2)
#             scores.append(cosine_scores.item())

#         return np.percentile(scores, 75)

#     def get_cola_score(self, q=None):
#         """Calculate COLA (linguistic acceptability) for a question or all raw questions."""
#         if q is None:
#             results = {}
#             for Q in tqdm(self.raw_questions, desc="Calculating COLA scores"):
#                 q_instance = Q()
#                 description = q_instance._descriptor

#                 scores = []
#                 for kmap in q_instance._keywords_map:
#                     strPermutation = self._render(q_instance, kmap)
#                     cola_result = self.cola(strPermutation)[0]
#                     scores.append(cola_result.get('score'))

#                 question_name = f"{description['Questionnair']}{description['Factor']}{description['Ordinal']}"
#                 results[question_name] = np.mean(scores)

#             return pd.DataFrame.from_dict(results, orient='index', columns=['cola_score'])

#         scores = []
#         for kmap in q._keywords_map:
#             strPermutation = self._render(q, kmap)
#             cola_result = self.cola(strPermutation)[0]
#             scores.append(cola_result.get('score'))

#         return np.mean(scores)

#     def calc_correlations(self, results_csv, softmax=None, positiveonly=True, method='spearman'):
#         if softmax is None:
#             softmax = self.index + self.scales

#         value = 'mean_score'

#         results = []
#         for softmax_filter in [softmax]:
#             results.append(
#                 self.load_results(results_csv, softmax=softmax_filter, positiveonly=positiveonly, value=value)
#             )

#         data_df = pd.concat(results, axis=1)
#         filtered_df = pd.DataFrame()

#         for factor in self.factors:
#             feature_subset = self._get_factor_sub_features([factor], data_df)
#             if len(feature_subset) > 0:
#                 filtered_df[factor] = data_df[feature_subset].mean(axis=1)

#         all_feature_subset = self._get_factor_sub_features(self.factors, data_df)
#         filtered_df[self.questionnaire_name] = data_df[all_feature_subset].mean(axis=1)

#         corr_df = filtered_df.rcorr(method=method)
#         print(f"\n✓ Factor correlations ({method}):")
#         print(corr_df)

#         return corr_df

#     @staticmethod
#     def _get_factor_sub_features(factor_list, data_df):
#         feature_subset = []
#         for subset in factor_list:
#             feature_subset += [c for c in data_df.columns if subset in c]
#         return list(set(feature_subset))

#     def run_validation(self, output_filename=None):
#         """Run the full validation pipeline."""
#         print(f"\n{'='*70}")
#         print(f"Running Complete CLM Validation for {self.questionnaire_name} Questionnaire")
#         print(f"{'='*70}")

#         results_csv = self.run_model_evaluation(output_filename)

#         print(f"\n{'='*70}")
#         print("Calculating Content Validity Metrics")
#         print(f"{'='*70}")
#         content_validity = self.calc_content_validity(results_csv)
#         print("\nContent Validity Results:")
#         print(content_validity)

#         print(f"\n{'='*70}")
#         print("Calculating Internal Consistency (Cronbach's Alpha)")
#         print(f"{'='*70}")
#         alpha_results = self.calc_cronbach_alpha(results_csv)

#         print(f"\n{'='*70}")
#         print("Calculating Factor Correlations")
#         print(f"{'='*70}")
#         correlations = self.calc_correlations(results_csv)

#         print(f"\n{'='*70}")
#         print("Validation Complete!")
#         print(f"{'='*70}")
#         print(f"Results saved in: {self.result_path}")

#         return {
#             'results_csv': results_csv,
#             'content_validity': content_validity,
#             'cronbach_alpha': alpha_results,
#             'correlations': correlations,
#         }


#!/usr/bin/env python
# coding: utf-8

"""
General Questionnaire Validation Module (CLM version)

Parallel of questionnaire_validator.py for Causal Language Model (CLM) questions.
Provides validation capabilities for psychometric questionnaires including
linguistic acceptability, internal consistency, Cronbach's alpha, and
correlation analysis -- evaluated against causal LMs via QCLM.

Base (pretrained) models are scored with mode="raw"; instruction-tuned / chat
models are scored with mode="chat" (the item is wrapped with the tokenizer's
chat template). Each result row is tagged with model_type ("base" or "chat"),
so downstream analysis can be run separately per population.

Usage:
    from questionnaire_clm_validator import QuestionnaireCLMValidator

    validator = QuestionnaireCLMValidator(
        questionnaire_name="PHQ9",
        questions=phq9_questions,
        factors=["Q"],
        clm_pipelines=["google/gemma-2-2b", "google/gemma-3-1b-it"],
        instruct_models=["google/gemma-3-1b-it"],
        result_path="results/",
    )

    validator.run_validation()

    # Per-type analysis (call manually):
    validator.calc_content_validity(csv, model_type="base")
    validator.calc_content_validity(csv, model_type="chat")
"""

import torch
import pandas as pd
from pathlib import Path
import gc
import json
import os
import time
import numpy as np
from tqdm.auto import tqdm
import warnings
import pingouin as pg
from functools import partial
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
from collections import defaultdict
from qlatent.qclm.qclm import *
from qlatent.qclm.qclm import QCLM


class QuestionnaireCLMValidator:
    """
    Validation framework for psychometric questionnaires evaluated with
    causal language models (QCLM).

    Parameters
    ----------
    questionnaire_name : str
        Short name/abbreviation (e.g., "PHQ9", "GAD7").
    questions : list
        List of QCLM-subclass question constructors.
    factors : list
        List of factor names in the questionnaire.
    index : list, optional
        Index dimensions (default: ["question"]).
    scales : list, optional
        Scale dimensions (default: ["answer"]).
    result_path : str or Path, optional
        Path to save results (default: "results/").
    clm_pipelines : list, optional
        List of causal LM model identifiers to validate against.
    instruct_models : list, optional
        Explicit list of model identifiers (a subset of clm_pipelines) that are
        instruction-tuned / chat models. These are scored with mode="chat";
        all others are scored with mode="raw". Rows are tagged accordingly.
    softmax_settings : list, optional
        Softmax settings (default: [True, False]).
    filters : dict, optional
        Filter configurations.
    device : int or str, optional
        Device for computation (default: auto-detect GPU).
    q_range : list, optional
        Question score range (default: [5, 0]).
    update : bool, optional
        Whether to re-evaluate already-scored questions.
    """

    def __init__(
        self,
        questionnaire_name,
        questions,
        factors,
        index=None,
        scales=None,
        result_path="results/",
        clm_pipelines=None,
        instruct_models=None,
        softmax_settings=None,
        filters=None,
        device=None,
        q_range=None,
        update=True,
    ):
        self.questionnaire_name = questionnaire_name
        self.raw_questions = questions
        self.factors = factors
        self.index = index if index is not None else ["question"]
        self.scales = scales if scales is not None else ["answer"]
        self.result_path = Path(result_path)
        self.update = update

        # Default causal LM pipelines if not provided.
        # Base models are listed first; instruction-tuned models follow.
        if clm_pipelines is None:
            self.clm_pipelines = [
                # ---- base (pretrained) models ----
                "google/gemma-2-2b",
                "google/gemma-2-9b",
                "google/gemma-3-270m",
                "meta-llama/Llama-3.2-1B",
                "meta-llama/Llama-3.2-3B",
                "microsoft/MediPhi",
                "microsoft/MediPhi-PubMed",
                "Qwen/Qwen2.5-3B",
                # "meta-llama/Meta-Llama-3-8B",
                # "meta-llama/Llama-3.1-8B",
                # ---- instruction-tuned / chat models ----
                "google/gemma-3-1b-it",
                "google/gemma-3-270m-it",
                "meta-llama/Llama-3.2-1B-Instruct",
                "meta-llama/Llama-3.2-3B-Instruct",
                "microsoft/MediPhi-Instruct",
                "microsoft/Phi-4-mini-instruct",
                "Qwen/Qwen3-1.7B",
                "Qwen/Qwen3-4B",
                # "meta-llama/Llama-3.1-8B-Instruct",
                # "meta-llama/Meta-Llama-3-8B-Instruct",
            ]
        else:
            self.clm_pipelines = clm_pipelines

        # Explicit set of instruction-tuned / chat model identifiers.
        # When not provided, defaults to the instruct entries in the default
        # clm_pipelines list above, so base/chat modes are assigned correctly
        # without needing to specify the lists in the notebook.
        if instruct_models is not None:
            self.instruct_models = set(instruct_models)
        else:
            self.instruct_models = {
                "google/gemma-3-1b-it",
                "google/gemma-3-270m-it",
                "meta-llama/Llama-3.2-1B-Instruct",
                "meta-llama/Llama-3.2-3B-Instruct",
                "microsoft/MediPhi-Instruct",
                "microsoft/Phi-4-mini-instruct",
                "Qwen/Qwen3-1.7B",
                "Qwen/Qwen3-4B",
                # "meta-llama/Llama-3.1-8B-Instruct",
                # "meta-llama/Meta-Llama-3-8B-Instruct",
            }

        self.softmax_settings = softmax_settings if softmax_settings is not None else [True, False]

        if filters is None:
            self.filters = self._get_default_filters()
        else:
            self.filters = filters

        if device is None:
            self.device = 0 if torch.cuda.is_available() else -1
        else:
            self.device = device

        self.q_range = q_range if q_range is not None else [5, 0]

        self._init_models()

        if not self.result_path.exists():
            os.makedirs(self.result_path)

        self.split_questions = self._split_all_questions()

        print(f"Initialized {questionnaire_name} CLM Validator:")
        print(f"  - Questions: {len(self.raw_questions)}")
        print(f"  - Factors: {self.factors}")
        print(f"  - Scales: {self.scales}")
        print(f"  - Index: {self.index}")
        print(f"  - Device: {self.device}")
        print(f"  - Instruct (chat) models: {len(self.instruct_models)}")
        print(f"  - Result path: {self.result_path}")

    # ---- model-type helpers ---------------------------------------------

    def _model_mode(self, model_id):
        """Return the QCLM run mode for a model: 'chat' for instruct models, else 'raw'."""
        return "chat" if str(model_id) in self.instruct_models else "raw"

    def _model_type(self, model_id):
        """Return the population tag for a model: 'chat' for instruct models, else 'base'."""
        return "chat" if str(model_id) in self.instruct_models else "base"

    def _get_default_filters(self):
        return {
            'unfiltered': {},
            'positiveonly': lambda q: q.get_filter_for_postive_keywords(self.scales),
        }

    def _init_models(self):
        """Initialize sentence embedding and COLA models (for linguistic metrics)."""
        print("Loading validation models...")
        self.sentence_embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.cola = pipeline(
            "text-classification",
            "mrm8488/deberta-v3-small-finetuned-cola",
            device=self.device,
        )
        print("Models loaded successfully.")

    def _split_question(self, Q, verbose=False):
        """Split a question into multiple variants with different softmax strategies and filters."""
        result = []
        for s in self.scales:
            q = QCACHE(Q())
            for sf in self.softmax_settings:
                for filter_name, filter_func in self.filters.items():
                    filter_val = filter_func(Q()) if callable(filter_func) else filter_func

                    if sf:
                        qsf = QSOFTMAX(q, dim=[self.index[0], s])
                        qsf_f = QFILTER(qsf, filter_val, filtername=filter_name)
                        if verbose:
                            print((self.index, s), sf, filter_name)
                        result.append(qsf_f)

                        qsf = QSOFTMAX(q, dim=s)
                        qsf_f = QFILTER(qsf, filter_val, filtername=filter_name)
                        if verbose:
                            print(s, sf, filter_name)
                        result.append(qsf_f)

                        qsf = QSOFTMAX(q, dim=self.index[0])
                        qsf_f = QFILTER(qsf, filter_val, filtername=filter_name)
                        if verbose:
                            print(self.index[0], sf, filter_name)
                        result.append(qsf_f)
                    else:
                        qsf = QPASS(q, descupdate={'softmax': ''})
                        qsf_f = QFILTER(qsf, filter_val, filtername=filter_name)
                        if verbose:
                            print(s, sf, filter_name)
                        result.append(qsf_f)
        return result

    def _split_all_questions(self, verbose=False):
        print(f"Splitting {len(self.raw_questions)} questions...")
        all_split = []
        for Q in self.raw_questions:
            all_split.append(self._split_question(Q, verbose=verbose))
        print(f"Generated {sum(len(qs) for qs in all_split)} question variants.")
        return all_split

    # ---- Per-question rendering -----------------------------------------

    @staticmethod
    def _render(q, kmap):
        """Render a QCLM question's template with a keyword map."""
        return q._template.format_map(kmap)

    @staticmethod
    def _clean_original(description):
        """Strip the factor/ordinal prefix off the 'Original' descriptor field."""
        strFactor = description['Factor']
        strOrdinal = str(description.get('Ordinal', 0))
        s = description['Original']
        s = 'none' if s is None else s
        s = s.replace(strFactor, '', 1)
        s = s.replace(strOrdinal, '', 1)
        s = s.replace('.', '', 1)
        return s.strip()

    # ---- Linguistic acceptability ---------------------------------------

    def _linguistic_acceptabilities(self, q, index, scale, question_name,
                                    student_id, output_path=None, save_to_file=False):
        if output_path is None:
            output_path = self.result_path
        else:
            output_path = Path(output_path)

        description = q._descriptor
        strOriginal = self._clean_original(description)

        rows = []

        partial_internal_consistency = partial(
            q.internal_consistency,
            filter={},
            index=index,
            scale=scale,
        )
        try:
            silhouette_score = partial_internal_consistency(
                measure='silhouette_score',
                metric='correlation',
            )
        except Exception as e:
            print(e)
            print('silhouette_score is set to -1')
            silhouette_score = -1

        if hasattr(q, 'linguistic_acceptability'):
            q.linguistic_acceptability['silhouette_score'] = silhouette_score
            return q.linguistic_acceptability

        for kmap in q._keywords_map:
            score = {}
            score['question_name'] = question_name
            strPermutation = self._render(q, kmap)
            score['original_question'] = strOriginal

            cola_result = self.cola(strPermutation)[0]
            score['cola_score'] = cola_result.get('score')
            score['param'] = kmap
            score['question_permutation'] = strPermutation

            embeddings1 = self.sentence_embedding_model.encode(strOriginal, convert_to_tensor=True)
            embeddings2 = self.sentence_embedding_model.encode(strPermutation, convert_to_tensor=True)
            cosine_scores = util.cos_sim(embeddings1, embeddings2)
            score['semantic_similarity'] = cosine_scores.item()

            score['silhouette_score'] = silhouette_score
            rows.append(score)

        filename = output_path / 'linguistic_acceptabilities.csv'
        df = pd.DataFrame(rows)
        df['student_id'] = student_id
        df = df[[
            'student_id', 'question_name', 'original_question', 'param',
            'question_permutation', 'cola_score', 'semantic_similarity', 'silhouette_score',
        ]]

        if save_to_file:
            if filename.exists():
                df.to_csv(filename, index=False, header=None, mode='a', encoding='utf-8-sig')
            else:
                df.to_csv(filename, index=False, encoding='utf-8-sig')

        q.linguistic_acceptability = df
        return df

    def _question_attributes(self, q):
        """Extract attributes from a QCLM question (single template, not context+answer)."""
        score = {}
        score['questionnair'] = q._descriptor['Questionnair']
        score['factor'] = q._descriptor['Factor']
        score['ordinal'] = q._descriptor['Ordinal']
        score['scale'] = q._descriptor['scale']
        score['index'] = q._descriptor['index']
        score['filter'] = q._descriptor['filter']
        score['softmax'] = q._descriptor['softmax']
        score['original'] = q._descriptor['Original']
        score['Q'] = f"{score['questionnair']}{score['factor']}{score['ordinal']}"
        score['template'] = q._template
        score['dimensions'] = q._dimensions
        score['model'] = q.model.model_identifier if q.model else ""
        return score

    def _get_question_features(self, q, student_id='student_id', output_path=None, save_to_file=False):
        if output_path is None:
            output_path = self.result_path

        score = self._question_attributes(q)
        score['mean_score'] = q.mean_score().detach().cpu().item()
        index = q._index
        scale = q._scale
        linguistic_df = self._linguistic_acceptabilities(
            q, index=index, scale=scale, question_name=score['Q'],
            student_id=student_id, output_path=output_path, save_to_file=save_to_file,
        )
        row = linguistic_df[['cola_score', 'silhouette_score']].mean(axis=0)
        row_dict = dict(row)
        row_dict['semantic_similarity'] = linguistic_df['semantic_similarity'].quantile(0.75)
        score = score | row_dict
        return score

    # ---- Path helpers (unchanged) ---------------------------------------

    @staticmethod
    def _extract_epoch(model_path):
        if 'epoch-' in model_path.name:
            i = model_path.name.find('epoch-')
            j = model_path.name.find('_', i)
            if j > 0:
                epoch = int(model_path.name[i + len('epoch-'):j])
            else:
                epoch = int(model_path.name[i + len('epoch-'):])
        elif 'checkpoint-' in model_path.name:
            i = model_path.name.find('checkpoint-')
            j = model_path.name.find('_', i)
            if j > 0:
                epoch = int(model_path.name[i + len('checkpoint-'):j])
            else:
                epoch = int(model_path.name[i + len('checkpoint-'):])
        else:
            epoch = 0
        return epoch

    @staticmethod
    def _extract_run(model_path):
        try:
            if 'run' in model_path.name:
                for part in model_path.name.split('_'):
                    if 'run' in part:
                        return int(part.replace('run', ''))
            else:
                return -1
        except Exception as e:
            print(e)
            return -1

    @staticmethod
    def _get_clm_score(checkpoint_path):
        """Read an eval score from checkpoint metadata if available."""
        score_path = checkpoint_path / 'all_results.json'
        if not score_path.exists():
            score_path = checkpoint_path.parent / (checkpoint_path.name + '_clm_eval') / 'all_results.json'
        if score_path.exists():
            with open(score_path) as f:
                data = json.load(f)
                # Try a few likely keys; fall back to -1.
                for key in ('eval_accuracy', 'eval_loss', 'perplexity'):
                    if key in data:
                        return data[key]
                return -1
        return -1

    # ---- Run loop -------------------------------------------------------

    def _run_questions(self, questions, clm_checkpoint, train_process, finetune_dataset, mode, model_type):
        rows = []
        checkpoint = Path(clm_checkpoint.model_identifier)
        for q_raw in tqdm(questions, desc="Processing questions"):
            # mode is "raw" for base models, "chat" for instruction-tuned models
            q = q_raw.run(clm_checkpoint, mode=mode)
            score = self._get_question_features(q)
            score['epoch'] = self._extract_epoch(checkpoint)
            score['train_process'] = train_process
            score['dataset'] = finetune_dataset
            score['run'] = self._extract_run(checkpoint.parent)
            score['clm_score'] = self._get_clm_score(checkpoint)
            score['range'] = (q._weights_flat.min(), q._weights_flat.max())
            score['score'] = np.interp(
                score['mean_score'],
                [q._weights_flat.min(), q._weights_flat.max()],
                self.q_range,
            )
            score['mode'] = mode
            score['model_type'] = model_type
            rows.append(score)
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
        return rows

    def _calc_scores(self, questions, checkpoint, train_process, finetune_dataset, mode, model_type):
        clm_checkpoint = pipeline("text-generation", str(checkpoint), device=self.device)
        clm_checkpoint.model_identifier = str(checkpoint)
        try:
            return self._run_questions(
                questions, clm_checkpoint, train_process, finetune_dataset, mode, model_type
            )
        finally:
            # Aggressively free the model from GPU so the next model can load.
            self._release_pipeline(clm_checkpoint)

    @staticmethod
    def _release_pipeline(pipe):
        """Delete a HF pipeline and free all associated CUDA memory."""
        try:
            model = getattr(pipe, "model", None)
            if model is not None:
                try:
                    model.to("cpu")
                except Exception:
                    pass
                del model
            if hasattr(pipe, "model"):
                pipe.model = None
        except Exception as e:
            print(f"[cleanup] model release warning: {e}")
        try:
            del pipe
        except Exception:
            pass
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
            torch.cuda.synchronize()

    @staticmethod
    def _add_epochs_to_rows(rows, mlm_epoch, clm_checkpoint):
        for score in rows:
            score['mlm_epoch'] = mlm_epoch
            score['clm_checkpoint'] = clm_checkpoint
        return rows

    @staticmethod
    def _write_to_csv(rows, output_path):
        df = pd.DataFrame(rows)
        if output_path.exists():
            df.to_csv(output_path, index=False, header=None, mode='a')
        else:
            df.to_csv(output_path, index=False)

    def run_model_evaluation(self, output_filename=None):
        """
        Run the questionnaire evaluation on all configured CLM pipelines.

        Base models are scored with mode="raw"; models listed in
        instruct_models are scored with mode="chat". Each row is tagged with
        model_type ("base"/"chat"). GPU memory is released after every model.

        Parameters
        ----------
        output_filename : str, optional
            Name of the output CSV (default: "{questionnaire_name}_clm_results.csv").

        Returns
        -------
        Path
            Path to the output CSV file.
        """
        if output_filename is None:
            output_filename = f'{self.questionnaire_name.lower()}_clm_results.csv'

        output_path = self.result_path / output_filename

        questions = []
        for qs in self.split_questions:
            questions.extend(qs)

        print(f"\nRunning model evaluation with {len(questions)} question variants...")

        if output_path.exists():
            temp_df = pd.read_csv(output_path)
            indexes = temp_df.groupby(['model', 'Q']).count().index.values
            used_models = defaultdict(set)
            for k, v in indexes:
                used_models[k].add(v)
        else:
            used_models = {}

        for p in tqdm(self.clm_pipelines, desc="Evaluating models"):
            mode = self._model_mode(p)
            model_type = self._model_type(p)
            print(f"\nEvaluating model: {p}  (mode={mode}, type={model_type})")
            with warnings.catch_warnings():
                try:
                    warnings.simplefilter("ignore")

                    if p in used_models and not self.update:
                        pipeline_questions = []
                        for q in questions:
                            print(f"the item we try is: {self._question_attributes(q)['Q']}")
                            if self._question_attributes(q)['Q'] not in used_models[p]:
                                pipeline_questions.append(q)
                            else:
                                print('skip', p, self._question_attributes(q)['Q'])
                    else:
                        pipeline_questions = questions

                    if len(pipeline_questions) == 0:
                        print(f"All questions already evaluated for {p}, skipping...")
                        continue

                    rows = self._calc_scores(
                        pipeline_questions,
                        Path(p),
                        'base',
                        'evaluation',
                        mode,
                        model_type,
                    )
                    rows = self._add_epochs_to_rows(rows, 0, 0)
                    self._write_to_csv(rows, output_path)

                except Exception as e:
                    print(f"Error evaluating {p}: {e}")
                finally:
                    # Defensive: ensure memory is freed even on error paths.
                    gc.collect()
                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()
                        torch.cuda.ipc_collect()

        df = pd.read_csv(output_path)
        df = df.drop_duplicates(subset=['filter', 'softmax', 'model', 'Q'], keep='last')
        df.to_csv(output_path, index=False)

        print(f"\n✓ Model evaluation complete. Results saved to: {output_path}")
        return output_path

    # ---- Analysis methods -----------------------------------------------

    def load_results(self, csv_path, softmax, positiveonly, value='score',
                     index='model', columns='Q', model_type=None):
        """
        Load and pivot results. If model_type is given ("base" or "chat"),
        only rows of that population are used.
        """
        df = pd.read_csv(csv_path)

        # Filter by population when requested. Falls back gracefully if the
        # column is absent (older result files without the tag).
        if model_type is not None:
            if 'model_type' in df.columns:
                df = df[df['model_type'] == model_type]
            else:
                print("[load_results] warning: 'model_type' column not found; "
                      "returning unfiltered results.")

        if df['softmax'].isna().sum() > 0:
            softmax_filter = df['softmax'].isna()
        else:
            softmax_filter = df['softmax'] == ''

        if softmax:
            df = df[df['softmax'] == str(softmax)]
        else:
            df = df[softmax_filter]

        if value == 'silhouette_score':
            df = df[df['silhouette_score'] > -1]

        if positiveonly:
            df = df[df['filter'] == "positiveonly"]
        else:
            df = df[df['filter'] == "unfiltered"]

        return pd.pivot_table(df, values=value, index=index, columns=columns, aggfunc='mean')

    def calc_content_validity(self, results_csv, softmax=None, output_filename=None, model_type=None):
        if softmax is None:
            softmax = self.index + self.scales
        if output_filename is None:
            suffix = f"_{model_type}" if model_type else ""
            output_filename = f"linguistic_acceptability{suffix}.csv"

        cols = ['semantic_similarity', 'cola_score', 'silhouette_score']

        results = []
        for softmax_filter in [softmax]:
            q_res = [
                self.load_results(results_csv, softmax=softmax_filter, positiveonly=False,
                                  value=v, model_type=model_type).mean(axis=0)
                for v in cols
            ]
            results.append(pd.concat(q_res, axis=1))

        linguistic_acceptability_df = pd.concat(results, axis=0)
        linguistic_acceptability_df.columns = ['semantic_similarity', 'cola_score', 'silhouette_score']

        output_path = self.result_path / output_filename
        linguistic_acceptability_df.to_csv(output_path, index=True)

        label = f" ({model_type})" if model_type else ""
        print(f"\n✓ Content validity metrics{label} saved to: {output_path}")
        return linguistic_acceptability_df.sort_values('silhouette_score')

    def calc_cronbach_alpha(self, results_csv, softmax=None, positiveonly=True, model_type=None):
        if softmax is None:
            softmax = self.index + self.scales

        value = 'mean_score'
        results = []
        for softmax_filter in [softmax]:
            results.append(
                self.load_results(results_csv, softmax=softmax_filter, positiveonly=positiveonly,
                                  value=value, model_type=model_type)
            )

        data_df = pd.concat(results, axis=1)

        label = f" ({model_type})" if model_type else ""
        print(f'\nCronbach Alpha{label}:')
        factor_alphas = {}
        for subset in self.factors:
            feature_subset = [c for c in data_df.columns if subset in c]
            if len(feature_subset) > 1:
                alpha = pg.cronbach_alpha(data=data_df[feature_subset])
                print(f'{subset}: {alpha}')
                factor_alphas[subset] = alpha
            else:
                print(f'{subset}: Insufficient items (n={len(feature_subset)})')

        all_feature_subset = self._get_factor_sub_features(self.factors, data_df)
        if len(all_feature_subset) > 1:
            alpha = pg.cronbach_alpha(data=data_df[all_feature_subset])
            print(f'\n{self.questionnaire_name} Overall{label}: {alpha}')
            overall_alpha = alpha
        else:
            print(f'\n{self.questionnaire_name} Overall{label}: Insufficient items')
            overall_alpha = None

        return {
            'data_df': data_df,
            'overall': overall_alpha,
            'factors': factor_alphas,
        }

    def test_question_affect_on_cronbach_alpha(self, data_df, specific_factors=None):
        if specific_factors is None:
            subset_df = data_df
            alpha = pg.cronbach_alpha(data=subset_df)
            print('All Questions Alpha:', alpha)
            for feature in subset_df.columns:
                sub = [c for c in subset_df.columns if c != feature]
                alpha = pg.cronbach_alpha(data=subset_df[sub])
                print('without:', feature, 'Alpha:', alpha)
        else:
            if specific_factors == "all":
                specific_factors = self.factors
            for subset in specific_factors:
                feature_subset = [c for c in data_df.columns if subset in c]
                subset_df = data_df[feature_subset]
                alpha = pg.cronbach_alpha(data=subset_df)
                print(subset, 'Alpha:', alpha)
                for feature in subset_df.columns:
                    sub = [c for c in subset_df.columns if c != feature]
                    alpha = pg.cronbach_alpha(data=subset_df[sub])
                    print('without:', feature, 'Alpha:', alpha)

    def get_semantic_similarity(self, q=None):
        """Calculate semantic similarity for a question or all raw questions."""
        if q is None:
            results = {}
            for Q in tqdm(self.raw_questions, desc="Calculating semantic similarity"):
                q_instance = Q()
                description = q_instance._descriptor
                strOriginal = self._clean_original(description)

                scores = []
                for kmap in q_instance._keywords_map:
                    strPermutation = self._render(q_instance, kmap)
                    embeddings1 = self.sentence_embedding_model.encode(strOriginal, convert_to_tensor=True)
                    embeddings2 = self.sentence_embedding_model.encode(strPermutation, convert_to_tensor=True)
                    cosine_scores = util.cos_sim(embeddings1, embeddings2)
                    scores.append(cosine_scores.item())

                question_name = f"{description['Questionnair']}{description['Factor']}{description['Ordinal']}"
                results[question_name] = np.percentile(scores, 75)

            return pd.DataFrame.from_dict(results, orient='index', columns=['semantic_similarity'])

        description = q._descriptor
        strOriginal = self._clean_original(description)

        scores = []
        for kmap in q._keywords_map:
            strPermutation = self._render(q, kmap)
            embeddings1 = self.sentence_embedding_model.encode(strOriginal, convert_to_tensor=True)
            embeddings2 = self.sentence_embedding_model.encode(strPermutation, convert_to_tensor=True)
            cosine_scores = util.cos_sim(embeddings1, embeddings2)
            scores.append(cosine_scores.item())

        return np.percentile(scores, 75)

    def get_cola_score(self, q=None):
        """Calculate COLA (linguistic acceptability) for a question or all raw questions."""
        if q is None:
            results = {}
            for Q in tqdm(self.raw_questions, desc="Calculating COLA scores"):
                q_instance = Q()
                description = q_instance._descriptor

                scores = []
                for kmap in q_instance._keywords_map:
                    strPermutation = self._render(q_instance, kmap)
                    cola_result = self.cola(strPermutation)[0]
                    scores.append(cola_result.get('score'))

                question_name = f"{description['Questionnair']}{description['Factor']}{description['Ordinal']}"
                results[question_name] = np.mean(scores)

            return pd.DataFrame.from_dict(results, orient='index', columns=['cola_score'])

        scores = []
        for kmap in q._keywords_map:
            strPermutation = self._render(q, kmap)
            cola_result = self.cola(strPermutation)[0]
            scores.append(cola_result.get('score'))

        return np.mean(scores)

    def calc_correlations(self, results_csv, softmax=None, positiveonly=True, method='spearman', model_type=None):
        if softmax is None:
            softmax = self.index + self.scales

        value = 'mean_score'

        results = []
        for softmax_filter in [softmax]:
            results.append(
                self.load_results(results_csv, softmax=softmax_filter, positiveonly=positiveonly,
                                  value=value, model_type=model_type)
            )

        data_df = pd.concat(results, axis=1)
        filtered_df = pd.DataFrame()

        for factor in self.factors:
            feature_subset = self._get_factor_sub_features([factor], data_df)
            if len(feature_subset) > 0:
                filtered_df[factor] = data_df[feature_subset].mean(axis=1)

        all_feature_subset = self._get_factor_sub_features(self.factors, data_df)
        filtered_df[self.questionnaire_name] = data_df[all_feature_subset].mean(axis=1)

        corr_df = filtered_df.rcorr(method=method)
        label = f" ({model_type})" if model_type else ""
        print(f"\n✓ Factor correlations{label} ({method}):")
        print(corr_df)

        return corr_df

    @staticmethod
    def _get_factor_sub_features(factor_list, data_df):
        feature_subset = []
        for subset in factor_list:
            feature_subset += [c for c in data_df.columns if subset in c]
        return list(set(feature_subset))

    def run_validation(self, output_filename=None):
        """
        Run the full validation pipeline (single combined evaluation pass).

        Note: this runs the analysis once over ALL models combined. To analyze
        the base and chat populations separately, call the analysis methods
        manually with model_type="base" / model_type="chat" on the returned
        results_csv (see notebook cells).
        """
        print(f"\n{'='*70}")
        print(f"Running Complete CLM Validation for {self.questionnaire_name} Questionnaire")
        print(f"{'='*70}")

        results_csv = self.run_model_evaluation(output_filename)

        print(f"\n{'='*70}")
        print("Calculating Content Validity Metrics (all models)")
        print(f"{'='*70}")
        content_validity = self.calc_content_validity(results_csv)
        print("\nContent Validity Results:")
        print(content_validity)

        print(f"\n{'='*70}")
        print("Calculating Internal Consistency (Cronbach's Alpha, all models)")
        print(f"{'='*70}")
        alpha_results = self.calc_cronbach_alpha(results_csv)

        print(f"\n{'='*70}")
        print("Calculating Factor Correlations (all models)")
        print(f"{'='*70}")
        correlations = self.calc_correlations(results_csv)

        print(f"\n{'='*70}")
        print("Validation Complete!")
        print(f"{'='*70}")
        print(f"Results saved in: {self.result_path}")

        return {
            'results_csv': results_csv,
            'content_validity': content_validity,
            'cronbach_alpha': alpha_results,
            'correlations': correlations,
        }