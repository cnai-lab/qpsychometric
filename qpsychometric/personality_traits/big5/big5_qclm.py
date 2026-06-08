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


class BIG5Q1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} new experiences and trying new things? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['open yourself to', 'enjoy'], 
                                ['avoid', 'reject'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Openness",
                        "Ordinal":1,
                        "Original":"I am open to new experiences and enjoy trying new things."
            },
            **kwargs,
        )
        
        
class BIG5Q2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['inventive', 'imaginative'], 
                                ['limited in inner life', 'uncreative'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Openness",
                        "Ordinal":2,
                        "Original":"I am imaginative and have a rich inner life."
            },
            **kwargs,
        )
    
    
class BIG5Q3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} new experiences? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['seek out', 'pursue'], 
                                ['avoid', 'reject'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Openness",
                        "Ordinal":3,
                        "Original":"I am adventurous and seek out new experiences."
            },
            **kwargs,
        )
    
    
class BIG5Q4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} details? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['closely inspect', 'pay attention to', 'focus on'], 
                             ['overlook', 'skip', 'disregard'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Conscientiousness",
                        "Ordinal":4,
                        "Original":"I am thorough and pay attention to detail."
            },
            **kwargs,
        )
       
        
class BIG5Q5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['dependable', 'reliable', 'accountable'], 
                             ['unreliable', 'irresponsible', 'untrustworthy'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Conscientiousness",
                        "Ordinal":5,
                        "Original":"I am responsible and dependable."
            },
            **kwargs,
        )
        
        
class BIG5Q6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often are your things {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['organized', 'neat', 'tidy'], 
                             ['cluttered', 'messy', 'disordered', 'scattered'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Conscientiousness",
                        "Ordinal":6,
                        "Original":"I am organized and like to keep things tidy."
            },
            **kwargs,
        )
        

class BIG5Q7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often are you {question} around other people? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['talkative', 'chatty'], 
                             ['quiet', 'silent'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Extraversion",
                        "Ordinal":7,
                        "Original":"I am talkative and enjoy being around others."
            },
            **kwargs,
        )
      
        
class BIG5Q8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel {question} around people? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['expressive', 'talkative', 'sociable'], 
                             ['quiet', 'shy', 'reserved'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Extraversion",
                        "Ordinal":8,
                        "Original":"I am outgoing and enjoy being the center of attention."
            },
            **kwargs,
        )
        
        
class BIG5Q9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often are you {question} around new people? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg([ 'friendly', 'personable', 'sociable'], 
                             ['silent', 'distant', 'shy'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Extraversion",
                        "Ordinal":9,
                        "Original":"I am sociable and make friends easily."
            },
            **kwargs,
        )
        
        
class BIG5Q10(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often are you {question} other people's feelings? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['considerate of', 'mindful of', 'respectful of'], 
                                ['indifferent to', 'emotionally distant from', 'insensitive to'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Agreeableness",
                        "Ordinal":10,
                        "Original":"I am considerate and care about other people's feelings."
            },
            **kwargs,
        )
    
    
        
class BIG5Q11(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel {question} towards others? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['compassionate', 'empathetic', 'sympathetic'], 
                                ['indifferent', 'careless'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Agreeableness",
                        "Ordinal":11,
                        "Original":"I am compassionate and empathetic towards others."
            },
            **kwargs,
        )
        
        
class BIG5Q12(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often are you {question} while working with others? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['cooperative', 'team-oriented', 'collegial'], 
                                ['non-collaborative', 'disobliging', 'non-contributory'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Agreeableness",
                        "Ordinal":12,
                        "Original":"I am cooperative and work well with others."
            },
            **kwargs,
        )
        
        
class BIG5Q13(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel {question} about things? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['stressed', 'worried', 'distressed'], 
                                ['calm', 'undisturbed', 'composed'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Neuroticism",
                        "Ordinal":13,
                        "Original":"I am easily stressed and worry about things."
            },
            **kwargs,
        )
    
        
class BIG5Q14(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel emotionally {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['distressed', 'upset', 'volatile'], 
                                ['calm', 'composed', 'collected'],1.0),
            },
            descriptor = {"Questionnair":"BIG5",
                        "Factor":"Neuroticism",
                        "Ordinal":14,
                        "Original":"I am easily upset and prone to mood swings."
            },
            **kwargs,
        )
        
big5_qclm_list = [BIG5Q1, BIG5Q2, BIG5Q3, BIG5Q4, BIG5Q5, BIG5Q6, BIG5Q7, BIG5Q8, BIG5Q9, BIG5Q10, BIG5Q11, BIG5Q12, BIG5Q13, BIG5Q14]