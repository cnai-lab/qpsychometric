from .asi_qmnli import asi_qmnli_list
from .asi_qmlm import asi_qmlm_list

asi_questionnaire = {'QMNLI':asi_qmnli_list, 'QMLM':asi_qmlm_list}

__all__ = ['asi_questionnaire']