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


class PHQ9Q1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been bothered by feeling {question} when doing things? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['unsatisfied', 'down'], 
                                 ['interest', 'pleasure',],1.0),
            },
            scale = "answer",
            descriptor = {"Questionnair":"PHQ9",
              "Factor":"Q",
              "Ordinal":1,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Little interest or pleasure in doing things'
            },
            **kwargs
        )
        


class PHQ9Q2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been feeling {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['depressed', 'down', 'hopeless'], 
                                    ['hopeful', 'cheerful', 'up'],1.0),
            },
            scale = "answer",
            descriptor = {"Questionnair":"PHQ9",
              "Factor":"Q",
              "Ordinal":2,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Feeling down, depressed or hopeless'
            },
            **kwargs
        )
        


class PHQ9Q3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often you had {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['trouble falling asleep', 'trouble staying asleep'], 
                                    ['been resting well', 'been sleeping well'],1.0),
            },
            scale = "answer",
            descriptor = {"Questionnair":"PHQ9",
              "Factor":"Q",
              "Ordinal":3,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Trouble falling asleep, staying asleep, or sleeping too much'
            },
            **kwargs
        )
        
        
class PHQ9Q4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been feeling {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['tired', 'drained', 'fatigued'], 
                                    ['energized', 'refreshed', 'lively'],1.0),
            },
            scale = "answer",
            descriptor = {"Questionnair":"PHQ9",
              "Factor":"Q",
              "Ordinal":4,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Feeling tired or having little energy'
            },
            **kwargs
        )
        
        


class PHQ9Q5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often you had {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['poor appetite', 'been overeating'], 
                                    ['healthy appetite', 'satisfying appetite'],1.0),
            },
            scale = "answer",
            descriptor = {"Questionnair":"PHQ9",
              "Factor":"Q",
              "Ordinal":5,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Poor appetite or overeating'
            },
            **kwargs
        )



class PHQ9Q6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been feeling {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['a failure', 'underachievment', 'I let myself down', 'I let my family down'], 
                                    ['successful ', 'lucky', 'confident'],1.0),
            },
            scale = "answer",
            descriptor = {"Questionnair":"PHQ9",
              "Factor":"Q",
              "Ordinal":6,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Feeling bad about yourself - or that you’re a failure or have let yourself or your family down'
            },
            **kwargs
        )
        
    

class PHQ9Q7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often you {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['had trouble concentrating', 'had difficulty focusing'], 
                                    ['concentrated easily', 'focused effortlessly'],1.0),
            },
            scale = "answer",
            descriptor = {"Questionnair":"PHQ9",
              "Factor":"Q",
              "Ordinal":7,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Trouble concentrating on things, such as reading the newspaper or watching television'
            },
            **kwargs
        )
        
        


class PHQ9Q8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often have you been moving or speaking {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['fidgetly', 'slowly'], 
                                    ['normally', 'naturally'],1.0),
            },
            scale = "answer",
            descriptor = {"Questionnair":"PHQ9",
              "Factor":"Q",
              "Ordinal":8,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Moving or speaking so slowly that other people could have noticed. Or, the opposite - being so fidgety or restless that you have been moving around a lot more than usual'
            },
            **kwargs
        )
        


class PHQ9Q9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Over the last 2 weeks, how often you have been having {question} thoughts? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['suicidal', 'self destructive', 'deadly'], 
                                    ['harmless', 'hopeful', 'positive'],1.0),
            },
            scale = "answer",
            descriptor = {"Questionnair":"PHQ9",
              "Factor":"Q",
              "Ordinal":9,
              "Original":'Over the last 2 weeks, how often have you been bothered by the following problems? Thoughts that you would be better off dead or of hurting yourself in some way'
            },
            **kwargs
        )
        
        
phq_qclm_list = [PHQ9Q1, PHQ9Q2, PHQ9Q3, PHQ9Q4, PHQ9Q5, PHQ9Q6, PHQ9Q7, PHQ9Q8, PHQ9Q9]