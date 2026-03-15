from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg

agreement_weights: SCALE = {
    "strongly disagree": -2,
    "disagree": -1,
    "agree": 1,
    "strongly agree": 2
}


class STCITQ1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['gloomy', 'glum', 'downcast'],
                                         ['bright', 'upbeat', 'cheerful'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-BM",
                        "Ordinal": 1,
                        "Original": "I feel gloomy."},
            **kwargs
        )


class STCITQ2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, are you {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['carefree', 'unfocused', 'lighthearted'],
                                         ['set for serious things', 'focused', 'earnest'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-SE",
                        "Ordinal": 2,
                        "Original": "I am set for serious things."},
            **kwargs
        )


class STCITQ3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['sullen', 'gloomy', 'cheerless'],
                                         ['cheerful', 'bright', 'upbeat'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-CH",
                        "Ordinal": 3,
                        "Original": "I am cheerful."},
            **kwargs
        )


class STCITQ4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you have {question} on your mind? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['nothing of concern', 'trivial matters', 'nothing pressing'],
                                         ['important things', 'significant concerns', 'pressing matters'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-SE",
                        "Ordinal": 4,
                        "Original": "I have important things on my mind."},
            **kwargs
        )


class STCITQ5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, are you in a {question} mood? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['crabby', 'cranky', 'grumpy'],
                                         ['pleasant', 'good-humored', 'amiable'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-BM",
                        "Ordinal": 5,
                        "Original": "I am in a crabby mood."},
            **kwargs
        )


class STCITQ6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['sad', 'sorrowful', 'melancholy'],
                                         ['happy', 'content', 'joyful'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-BM",
                        "Ordinal": 6,
                        "Original": "I am sad."},
            **kwargs
        )


class STCITQ7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, are you {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['reluctant to have fun', 'unenthusiastic', 'unwilling to play'],
                                         ['ready to have fun', 'playful', 'lighthearted'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-CH",
                        "Ordinal": 7,
                        "Original": "I am ready to have some fun."},
            **kwargs
        )


class STCITQ8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you have a {question} mental attitude? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['lighthearted', 'playful', 'unserious'],
                                         ['serious', 'earnest', 'solemn'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-SE",
                        "Ordinal": 8,
                        "Original": "I have a serious mental attitude."},
            **kwargs
        )


class STCITQ9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, are you {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['humorless', 'serious', 'unresponsive to humor'],
                                         ['easily amused', 'quick to laugh', 'ready to find humor'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-CH",
                        "Ordinal": 9,
                        "Original": "I could laugh at the drop of a hat."},
            **kwargs
        )


class STCITQ10(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['peeved', 'irritated', 'annoyed'],
                                         ['content', 'calm', 'unbothered'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-BM",
                        "Ordinal": 10,
                        "Original": "I am peeved."},
            **kwargs
        )


class STCITQ11(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['downcast', 'weighed down', 'heavy-hearted'],
                                         ['elated', 'overjoyed', 'on top of the world'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-CH",
                        "Ordinal": 11,
                        "Original": "I'm walking on air."},
            **kwargs
        )


class STCITQ12(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, are you {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['reactive', 'emotional', 'subjective'],
                                         ['objective', 'sober', 'clear-headed'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-SE",
                        "Ordinal": 12,
                        "Original": "I regard my situation objectively and soberly."},
            **kwargs
        )


class STCITQ13(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['unamused', 'bored', 'indifferent'],
                                         ['amused', 'entertained', 'delighted'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-CH",
                        "Ordinal": 13,
                        "Original": "I am amused."},
            **kwargs
        )


class STCITQ14(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, are you in a {question} frame of mind? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['playful', 'carefree', 'lighthearted'],
                                         ['serious', 'focused', 'grave'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-SE",
                        "Ordinal": 14,
                        "Original": "I am in a serious frame of mind."},
            **kwargs
        )


class STCITQ15(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, are you in a {question} mood? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['impulsive', 'unreflective', 'distracted'],
                                         ['thoughtful', 'reflective', 'pensive'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-SE",
                        "Ordinal": 15,
                        "Original": "I am in a thoughtful mood."},
            **kwargs
        )


class STCITQ16(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['dejected', 'downhearted', 'disheartened'],
                                         ['uplifted', 'encouraged', 'hopeful'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-BM",
                        "Ordinal": 16,
                        "Original": "I feel dejected."},
            **kwargs
        )


class STCITQ17(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['displeased', 'disappointed', 'unimpressed'],
                                         ['delighted', 'pleased', 'thrilled'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-CH",
                        "Ordinal": 17,
                        "Original": "I am delighted."},
            **kwargs
        )


class STCITQ18(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(['grouchy', 'grumpy', 'irritable'],
                                         ['good-natured', 'pleasant', 'even-tempered'], 1.0),
            },
            descriptor={"Questionnair": "STCI-T18",
                        "Factor": "trait-BM",
                        "Ordinal": 18,
                        "Original": "I feel grouchy."},
            **kwargs
        )


stci_t_qclm = [
    STCITQ1, STCITQ2, STCITQ3, STCITQ4, STCITQ5, STCITQ6,
    STCITQ7, STCITQ8, STCITQ9, STCITQ10, STCITQ11, STCITQ12,
    STCITQ13, STCITQ14, STCITQ15, STCITQ16, STCITQ17, STCITQ18,
]
stci_t_qclm_list = stci_t_qclm
