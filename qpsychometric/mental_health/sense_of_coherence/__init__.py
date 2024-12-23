from .soc_qmnli import soc_qmnli_list
from .soc_qmlm import soc_qmlm_list

soc_questionnaire = {'QMNLI':soc_qmnli_list, 'QMLM':soc_qmlm_list}


__all__ = ['soc_questionnaire']