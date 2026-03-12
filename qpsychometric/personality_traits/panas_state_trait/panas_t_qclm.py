from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg

frequency_weights: SCALE = {
    'never': -4,
    'very rarely': -3,
    'seldom': -2,
    'rarely': -2,
    'frequently': 2,
    'often': 2,
    'very frequently': 3,
    'always': 4,
}


class PANASTQ1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['bored', 'disengaged'],
                                         ['interested', 'engaged'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "PA",
                        "Ordinal": 1,
                        "Original": "Interested"},
            **kwargs
        )


class PANASTQ2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['distressed', 'troubled', 'anguished'],
                                         ['calm', 'undisturbed', 'at ease'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "NA",
                        "Ordinal": 2,
                        "Original": "Distressed"},
            **kwargs
        )

#unexcited
class PANASTQ3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['flat', 'indifferent', 'apathetic'],
                                         ['excited', 'exhilarated', 'enthusiastic'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "PA",
                        "Ordinal": 3,
                        "Original": "Excited"},
            **kwargs
        )


class PANASTQ4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['upset', 'troubled', 'bothered'],
                                         ['content', 'undisturbed', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "NA",
                        "Ordinal": 4,
                        "Original": "Upset"},
            **kwargs
        )

#feeble
#powerless
class PANASTQ5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['weak', 'fragile', 'exhausted'],
                                         ['strong', 'powerful', 'capable'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "PA",
                        "Ordinal": 5,
                        "Original": "Strong"},
            **kwargs
        )

#innocent
class PANASTQ6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['guilty', 'convicted'],
                                         ['blameless', 'guilt-free'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "NA",
                        "Ordinal": 6,
                        "Original": "Guilty"},
            **kwargs
        )


class PANASTQ7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['scared', 'frightened', 'fearful'],
                                         ['unafraid', 'fearless', 'safe'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "NA",
                        "Ordinal": 7,
                        "Original": "Scared"},
            **kwargs
        )


class PANASTQ8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['hostile', 'aggressive'],
                                         ['friendly', 'amicable'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "NA",
                        "Ordinal": 8,
                        "Original": "Hostile"},
            **kwargs
        )

#apathetic
class PANASTQ9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['unenthusiastic', 'indifferent', 'disinterested'],
                                         ['enthusiastic', 'eager', 'passionate', 'excited'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "PA",
                        "Ordinal": 9,
                        "Original": "Enthusiastic"},
            **kwargs
        )


class PANASTQ10(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['ashamed', 'unworthy', 'humiliated'],
                                         ['proud', 'accomplished', 'self-satisfied'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "PA",
                        "Ordinal": 10,
                        "Original": "Proud"},
            **kwargs
        )


class PANASTQ11(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['irritable', 'irritated', 'annoyed'],
                                         ['calm', 'good-natured', 'even-tempered'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "NA",
                        "Ordinal": 11,
                        "Original": "Irritable"},
            **kwargs
        )


class PANASTQ12(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['drowsy', 'tired', 'fatigued'],
                                         ['alert', 'attentive', 'sharp', 'aware'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "PA",
                        "Ordinal": 12,
                        "Original": "Alert"},
            **kwargs
        )


class PANASTQ13(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['ashamed', 'embarrassed', 'humiliated'],
                                         ['dignified', 'unashamed', 'self-respecting'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "NA",
                        "Ordinal": 13,
                        "Original": "Ashamed"},
            **kwargs
        )


class PANASTQ14(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['uninspired', 'unmotivated'],
                                         ['inspired', 'motivated'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "PA",
                        "Ordinal": 14,
                        "Original": "Inspired"},
            **kwargs
        )


class PANASTQ15(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['nervous', 'anxious', 'on edge'],
                                         ['calm', 'relaxed', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "NA",
                        "Ordinal": 15,
                        "Original": "Nervous"},
            **kwargs
        )

#resolute
#undecided
class PANASTQ16(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['irresolute', 'aimless'],
                                         ['determined', 'driven'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "PA",
                        "Ordinal": 16,
                        "Original": "Determined"},
            **kwargs
        )


class PANASTQ17(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['distracted', 'unfocused'],
                                         ['attentive', 'focused', 'mindful'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "PA",
                        "Ordinal": 17,
                        "Original": "Attentive"},
            **kwargs
        )


class PANASTQ18(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['jittery', 'restless', 'edgy'],
                                         ['calm', 'steady', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "NA",
                        "Ordinal": 18,
                        "Original": "Jittery"},
            **kwargs
        )

#lively
#sluggish
class PANASTQ19(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['lethargic', 'tired'],
                                         ['active', 'engaged', 'productive'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "PA",
                        "Ordinal": 19,
                        "Original": "Active"},
            **kwargs
        )


class PANASTQ20(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, on the average, how often do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['afraid', 'fearful', 'terrified'],
                                         ['unafraid', 'courageous', 'fearless'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-T",
                        "Factor": "NA",
                        "Ordinal": 20,
                        "Original": "Afraid"},
            **kwargs
        )


panas_t_qclm = [
    PANASTQ1, PANASTQ2, PANASTQ3, PANASTQ4, PANASTQ5,
    PANASTQ6, PANASTQ7, PANASTQ8, PANASTQ9, PANASTQ10,
    PANASTQ11, PANASTQ12, PANASTQ13, PANASTQ14, PANASTQ15,
    PANASTQ16, PANASTQ17, PANASTQ18, PANASTQ19, PANASTQ20,
]
panas_t_qclm_list = panas_t_qclm
