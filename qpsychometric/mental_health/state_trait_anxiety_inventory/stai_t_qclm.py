from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg
# import sys
# sys.path.append("/home/shistikk/IndicatorsOfResilience/code")
# from qlatent.qclm.qclm import *

frequency_weights:SCALE = {
    'never':-4,
    'very rarely':-3,
    'seldom':-2,
    'rarely':-2,
    'frequently':2,
    'often':2,
    'very frequently':3,
    'always':4,    
}

class STAITQ1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['off', 'terrible', 'bad'], 
                                 ['fine', 'good', 'well'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":1,
              "Original":'I feel pleasent'
            },
            # direction = "positive",
            **kwargs
        )


class STAITQ2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['tire quickly', 'fatigue easily', 'get exhausted quickly'], 
                                 ['have steady energy', 'have good stamina'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":2,
              "Original":'I tire quickly'
            },
            # direction = "positive",
            **kwargs
        )
            

class STAITQ3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['like crying', 'tearful', 'overwhelmed with emotion'], 
                                 ['calm', 'steady', 'uplifted'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":3,
              "Original":'I feel like crying'
            },
            # direction = "positive",
            **kwargs
        )
                

class STAITQ4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question} others? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['less happy than', 'not as joyful as'], 
                                 ['as happy as', 'just as cheerful as', 'fully content as'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":4,
              "Original":'I wish I could be as happy as others seem to be'
            },
            # direction = "positive",
            **kwargs
        )
        

class STAITQ5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['indecisive', 'hesitant', 'doubtful'], 
                                 ['determined', 'decisive', 'quick to decide', 'sure-minded'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":5,
              "Original":'I am losing opportunities because I cannot make decisions fast'
            }, 
            # direction = "positive",
            **kwargs
        )
        


class STAITQ6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['fatigued', 'tired', 'wearied'], 
                                    ['rested', 'restored', 'recovered', 'refreshed', 'relaxed'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":6,
              "Original":'I feel rested'
            },
            # direction = "negative",
            **kwargs
        )
        

class STAITQ7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['agitated', 'nervous', 'troubled'],
                                    ['calm', 'peaceful', 'tranquil'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":7,
              "Original":'I am calm'
            },
            # direction = "negative",
            **kwargs
        )

class STAITQ8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel that difficulties are piling up and you can {question} them? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['overwhelmed by', 'unable to manage', 'feel weighed down by'], 
                                 ['overcome','handle', 'cope with', 'manage'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":8,
              "Original":'I feel that difficulties are piling up in such a way that I cannot overcome them'
            },
            # direction = "positive",
            **kwargs
        )

class STAITQ9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question} about thing that do not really matter? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['worried', 'troubled', 'distrubed', 'bothered'], 
                                 ['calm','comforted', 'uncaring', 'relaxed'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":9,
              "Original":'I worry too much about things that do not really matter'
            },
            # direction = "positive",
            **kwargs
        )


class STAITQ10(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['depressed', 'down', 'miserable'], 
                                 ['happy','content','joyful', 'cheerful'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":10,
              "Original":'I am happy'
            },
            # direction = "negative",
            **kwargs
        )

class STAITQ11(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['easily hurt', 'sensitive', 'prone to taking things hard'], 
                                 ['resilient','not easily upset', 'able to take things lightly'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":11,
              "Original":'I am inclined to take things hard'
            },
            # direction = "positive",
            **kwargs
        )

class STAITQ12(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['insecure', 'unsure'], 
                                 ['self-confident','self-assured', 'self-reliant'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":12,
              "Original":'I lack self-confidence'
            },
            # direction = "positive",
            **kwargs
        )

class STAITQ13(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['unsecure', 'unsafe', 'unprotected'], 
                                    ['secure', 'safe', 'protected'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":13,
              "Original":'I feel secure'
            },
            # direction = "negative",
            **kwargs
        )

class STAITQ14(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally {question} difficulties? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['avoid', 'ignore', 'escape'], 
                                 ['face','handle', 'deal with', 'confront'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":14,
              "Original":'I try to avoid facing a crisis or difficulty'
            },
            # direction = "positive",
            **kwargs
        )


class STAITQ15(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['blue', 'sad', 'depressed'], 
                                 ['cheerful','encouraged', 'happy'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":15,
              "Original":'I feel blue'
            },
            # direction = "positive",
            **kwargs
        )


class STAITQ17(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question} unimportant thoughts? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['bothered by', 'distracted by', 'affected by'], 
                                 ['free from','mentally clear from', 'unaffected by'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":17,
              "Original":'Some unimportant thoughts run through my mind and bother me'
            },
            # direction = "positive",
            **kwargs
        )


class STAITQ18(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel about disappointments that you are {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['unable to let them go', 'deeply affected by them', 'stuck thinking about them'], 
                                 ['quick to move on','emotionally resilient'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":18,
              "Original":'I take disappointments so keenly that I cannot get them out of my mind'
            },
            # direction = "positive",
            **kwargs
        )


class STAITQ19(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel you are a {question} person? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['undependable', 'inconsistent', 'unpredictable'], 
                                 ['steady','stable', 'reliable'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":19,
              "Original":'I am a steady person'
            },
            # direction = "negative",
            **kwargs
        )


class STAITQ20(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you generally feel {question} when thinking about current concerns? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['tense', 'upset', 'stressed', 'agitated'], 
                                    ['calm', 'composed', 'unworried'],1.0),
            },
            descriptor = {"Questionnair":"STAI-T",
              "Factor":"Q",
              "Ordinal":20,
              "Original":'I become tense and upset when I think about my current concerns'
            },
            # direction = "positive",
            **kwargs
        )


stai_t_qclm = [STAITQ1, STAITQ2, STAITQ3, STAITQ4, STAITQ5, STAITQ6, STAITQ7, STAITQ8, STAITQ9, STAITQ10, STAITQ11, STAITQ12, STAITQ13, STAITQ14, STAITQ15, STAITQ17, STAITQ18, STAITQ19, STAITQ20]
stai_t_qclm_list = stai_t_qclm