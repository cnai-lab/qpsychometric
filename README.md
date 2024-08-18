# qpsychometric

This package contains several psychometric questionnaires from the following categories:
- Mental health
- Personality traits
- Social biases

These psychometric questionnaires will help you to assess your model's biases and behavioural tendencies.
Currently contains the following questionnaires: ASI, BIG5, Compassion Scale, GAD, PHQ, SD3, SOC.

## List of questionnaires are available for running
* ASI:
  * asi_all_qmnli (all questions of ASI)
  * asi_bg_qmnli (questions from the benevolent sexism - complementary gender differentiation category of ASI)
  * asi_bi_qmnli (questions from the benevolent sexism - heterosexual intimacy category of ASI)
  * asi_bp_qmnli (questions from the benevolent sexism - protective paternalism category of ASI)
  * asi_h_qmnli (questions from the hostile sexism category of ASI)
* BIG5:
  * big5_qmnli (all questions of BIG5)
* CS:
  * compassion_scale_qmnli (all questions of CS)
* GAD:
  * gad2_qmnli (first 2 questions of GAD)
  * gad7_qmnli (all questions of GAD)
* PHQ:
  * phq2_qmnli (first 2 questions of PHQ)
  * phq7_qmnli (all questions of PHQ)
* SD3:
  * sd3_qmnli (all questions of SD3)
  * sd3_machiavellianism_qmnli (questions from the machiavellianism category of SD3)
  * sd3_narcissism_qmnli (questions from the narcissism category of SD3)
  * sd3_psychopathy_qmnli (questions from the psychopathy category of SD3)
* SOC:
  * soc_qmnli (all questions of SOC)

## Structure of the qpsychometric package:
qpsychometric<br>
|-mental_health<br>
| |-generalized_anxiety_disorder (GAD)<br>
| |-patient_health_questionnaire (PHQ)<br>
| |-sense_of_coherence (SOC)<br>
|-personality_traits<br>
| |-big5 (BIG5)<br>
| |-compassion_scale (Compassion Scale)<br>
| |-sd3 (SD3)<br>
|-social_biases<br>
| |-ambivalent_sex_inventory (ASI)<br>

## Commands and steps for running a questionnaire:

* How to install the qlatent package:
  ```
  %pip install qlatent
  ```
* How to import the classes of the questionnaires:
  ```
  from qlatent.qmnli.qmnli import *
  ```
* How to load an NLI model from huggingface.com into a pipeline a few simple steps:
  ```
  device = 0 if torch.cuda.is_available() else -1  # (0 is CUDA, -1 is CPU)
  p = "typeform/distilbert-base-uncased-mnli"  # You may replace the presented path with another MNLI model's path
  nli = pipeline("zero-shot-classification",device=device, model=p)
  nli.model_identifier = p
  ```
* How to load a question:
  ```
  """
  The format for importing the question from the right questionnaire is the following:
   from qpsychometric.<category_underscored>.<full_questionnaire_name_underscored>.<full_questionnaire_name_underscored> import <question_name>
  For example:
  """
  
  from qpsychometric.social_biases.ambivalent_sexism_inventory.ambivalent_sexism_inventory import ASIQ2
  from qpsychometric.personality_traits.compassion_scale.compassion_scale import CSQ10
  from qpsychometric.mental_health.sense_of_coherence.sense_of_coherence import SOCQ28
  ```
* How to load a questionnaire:
  ```
  """
  The format for importing a questionnaire is the following:
   from qpsychometric.<category_with_underscores>.<full_questionnaire_name_with_underscores>.<full_questionnaire_name_with_underscores> import <questionnaire_name>
  For example:
  """
  
  from qpsychometric.social_biases.ambivalent_sexism_inventory.ambivalent_sexism_inventory import asi_h_qmnli
  from qpsychometric.personality_traits.compassion_scale.compassion_scale import compassion_scale_qmnli
  from qpsychometric.mental_health.sense_of_coherence.sense_of_coherence import soc_qmnli
  ```
* How to run a question from a questionnaire through an MNLI pipeline:<br>
  This package includes (as it relies on) the package qlatent.<br>
  The qlatent package contains a description that explains how to run QMNLI (and _QMNLI) questions.<br>
  Look at these descriptions for the info you need.<br>
* How to run a full questionnaire:
  ```
  """
  Simply iterate through the questionnaire (as it is a list of questions),
  and apply the code for running a question on each question individually.
  """

  for Q in tqdm(<questionnaire_name>):
    Qs = split_question(Q,
                        index=Q.q_index,
                        scales=[Q.q_scale],
                        softmax=[True],
                        filters={'unfiltered':{},
                                "positiveonly":Q().get_filter_for_postive_keywords()
                                },
                        )
    print(Qs[0]._descriptor['Ordinal'])
    Qs[0].run(mnli)  # you may add .mean_score() or .report() after the run() function
  ```
