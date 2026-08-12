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

class SOCQ4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you have the feeling that you are {question} what goes on around you? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(["concerned about", "curious about", "interested in"], 
                                ["indifferent to", "don’t really care", "apathetic to"],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Meaningfulness",
                        "Ordinal":4,
                        "Original":"Do you have the feeling that you don’t really care what goes on around you? "
            },
            **kwargs,
        )
        
        


class SOCQ5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(        
            template="Question: How often you are {question} the behavior of people? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(["anticipating", "expecting", 'predicting'], 
                                ['surprise by','stun by', 'shocked by'],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Comprehensibility",
                        "Ordinal":5,
                        "Original":"Has it happened in the past that you were surprised by the behavior of people whom you thought you knew well? "
            },
            **kwargs,
        )
        
        


class SOCQ6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(        
            template="Question: How often has it happened that people whom you counted on {question} you? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(["supported", "helped" , 'backed'], 
                                ["disappointed", 'failed'],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Manageability",
                        "Ordinal":6,
                        "Original":"Has it happened that people whom you counted on disappointed you? "
            },
            **kwargs,
        )
        
        


class SOCQ8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you think your life has {question} goals and purposes? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(["clear", "definite", 'precise'], 
                                ["vague", "uncertain", "unclear"],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Meaningfulness",
                        "Ordinal":8,
                        "Original":"Until now your life has had:"
            },
            **kwargs,
        )
        


class SOCQ9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(        
            template="Question: How often do you have the feeling that you are being treated {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(["justly", "properly"], 
                                [ "unjustly", "with discrimination"],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Manageability",
                        "Ordinal":9,
                        "Original":"Do you have the feeling that you’re being treated unfairly?"
            },
            **kwargs,
        )


class SOCQ12(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often when you are in an unfamiliar situation do you feel {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg([ "comfortable", 'known'], 
                                ["helpless", "hopeless", 'powerless'],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Comprehensibility",
                        "Ordinal":12,
                        "Original":"Do you have the feeling that you’re in an unfamiliar situation and don’t know what to do?"
            },
            **kwargs,
        )
        


class SOCQ16(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel that your daily routine brings you {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(["pleasure", "satisfaction", 'fulfillment'], 
                                ["pain", 'agony', 'sadness'],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Meaningfulness",
                        "Ordinal":16,
                        "Original":"Doing the things you do every day is:"
            },
            **kwargs,
        )
        
        


class SOCQ19(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you have very {question} feelings and ideas? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(["clear", "coherent"], 
                                ["mixed-up", "confounded"],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Comprehensibility",
                        "Ordinal":19,
                        "Original":"Do you have very mixed-up feelings and ideas?"
            },
            **kwargs,
        )
        


class SOCQ21(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often does it happen that you have feelings inside you would like to {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(['face', 'confront'],#, 'acknowledge', 'process', 'accept'], 
                                ['ignore', 'avoid', 'dismiss'],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Comprehensibility",
                        "Ordinal":21,
                        "Original":"Does it happen that you have feelings inside you would rather not feel?"
            },
            **kwargs,
        )
        
        


class SOCQ25(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel you are a {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(["winner", "success"], 
                                ["loser", "failure", 'disappointment'],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Manageability",
                        "Ordinal":25,
                        "Original":"Many people—even those with a strong character—sometimes feel like sad sacks (losers) in certain situations. How often have you felt this way in the past? "
            },
            **kwargs,
        )
        
        


class SOCQ26(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} the importance of things that happen? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(["estimate in proportion", "judge in proportion"], 
                                ["overestimate","misjudge",'underestimate'],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Comprehensibility",
                        "Ordinal":26,
                        "Original":"When something happened‚ you have generally found that: you overestimated or underestimated its importance, you saw things in the right proportion"
            },
            **kwargs,
        )
        


class SOCQ28(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel that the things you do in your daily life are {question}? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg([ "interesting", 'fascinating'], 
                                ["dull", "aimless", 'boring'],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Meaningfulness",
                        "Ordinal":28,
                        "Original":"How often do you have the feeling that there’s little meaning in the things you do in your daily life? "
            },
            **kwargs,
        )
        


class SOCQ29(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you have feelings that are {question} you? Answer: {answer}",
            dimensions={
            "answer":frequency_weights,
            "question":dict_pos_neg(["contained", "collected", 'controlled'], 
                                ["out of control", "uncontrollable", 'unmanageable'],1.0),
            },
            # scale = "answer",
            descriptor = {"Questionnair":"SOC",
                        "Factor":"Manageability",
                        "Ordinal":29,
                        "Original":"How often do you have feelings that you’re not sure you can keep under control? "
            },
            **kwargs,
        )
        
        
soc_qclm_list = [SOCQ4, SOCQ5, SOCQ6, SOCQ8, SOCQ9, SOCQ12, SOCQ16, SOCQ19, SOCQ21, SOCQ25, SOCQ26, SOCQ28, SOCQ29]