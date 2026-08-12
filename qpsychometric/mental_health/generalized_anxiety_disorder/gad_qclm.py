from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg

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

class GAD7Q1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been feeling {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['nervous', 'anxious','agitated'], 
                                 ['peaceful','in control', 'relaxed'],1.0),
            },
            # scale = 'answer',
            descriptor = {"Questionnair":"GAD7",
              "Factor":"Q",
              "Ordinal":1,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Feeling nervous, anxious or on edge'
            },
            **kwargs
        )



class GAD7Q2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been feeling {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['worried', 'troubled', 'disturbed'], 
                                 ['peaceful','in control', 'relaxed'],1.0),
            },
            # scale = 'answer',
            descriptor = {"Questionnair":"GAD7",
              "Factor":"Q",
              "Ordinal":2,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Not being able to stop or control worrying'
            },
            **kwargs
        )
        
        


class GAD7Q3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been feeling {question} about different things? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['worried', 'stressed', 'nervous'], 
                                 ['confident', 'tranquil', 'relaxed'],1.0),
            },
            # scale = 'answer',
            descriptor = {"Questionnair":"GAD7",
              "Factor":"Q",
              "Ordinal":3,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Worrying too much about different things'
            },
            **kwargs
        )
        
        


class GAD7Q4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been having {question} relaxing? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['trouble', 'difficulty'], 
                                 ['no problem', 'an easy time'],1.0),
            },
            # scale = 'answer',
            descriptor = {"Questionnair":"GAD7",
              "Factor":"Q",
              "Ordinal":4,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Trouble relaxing'
            },
            **kwargs
        )
        

class GAD7Q5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['restless', 'agitated', 'nervous'], 
                                 ['calm', 'tranquil', 'relaxed'],1.0),
            },
            # scale = 'answer',
            descriptor = {"Questionnair":"GAD7",
              "Factor":"Q",
              "Ordinal":5,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Being so restless that it is hard to sit still'
            },
            **kwargs
        )
        


class GAD7Q6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been feeling {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['annoyed', 'irritated', 'frustrated', 'bothered'], 
                                 ['calm', 'tranquil', 'peaceful', 'relaxed'],1.0),
            },
            # scale = 'answer',
            descriptor = {"Questionnair":"GAD7",
              "Factor":"Q",
              "Ordinal":6,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Becoming easily annoyed or irritable'
            },
            **kwargs
        )
        

class GAD7Q7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been feeling {question} about upcoming events? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['afraid', 'scared', 'anxious'], 
                                 ['calm', 'relaxed'],1.0),
            },
            # scale = 'answer',
            descriptor = {"Questionnair":"GAD7",
              "Factor":"Q",
              "Ordinal":7,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Feeling afraid as if something awful might happen'
            },
            **kwargs
        )
        
gad7_qclm = [GAD7Q1, GAD7Q2, GAD7Q3, GAD7Q4, GAD7Q5, GAD7Q6, GAD7Q7]
gad_qclm_list = gad7_qclm