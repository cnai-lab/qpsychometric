from .panas_s_qclm import panas_s_qclm_list
from .panas_t_qclm import panas_t_qclm_list
import pandas as pd
import os
from ...utils import QuestionnaireData, verify_df_intergrity



data = []

# Get the name of the parent directory of the current file directory
parent_directory_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
category_name = parent_directory_name


def get_questionnaire_info(question_class):
    task_name = question_class.__bases__[0].__name__
    question_obj = question_class()
    questionnaire_name = question_obj._descriptor["Questionnair"]
    return task_name, questionnaire_name


if panas_s_qclm_list:
    question_class_nli = panas_s_qclm_list[0]
    task_name, questionnaire_name = get_questionnaire_info(question_class_nli)
    for clm_question in panas_s_qclm_list:
        data.append((category_name, questionnaire_name, task_name, clm_question))

if panas_t_qclm_list:
    question_class_nli = panas_t_qclm_list[0]
    task_name, questionnaire_name = get_questionnaire_info(question_class_nli)
    for clm_question in panas_t_qclm_list:
        data.append((category_name, questionnaire_name, task_name, clm_question))


panas_questionnaire = QuestionnaireData(pd.DataFrame(data, columns=['category_name', 'questionnaire_name', 'questionnaire_task', 'question']))

__all__ = ['panas_questionnaire']
