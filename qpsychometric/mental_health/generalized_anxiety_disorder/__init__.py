from .gad_qmnli import gad_qmnli_list
from .gad_qmlm import gad_qmmlm_list

gad_questionnaire = {'QMNLI':gad_qmnli_list, 'QMLM':gad_qmmlm_list}

__all__ = ['gad_questionnaire']