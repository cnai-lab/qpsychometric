from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg

agreement_weights: SCALE = {
    "strongly disagree": -2,
    "disagree": -1,
    "agree": 1,
    "strongly agree": 2
}


class STCISQ1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['gloomy', 'glum', 'downcast'],
                                         ['bright', 'upbeat', 'cheerful'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-BM",
                        "Ordinal": 1,
                        "Original": "I feel gloomy."},
            **kwargs
        )


class STCISQ2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, are you {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['carefree', 'unfocused', 'lighthearted'],
                                         ['set for serious things', 'focused', 'earnest'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-SE",
                        "Ordinal": 2,
                        "Original": "I am set for serious things."},
            **kwargs
        )


class STCISQ3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['sullen', 'gloomy', 'cheerless'],
                                         ['cheerful', 'bright', 'upbeat'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-CH",
                        "Ordinal": 3,
                        "Original": "I am cheerful."},
            **kwargs
        )


class STCISQ4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you have {question} on your mind? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['nothing of concern', 'trivial matters', 'nothing pressing'],
                                         ['important things', 'significant concerns', 'pressing matters'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-SE",
                        "Ordinal": 4,
                        "Original": "I have important things on my mind."},
            **kwargs
        )


class STCISQ5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, are you in a {question} mood? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['crabby', 'cranky', 'grumpy'],
                                         ['pleasant', 'good-humored', 'amiable'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-BM",
                        "Ordinal": 5,
                        "Original": "I am in a crabby mood."},
            **kwargs
        )


class STCISQ6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['sad', 'sorrowful', 'melancholy'],
                                         ['happy', 'content', 'joyful'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-BM",
                        "Ordinal": 6,
                        "Original": "I am sad."},
            **kwargs
        )


class STCISQ7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, are you {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['reluctant to have fun', 'unenthusiastic', 'unwilling to play'],
                                         ['ready to have fun', 'playful', 'lighthearted'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-CH",
                        "Ordinal": 7,
                        "Original": "I am ready to have some fun."},
            **kwargs
        )


class STCISQ8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you have a {question} mental attitude? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['lighthearted', 'playful', 'unserious'],
                                         ['serious', 'earnest', 'solemn'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-SE",
                        "Ordinal": 8,
                        "Original": "I have a serious mental attitude."},
            **kwargs
        )


class STCISQ9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, are you {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['humorless', 'serious', 'unresponsive to humor'],
                                         ['easily amused', 'quick to laugh', 'ready to find humor'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-CH",
                        "Ordinal": 9,
                        "Original": "I could laugh at the drop of a hat."},
            **kwargs
        )


class STCISQ10(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['peeved', 'irritated', 'annoyed'],
                                         ['content', 'calm', 'unbothered'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-BM",
                        "Ordinal": 10,
                        "Original": "I am peeved."},
            **kwargs
        )


class STCISQ11(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['downcast', 'weighed down', 'heavy-hearted'],
                                         ['elated', 'overjoyed', 'on top of the world'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-CH",
                        "Ordinal": 11,
                        "Original": "I'm walking on air."},
            **kwargs
        )


class STCISQ12(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, are you {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['reactive', 'emotional', 'subjective'],
                                         ['objective', 'sober', 'clear-headed'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-SE",
                        "Ordinal": 12,
                        "Original": "I regard my situation objectively and soberly."},
            **kwargs
        )


class STCISQ13(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['unamused', 'bored', 'indifferent'],
                                         ['amused', 'entertained', 'delighted'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-CH",
                        "Ordinal": 13,
                        "Original": "I am amused."},
            **kwargs
        )


class STCISQ14(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, are you in a {question} frame of mind? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['playful', 'carefree', 'lighthearted'],
                                         ['serious', 'focused', 'grave'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-SE",
                        "Ordinal": 14,
                        "Original": "I am in a serious frame of mind."},
            **kwargs
        )


class STCISQ15(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, are you in a {question} mood? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['impulsive', 'unreflective', 'distracted'],
                                         ['thoughtful', 'reflective', 'pensive'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-SE",
                        "Ordinal": 15,
                        "Original": "I am in a thoughtful mood."},
            **kwargs
        )


class STCISQ16(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['dejected', 'downhearted', 'disheartened'],
                                         ['uplifted', 'encouraged', 'hopeful'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-BM",
                        "Ordinal": 16,
                        "Original": "I feel dejected."},
            **kwargs
        )


class STCISQ17(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['displeased', 'disappointed', 'unimpressed'],
                                         ['delighted', 'pleased', 'thrilled'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-CH",
                        "Ordinal": 17,
                        "Original": "I am delighted."},
            **kwargs
        )


class STCISQ18(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['grouchy', 'grumpy', 'irritable'],
                                         ['good-natured', 'pleasant', 'even-tempered'], 1.0),
            },
            descriptor={"Questionnair": "STCI-S18",
                        "Factor": "state-BM",
                        "Ordinal": 18,
                        "Original": "I feel grouchy."},
            **kwargs
        )


stci_s_qclm = [
    STCISQ1, STCISQ2, STCISQ3, STCISQ4, STCISQ5, STCISQ6,
    STCISQ7, STCISQ8, STCISQ9, STCISQ10, STCISQ11, STCISQ12,
    STCISQ13, STCISQ14, STCISQ15, STCISQ16, STCISQ17, STCISQ18,
]
stci_s_qclm_list = stci_s_qclm
