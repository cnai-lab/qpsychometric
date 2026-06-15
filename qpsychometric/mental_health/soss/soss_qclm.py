from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg

agreement_weights = {
    "strongly agree" : 2,
    "agree" : 1,
    "disagree" : -1,
    "strongly disagree" : -2
}


class SOSSQ1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: IN THE PAST WEEK, have you felt {question}? Answer: {answer}",
            dimensions={
            "answer":agreement_weights,
            "question":dict_pos_neg(['inadequate', 'insufficient', 'incompetent'], 
                                 ['adequate', 'capable', 'enough'],1.0),
            },
            descriptor = {"Questionnair":"SOSS",
              "Factor":"Personal Vulnerability",
              "Ordinal":1,
              "Original":'IN THE PAST WEEK, have you felt: inadequate?'
            },
            **kwargs
        )
        
class SOSSQ2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: IN THE PAST WEEK, have you felt {question} by your responsibilities? Answer: {answer}",
            dimensions={
            "answer":agreement_weights,
            "question":dict_pos_neg(['swamped', 'overwhelmed', 'buried'], 
                                 ['unburdened', 'unbothered'],1.0),
            },
            descriptor = {"Questionnair":"SOSS",
              "Factor":"Event Load",
              "Ordinal":2,
              "Original":'IN THE PAST WEEK, have you felt: swamped by your responsibilities?'
            },
            **kwargs
        )
        
        
        
class SOSSQ3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: IN THE PAST WEEK, have you felt that the odds were {question} you? Answer: {answer}",
            dimensions={
            "answer":agreement_weights,
            "question":dict_pos_neg(['against', 'opposing'], 
                                 ['aligned with', 'favoring'],1.0),
            },
            descriptor = {"Questionnair":"SOSS",
              "Factor":"Personal Vulnerability",
              "Ordinal":3,
              "Original":'IN THE PAST WEEK, have you felt: that the odds were against you?'
            },
            **kwargs
        )
        
        
        
class SOSSQ4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: IN THE PAST WEEK, have you felt that there was {question} time to get to everything? Answer: {answer}",
            dimensions={
            "answer":agreement_weights,
            "question":dict_pos_neg(['too little', 'insufficient', 'not enough'], 
                                 ['enough', 'plenty of', 'ample'],1.0),
            },
            descriptor = {"Questionnair":"SOSS",
              "Factor":"Event Load",
              "Ordinal":4,
              "Original":'IN THE PAST WEEK, have you felt: that there wasn’t enough time to get to everything?'
            },
            **kwargs
        )
        
        
class SOSSQ5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: IN THE PAST WEEK, have you felt like everything was {question}? Answer: {answer}",
            dimensions={
            "answer":agreement_weights,
            "question":dict_pos_neg(['falling apart', 'out of control', 'breaking down'], 
                                 ['going smoothly', 'on track'],1.0),
            },
            descriptor = {"Questionnair":"SOSS",
              "Factor":"Personal Vulnerability",
              "Ordinal":5,
              "Original":'IN THE PAST WEEK, have you felt: like nothing was going right?'
            }, 
            **kwargs
        )
        
        
        
class SOSSQ6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: IN THE PAST WEEK, have you felt like you were {question}? Answer: {answer}",
            dimensions={
            "answer":agreement_weights,
            "question":dict_pos_neg(['rushed', 'hurried', 'under time pressure'], 
                                 ['in control of your pace', 'moving at your own speed', 'unhurried', 'calm'],1.0),
            },
            descriptor = {"Questionnair":"SOSS",
              "Factor":"Event Load",
              "Ordinal":6,
              "Original":'IN THE PAST WEEK, have you felt: like you were rushed?'
            },
            **kwargs
        )
        
        
        
class SOSSQ7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: IN THE PAST WEEK, have you felt like you were {question}? Answer: {answer}",
            dimensions={
            "answer":agreement_weights,
            "question":dict_pos_neg(['trapped', 'in a dead end', 'cornered'], 
                                 ['liberated','released'],1.0),
            },
            descriptor = {"Questionnair":"SOSS",
              "Factor":"Personal Vulnerability",
              "Ordinal":7,
              "Original":'IN THE PAST WEEK, have you felt: like there was no escape?'
            },
            **kwargs
        )
        
        
class SOSSQ8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: IN THE PAST WEEK, have you felt like things kept {question} ? Answer: {answer}",
            dimensions={
            "answer":agreement_weights,
            "question":dict_pos_neg(['piling up', 'stacking up', 'accumulating'], 
                                 ['clearing up', 'lightening', 'getting resolved'],1.0),
            },
            descriptor = {"Questionnair":"SOSS",
              "Factor":"Event Load",
              "Ordinal":8,
              "Original":'IN THE PAST WEEK, have you felt: like things kept piling up?'
            },
            **kwargs
        )
        
        
        
class SOSSQ9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: IN THE PAST WEEK, have you felt like just {question}? Answer: {answer}",
            dimensions={
            "answer":agreement_weights,
            "question":dict_pos_neg(['quitting', 'giving up'], 
                                 ['holding on', 'staying strong'],1.0),
            },
            descriptor = {"Questionnair":"SOSS",
              "Factor":"Personal Vulnerability",
              "Ordinal":9,
              "Original":'IN THE PAST WEEK, have you felt: like just giving up?'
            },
            **kwargs
        )
        
        
class SOSSQ10(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: IN THE PAST WEEK, have you felt like you were {question}? Answer: {answer}",
            dimensions={
            "answer":agreement_weights,
            "question":dict_pos_neg(['carrying a heavy load', 'weighed down'], 
                                 ['light as a feather', 'stress free'],1.0),
            },
            descriptor = {"Questionnair":"SOSS",
              "Factor":"Event Load",
              "Ordinal":10,
              "Original":'IN THE PAST WEEK, have you felt: like you were carrying a heavy load?'
            },
            **kwargs
        )
        

soss_qclm_list = [SOSSQ1, SOSSQ2, SOSSQ3, SOSSQ4, SOSSQ5, SOSSQ6, SOSSQ7, SOSSQ8, SOSSQ9, SOSSQ10]