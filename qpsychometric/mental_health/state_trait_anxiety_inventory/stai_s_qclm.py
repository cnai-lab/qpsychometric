from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg

likert_weights:SCALE = {
    "not at all" : -2,
    "somewhat" : -1,
    "moderately" : 1,
    "very much" : 2
}

class STAISQ1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['agitated', 'nervous', 'troubled'],
                                    ['calm', 'peaceful', 'tranquil'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":1,
              "Original":'I feel calm'
            },
            **kwargs
        )



class STAISQ2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['unsecure', 'unsafe', 'unprotected'], 
                                    ['secure', 'safe', 'protected'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":2,
              "Original":'I feel secure'
            },
            **kwargs
        )
        
        


class STAISQ3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['tense', 'stressed', 'agitated'], 
                                    ['calm', 'composed', 'unworried'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":3,
              "Original":'I am tense'
            },
            **kwargs
        )
        
        


class STAISQ4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['regretful', 'sorry', 'remorseful'], 
                                    ['content', 'satisfied', 'not guilty'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":4,
              "Original":'I am regretful'
            },
            **kwargs
        )
        

class STAISQ5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['nervous', 'upset', 'worried'], 
                                    ['at ease', 'carefree', 'composed', 'relaxed'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":5,
              "Original":'I feel at ease'
            },
            **kwargs
        )
        


class STAISQ6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['upset', 'disturbed', 'bothered'], 
                                    ['composed ', 'calm', 'comforted'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":6,
              "Original":'I feel upset'
            },
            **kwargs
        )
        

class STAISQ7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question} about possible misfortunes? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['worried', 'troubled', 'concerned'], 
                                    ['relaxed', 'uncaring', 'calm'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":7,
              "Original":'I am currently worried about possible misfortunes'
            },
            **kwargs
        )


class STAISQ8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['fatigued', 'tired', 'wearied'], 
                                    ['rested', 'restored', 'recovered', 'refreshed', 'relaxed'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":8,
              "Original":'I feel rested'
            },
            **kwargs
        )


class STAISQ9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['anxious', 'worried', 'tense'], 
                                    ['cool', 'calm', 'collected'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":9,
              "Original":'I feel anxious'
            },
            **kwargs
        )


class STAISQ10(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['cold', 'troubled','dissatisfied'], 
                                 ['comfortable','relaxed', 'pleasant'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":10,
              "Original":'I feel comfortable'
            },
            **kwargs
        )

class STAISQ11(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['insecure', 'unsure'], 
                                 ['self-confident','self-assured', 'self-reliant'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":11,
              "Original":'I feel self-confident'
            },
            **kwargs
        )


class STAISQ12(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['nervous', 'annoyed', 'edgy'], 
                                 ['easygoing','calm', 'composed'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":12,
              "Original":'I feel nervous'
            },
            **kwargs
        )


class STAISQ13(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['jittery', 'restless'], 
                                 ['calm', 'quiet', 'relaxed'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":13,
              "Original":'I am jittery'
            },
            **kwargs
        )


class STAISQ14(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['high-strung', 'excitable', 'nervous'], 
                                 ['calm', 'relaxed', 'composed'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":14,
              "Original":'I feel “high-strung”'
            },
            **kwargs
        )

class STAISQ18(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['overexcited', 'rattled', 'agitated', 'unsettled'], 
                                 ['calm', 'relaxed', 'steady', 'composed'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":18,
              "Original":'I feel overexcited and rattled'
            },
            **kwargs
        )


class STAISQ19(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['depressed', 'down', 'upset'], 
                                 ['joyful', 'happy', 'cheerful'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":19,
              "Original":'I feel joyful'
            },
            **kwargs
        )


class STAISQ20(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":likert_weights,
            "question":dict_pos_neg(['off', 'terrible', 'bad'], 
                                 ['fine', 'good', 'well'],1.0),
            },
            descriptor = {"Questionnair":"STAI-S",
              "Factor":"Q",
              "Ordinal":20,
              "Original":'I feel fine'
            },
            **kwargs
        )


stai_s_qclm = [STAISQ1s, STAISQ2s, STAISQ3s, STAISQ4s, STAISQ5s, STAISQ6s, STAISQ7s, STAISQ8s, STAISQ9s, STAISQ10s, STAISQ11s, STAISQ12s, STAISQ13s, STAISQ14s, STAISQ18s, STAISQ19s, STAISQ20s]
stai_s_qclm_list = stai_s_qclm