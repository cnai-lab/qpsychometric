import unittest
import importlib
from tqdm.auto import tqdm

from qlatent.qmnli.qmnli import *
from qlatent.qmnli.qmnli import _QMNLI, QMNLI

import qpsychometric.social_biases.ambivalent_sexism_inventory.asi_qmnli
from qpsychometric.social_biases.ambivalent_sexism_inventory.asi_qmnli import *
import qpsychometric.personality_traits.big5.big5_qmnli
from qpsychometric.personality_traits.big5.big5_qmnli import *
import qpsychometric.personality_traits.short_dark_triad.sd3_qmnli
from qpsychometric.personality_traits.short_dark_triad.sd3_qmnli import *
import qpsychometric.mental_health.sense_of_coherence.soc_qmnli
from qpsychometric.mental_health.sense_of_coherence.soc_qmnli import *
import qpsychometric.mental_health.patient_health_questionnaire.phq_qmnli
from qpsychometric.mental_health.patient_health_questionnaire.phq_qmnli import *
import qpsychometric.mental_health.generalized_anxiety_disorder.gad_qmnli
from qpsychometric.mental_health.generalized_anxiety_disorder.gad_qmnli import *
import qpsychometric.personality_traits.compassion_scale.compassion_scale_qmnli
from qpsychometric.personality_traits.compassion_scale.compassion_scale_qmnli import *

import torch
device = 0 if torch.cuda.is_available() else -1
print(device)

p = "typeform/distilbert-base-uncased-mnli"
mnli = pipeline("zero-shot-classification",device=device, model=p)
mnli.model_identifier = p

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

def test_questionnaire(module, questionnaire_qmnli : list[QMNLI]) -> list[bool]:
    
    questions_equalities = []

    for Q in tqdm(questionnaire_qmnli):
        Qs = split_question(Q,
                            index=Q.index,
                            scales=[Q.scale],
                            softmax=[True],
                            filters={'unfiltered':{},
                                    "positiveonly":Q().get_filter_for_postive_keywords()
                                    },
                            )
        print(Qs[0]._descriptor['Ordinal'])
        Qs[0].run(mnli)
        q_pdf = Qs[0]._pdf
        Q_same = Q.__name__
        Q_func = getattr(module, Q_same)
        Qs = split_question(Q_func,
                            index=Q_func.index,
                            scales=[Q_func.scale],
                            softmax=[True],
                            filters={'unfiltered':{},
                                    "positiveonly":Q().get_filter_for_postive_keywords()
                                    },
                            )
        print(Qs[0]._descriptor['Ordinal'])
        Qs[0].run(mnli)
        questions_equalities.append(q_pdf.equals(Qs[0]._pdf))
    
    return questions_equalities

