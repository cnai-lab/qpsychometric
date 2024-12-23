from .phq_qmnli import phq_qmnli_list
from .phq_qmlm import phq_qmlm_list


phq_questionnaire = {'QMNLI':phq_qmnli_list, 'QMLM':phq_qmlm_list}



__all__ = ['phq_questionnaire']