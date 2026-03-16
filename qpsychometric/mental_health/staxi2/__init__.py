from .staxi2_qclm import staxi2_qclm_list
import pandas as pd
import os
from ...utils import QuestionnaireData, verify_df_intergrity


data = []

parent_directory_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
category_name = parent_directory_name


def get_questionnaire_info(question_class):
    task_name = question_class.__bases__[0].__name__
    question_obj = question_class()
    questionnaire_name = question_obj._descriptor["Questionnair"]
    return task_name, questionnaire_name


if staxi2_qclm_list:
    question_class_nli = staxi2_qclm_list[0]
    task_name, questionnaire_name = get_questionnaire_info(question_class_nli)
    for clm_question in staxi2_qclm_list:
        data.append((category_name, questionnaire_name, task_name, clm_question))


staxi2_questionnaire = QuestionnaireData(pd.DataFrame(data, columns=['category_name', 'questionnaire_name', 'questionnaire_task', 'question']))

__all__ = ['staxi2_questionnaire']