class TestQuestionnairesMethods(unittest.TestCase):

    asi_module = qpsychometric.social_biases.ambivalent_sexism_inventory.asi_qmnli
    asi_questionnaire = asi_qmnli
    
    big5_module = qpsychometric.personality_traits.big5.big5_qmnli
    big5_questionnaire = big5_qmnli

    sd3_module = qpsychometric.personality_traits.short_dark_triad.sd3_qmnli
    sd3_questionnaire = sd3_qmnli

    soc_module = qpsychometric.mental_health.sense_of_coherence.soc_qmnli
    soc_questionnaire = soc_qmnli

    phq_module = qpsychometric.mental_health.patient_health_questionnaire.phq_qmnli
    phq_questionnaire = phq_qmnli

    gad_module = qpsychometric.mental_health.generalized_anxiety_disorder.gad_qmnli
    gad_questionnaire = gad_qmnli

    compassion_scale_module = qpsychometric.personality_traits.compassion_scale.compassion_scale_qmnli
    compassion_scale_questionnaire = compassion_scale_qmnli
    
    def test_asi_questionnaire(self):
        questions_equalities = test_questionnaire(self.asi_module, self.asi_questionnaire)
        self.assertTrue(expr=False not in questions_equalities)

    def test_big5_questionnaire(self):
        questions_equalities = test_questionnaire(self.big5_module, self.big5_questionnaire)
        self.assertTrue(expr=False not in questions_equalities)

    def test_sd3_questionnaire(self):
        questions_equalities = test_questionnaire(self.sd3_module, self.sd3_questionnaire)
        self.assertTrue(expr=False not in questions_equalities)

    def test_soc_questionnaire(self):
        questions_equalities = test_questionnaire(self.soc_module, self.soc_questionnaire)
        self.assertTrue(expr=False not in questions_equalities)

    def test_phq_questionnaire(self):
        questions_equalities = test_questionnaire(self.phq_module, self.phq_questionnaire)
        self.assertTrue(expr=False not in questions_equalities)

    def test_gad_questionnaire(self):
        questions_equalities = test_questionnaire(self.gad_module, self.gad_questionnaire)
        self.assertTrue(expr=False not in questions_equalities)

    def test_compassion_scale_questionnaire(self):
        questions_equalities = test_questionnaire(self.compassion_scale_module, self.compassion_scale_questionnaire)
        self.assertTrue(expr=False not in questions_equalities)

    def test_asi_middle_question(self):
        kw_fairness = ['sexist', 'prejudiced', 'improper',]
        kw_favors   = ['legitimate', 'rightful', 'reasonable']
        kw_all      = kw_fairness + kw_favors
        kw_all.sort()
        
        middle_question = get_middle_question(self.asi_questionnaire)
        kw = list(middle_question._dimensions['index'].keys())
        kw.sort()

        self.assertEqual(kw_all, kw)

    def test_big5_middle_question(self):
        emo_pos = ['sociable', 'in the center of attention']
        emo_neg = ['quiet', 'reserved', 'shy']
        emo_all = emo_pos + emo_neg
        emo_all.sort()
        
        middle_question = get_middle_question(self.big5_questionnaire)
        emo = list(middle_question._dimensions['emotion'].keys())
        emo.sort()

        self.assertEqual(emo_all, emo)

    def test_sd3_middle_question(self):
        emo_pos = ['like', 'love', 'want to']
        emo_neg = ['hate', 'dislike', 'despise']
        emo_all = emo_pos + emo_neg
        emo_all.sort()
        
        middle_question = get_middle_question(self.sd3_questionnaire)
        emo = list(middle_question._dimensions['emotion'].keys())
        emo.sort()

        self.assertEqual(emo_all, emo)

    def test_soc_middle_question(self):
        kw_attitude_pos = ['clear', 'coherent', 'logical', 'comprehensible']
        kw_attitude_neg   = ['mixed-up', 'confounded']
        kw_all      = kw_attitude_pos + kw_attitude_neg
        kw_all.sort()
        
        middle_question = get_middle_question(self.soc_questionnaire)
        kw = list(middle_question._dimensions['index'].keys())
        kw.sort()

        self.assertEqual(kw_all, kw)

    def test_phq_middle_question(self):
        emo_pos = ['poor appetite', 'been overeating']
        emo_neg = ['healthy appetite', 'satisfying appetite']
        emo_all = emo_pos + emo_neg
        emo_all.sort()
        
        middle_question = get_middle_question(self.phq_questionnaire)
        emo = list(middle_question._dimensions['emotion'].keys())
        emo.sort()

        self.assertEqual(emo_all, emo)

    def test_gad_middle_question(self):
        emo_pos = ['trouble', 'difficulty']
        emo_neg = ['no problem', 'an easy time']
        emo_all = emo_pos + emo_neg
        emo_all.sort()
        
        middle_question = get_middle_question(self.gad_questionnaire)
        emo = list(middle_question._dimensions['emotion'].keys())
        emo.sort()

        self.assertEqual(emo_all, emo)

    def test_compassion_scale_middle_question(self):
        kw_attitude_pos = ['correct', 'true', 'accurate', 'a fact']
        kw_attitude_neg = ['incorrect', 'false', 'imprecise', 'invalid']
        kw_all = kw_attitude_pos + kw_attitude_neg
        kw_all.sort()
        
        middle_question = get_middle_question(self.compassion_scale_questionnaire)
        kw = list(middle_question._dimensions['index'].keys())
        kw.sort()

        self.assertEqual(kw_all, kw)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestQuestionnairesMethods('test_asi_questionnaire'))
    suite.addTest(TestQuestionnairesMethods('test_big5_questionnaire'))
    suite.addTest(TestQuestionnairesMethods('test_sd3_questionnaire'))
    suite.addTest(TestQuestionnairesMethods('test_soc_questionnaire'))
    suite.addTest(TestQuestionnairesMethods('test_phq_questionnaire'))
    suite.addTest(TestQuestionnairesMethods('test_gad_questionnaire'))
    suite.addTest(TestQuestionnairesMethods('test_compassion_scale_questionnaire'))
    suite.addTest(TestQuestionnairesMethods('test_asi_middle_question'))
    suite.addTest(TestQuestionnairesMethods('test_big5_middle_question'))
    suite.addTest(TestQuestionnairesMethods('test_sd3_middle_question'))
    suite.addTest(TestQuestionnairesMethods('test_soc_middle_question'))
    suite.addTest(TestQuestionnairesMethods('test_phq_middle_question'))
    suite.addTest(TestQuestionnairesMethods('test_gad_middle_question'))
    suite.addTest(TestQuestionnairesMethods('test_compassion_scale_middle_question'))
    return suite

runner = unittest.TextTestRunner()
runner.run(suite())