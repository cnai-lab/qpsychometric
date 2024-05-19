from qlatent.qmnli.qmnli import _QMNLI, SCALE

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

class PHQ9Q1(_QMNLI):
    def __init__(self, **kwargs):
        super().__init__(
            context="Over the last 2 weeks, I had {emotion} in doing things.",
            template="It is {intensifier} correct.",
            emo_pos=['little interest', 'no pleasure', 'displeasure', 'dissatisfaction'],
            emo_neg=['pleasure', 'satisfaction'],
            intensifiers=frequency_weights,
            descriptor = {"Questionnair":"PHQ9",
              "Factor":"PHQ",
              "Ordinal":1,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Little interest or pleasure in doing things'
            },
            **kwargs
        )
        
        
class PHQ9Q2(_QMNLI):
    def __init__(self, **kwargs ):
        super().__init__(
            context="Over the last 2 weeks, I have been feeling {emotion}.",
            template="It is {intensifier} correct.",
            emo_pos=['down', 'depressed', 'hopeless'],
            emo_neg=['happy', 'hopeful', 'cheerful'],
            intensifiers=frequency_weights,
            descriptor = {"Questionnair":"PHQ9",
              "Factor":"PHQ",
              "Ordinal":2,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Feeling down, depressed or hopeless'
            },
            **kwargs
        )
        
phq2_qmnli = [PHQ9Q1, PHQ9Q2]
