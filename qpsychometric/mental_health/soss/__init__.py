from .soc_qclm import soss_qclm_list
import os
import pandas as pd
from ...utils import QuestionnaireData

data = []

parent_directory_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
category_name = parent_directory_name


def get_questionnaire_info(question_class):
    task_name = question_class.__bases__[0].__name__
    question_obj = question_class()
    questionnaire_name = question_obj._descriptor["Questionnair"]
    return task_name, questionnaire_name


if soss_qclm_list:
    question_class_nli = soss_qclm_list[0]
    task_name, questionnaire_name = get_questionnaire_info(question_class_nli)
    for clm_question in soss_qclm_list:
        data.append((category_name, questionnaire_name, task_name, clm_question))

soss_questionnaire = QuestionnaireData(pd.DataFrame(data, columns=['category_name', 'questionnaire_name', 'questionnaire_task', 'question']))

__all__ = ['soss_questionnaire']