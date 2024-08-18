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
  p = "<huggingface_model_path>"  # (Replace <huggingface_model_path> with an actual path. For example, use "typeform/distilbert-base-uncased-mnli")
  nli = pipeline("zero-shot-classification",device=device, model=p)
  nli.model_identifier = p
  ```
* How to load a question:
  ```
  """
  As mentioned before, the package contains 3 categories of questionnaires:
   Mental health
   Personality traits
   Social biases
  
  The package provides the following questionnaires:
   ASI - 22 questions (1-22)
   BIG5 - 14 questions (1-14)
   CS - 24 questions (1-24)
   GAD - 7 questions (1-7)
   PHQ - 9 questions (1-9)
   SD3 - 27 questions (1-27)
   SOC - 12 questions (4-6, 8, 12, 16, 19, 21, 25-26, 28-29)
  
  The format for a question's name is the following:
   <shortened_questionnaire_name>Q<question_number>
  For example:
   ASIQ2
   CSQ10
   SOCQ28

  The format for importing the question from the right questionnaire is the following:
   from qpsychometric.<category_with_underscores>.<full_questionnaire_name_with_underscores>.<full_questionnaire_name_with_underscores> import <question_name>
  For example:
   from qpsychometric.social_biases.ambivalent_sexism_inventory.ambivalent_sexism_inventory import ASIQ2
   from qpsychometric.personality_traits.compassion_scale.compassion_scale import CSQ10
   from qpsychometric.mental_health.sense_of_coherence.sense_of_coherence import SOCQ28
  """
  ```
* How to load a questionnaire:
  ```
  """
  As mentioned in the previous section (about how to load a question), the package provides the following questionnaires:
   ASI - 22 questions (1-22)
   BIG5 - 14 questions (1-14)
   CS - 24 questions (1-24)
   GAD - 7 questions (1-7)
   PHQ - 9 questions (1-9)
   SD3 - 27 questions (1-27)
   SOC - 12 questions (4-6, 8, 12, 16, 19, 21, 25-26, 28-29)

  The questionnaires are located in at least 1 list, because questionnaires are lists of questions:
   ASI - asi_qmnli (questions 1-22)
         asi_bg_qmnli (questions 8, 19, 22)
         asi_bi_qmnli (questions 1, 6, 12-13)
         asi_bp_qmnli (questions 3, 9, 17, 20)
         asi_h_qmnli (questions 2, 4-5, 7, 10-11, 14-16, 18, 21)
   BIG5 - big5_qmnli (questions 1-14)
   CS - compassion_scale_qmnli (questions 1-24)
   GAD - gad2_qmnli (questions 1-2)
         gad7_qmnli (questions 1-7)
         gad_qmnli (A.K.A gad7_qmnli)
   PHQ - phq2_qmnli (questions 1-2)
         phq9_qmnli (questions 1-9)
         phq_qmnli (A.K.A phq9_qmnli)
   SD3 - sd3_qmnli (questions 1-27)
         sd3_machiavellianism_qmnli (questions 1, 4, 7, 10, 13, 16, 19, 22, 25)
         sd3_narcissism_qmnli (questions 2, 5, 8, 11, 14, 17, 20, 23, 26)
         sd3_psychopathy_qmnli (questions 3, 6, 9, 12, 15, 18, 21, 24, 27)
   SOC - soc_qmnli (question 4-6, 8, 12, 16, 19, 21, 25-26, 28-29)

  The format for importing a questionnaire is the following:
   from qpsychometric.<category_with_underscores>.<full_questionnaire_name_with_underscores>.<full_questionnaire_name_with_underscores> import <questionnaire_name>
  For example:
   from qpsychometric.social_biases.ambivalent_sexism_inventory.ambivalent_sexism_inventory import asi_h_qmnli
   from qpsychometric.personality_traits.compassion_scale.compassion_scale import compassion_scale_qmnli
   from qpsychometric.mental_health.sense_of_coherence.sense_of_coherence import soc_qmnli
  """
  ```
* How to run a question from a questionnaire through an MNLI pipeline: ?
* How to run a report for a question's performance: ?
* How to run a full questionnaire: ?

## Run examples:
Load MNLI pipeline
```
p = "typeform/distilbert-base-uncased-mnli"
mnli = pipeline("zero-shot-classification",device=device, model=p)
mnli.model_identifier = p
```

Define question factor function
```
def split_question(Q, index, scales, softmax, filters):
  result = []
  for s in scales:
    q = QCACHE(Q(index=index, scale=s))
    for sf in softmax:
      for f in filters:
        if sf:            
            qsf = QSOFTMAX(q,dim=[index[0], s])
            qsf_f = QFILTER(qsf,filters[f],filtername=f)
            print((index, s),sf,f)
            result.append(qsf_f)
        else:
            qsf = QPASS(q,descupdate={'softmax':''})
            qsf_f = QFILTER(qsf,filters[f],filtername=f)
            print(s,sf,f)
            result.append(qsf_f)
  return result

```

Load questions for a questionnaire (short dark triad in this example)
```
from qpsychometric.personality_traits.short_dark_triad.sd3_qmnli import sd3_qmnli

for Q in tqdm(sd3_qmnli):
    Qs = split_question(Q,
                        index=Q.q_index,
                        scales=[Q.q_scale],
                        softmax=[True],
                        filters={'unfiltered':{},
                                "positiveonly":Q().get_filter_for_postive_keywords()
                                },
                        )
    print(Qs[0]._descriptor['Ordinal'])
    Qs[0].run(mnli).mean_score()
```

You can also load all available questions and run them. Here we load questions from files that ends with "_qmnli.py".
```
from qpsychometric.utils import load_questions

all_questions = load_questions(pattern='_qmnli.py')

for Q in tqdm(all_questions):
    Qs = split_question(Q,
                        index=Q.q_index,
                        scales=[Q.q_scale],
                        softmax=[True],
                        filters={'unfiltered':{},
                                "positiveonly":Q().get_filter_for_postive_keywords()
                                },
                        )
    print(Qs[0]._descriptor)
    Qs[0].run(mnli).mean_score()
```
?
