from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg

frequency_weights:SCALE = {
    'never':-4,
    'very rarely':-3,
    'seldom':3,
    'rarely':4,
    'frequently':5,
    'often':5,
    'very frequently':6,
    'always':7,    
}
    

basic_empathy_scale_qclm_list = [BESQ1, BESQ2, BESQ3, BESQ4, BESQ5, BESQ6, BESQ7, BESQ8, BESQ9, BESQ10, BESQ11, BESQ12, BESQ13, BESQ14, BESQ15, BESQ16, BESQ17, BESQ18, BESQ19, BESQ20]