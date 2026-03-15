from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg

likert_weights: SCALE = {
    "not at all": -2,
    "somewhat": -1,
    "moderately": 1,
    "very much": 2
}
# likert_weights: SCALE = {
#     "strongly agree" : 2,
#     "agree" : 1,
#     "disagree" : -1,
#     "strongly disagree" : -2
# }

class PANASSQ1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['bored', 'indifferent'],
                                         ['interested', 'curious', 'engaged'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-PA",
                        "Ordinal": 1,
                        "Original": "Interested"},
            **kwargs
        )


class PANASSQ2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['distressed', 'troubled', 'anguished'],
                                         ['calm', 'undisturbed', 'at ease'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-NA",
                        "Ordinal": 2,
                        "Original": "Distressed"},
            **kwargs
        )


class PANASSQ3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['bored', 'unexcited', 'flat'],
                                         ['excited', 'thrilled', 'exhilarated'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-PA",
                        "Ordinal": 3,
                        "Original": "Excited"},
            **kwargs
        )


class PANASSQ4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['upset', 'troubled', 'bothered'],
                                         ['content', 'undisturbed', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-NA",
                        "Ordinal": 4,
                        "Original": "Upset"},
            **kwargs
        )


class PANASSQ5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['weak', 'feeble', 'powerless'],
                                         ['strong', 'powerful', 'capable'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-PA",
                        "Ordinal": 5,
                        "Original": "Strong"},
            **kwargs
        )


class PANASSQ6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['guilty', 'remorseful', 'regretful'],
                                         ['blameless', 'innocent', 'guilt-free'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-NA",
                        "Ordinal": 6,
                        "Original": "Guilty"},
            **kwargs
        )


class PANASSQ7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['scared', 'frightened', 'fearful'],
                                         ['unafraid', 'fearless', 'safe'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-NA",
                        "Ordinal": 7,
                        "Original": "Scared"},
            **kwargs
        )


class PANASSQ8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['hostile', 'antagonistic', 'aggressive'],
                                         ['friendly', 'warm', 'amicable'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-NA",
                        "Ordinal": 8,
                        "Original": "Hostile"},
            **kwargs
        )


class PANASSQ9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['apathetic', 'unenthusiastic', 'indifferent'],
                                         ['enthusiastic', 'eager', 'passionate'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-PA",
                        "Ordinal": 9,
                        "Original": "Enthusiastic"},
            **kwargs
        )


class PANASSQ10(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['ashamed', 'unworthy', 'humiliated'],
                                         ['proud', 'accomplished', 'self-satisfied'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-PA",
                        "Ordinal": 10,
                        "Original": "Proud"},
            **kwargs
        )


class PANASSQ11(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['irritable', 'irritated', 'annoyed'],
                                         ['calm', 'good-natured', 'even-tempered'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-NA",
                        "Ordinal": 11,
                        "Original": "Irritable"},
            **kwargs
        )


class PANASSQ12(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['drowsy', 'inattentive', 'dull'],
                                         ['alert', 'sharp', 'wide-awake'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-PA",
                        "Ordinal": 12,
                        "Original": "Alert"},
            **kwargs
        )


class PANASSQ13(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['ashamed', 'embarrassed', 'humiliated'],
                                         ['dignified', 'unashamed', 'self-respecting'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-NA",
                        "Ordinal": 13,
                        "Original": "Ashamed"},
            **kwargs
        )


class PANASSQ14(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['uninspired', 'unmotivated', 'flat'],
                                         ['inspired', 'motivated', 'uplifted'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-PA",
                        "Ordinal": 14,
                        "Original": "Inspired"},
            **kwargs
        )


class PANASSQ15(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['nervous', 'anxious', 'on edge'],
                                         ['calm', 'relaxed', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-NA",
                        "Ordinal": 15,
                        "Original": "Nervous"},
            **kwargs
        )


class PANASSQ16(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['irresolute', 'aimless', 'undecided'],
                                         ['determined', 'resolute', 'driven'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-PA",
                        "Ordinal": 16,
                        "Original": "Determined"},
            **kwargs
        )


class PANASSQ17(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['inattentive', 'distracted', 'unfocused'],
                                         ['attentive', 'focused', 'mindful'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-PA",
                        "Ordinal": 17,
                        "Original": "Attentive"},
            **kwargs
        )


class PANASSQ18(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['jittery', 'restless', 'edgy'],
                                         ['calm', 'steady', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-NA",
                        "Ordinal": 18,
                        "Original": "Jittery"},
            **kwargs
        )


class PANASSQ19(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['inactive', 'lethargic', 'sluggish'],
                                         ['active', 'energetic', 'lively'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-PA",
                        "Ordinal": 19,
                        "Original": "Active"},
            **kwargs
        )


class PANASSQ20(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['afraid', 'fearful', 'terrified'],
                                         ['unafraid', 'courageous', 'fearless'], 1.0),
            },
            descriptor={"Questionnair": "PANAS-S",
                        "Factor": "state-NA",
                        "Ordinal": 20,
                        "Original": "Afraid"},
            **kwargs
        )


panas_s_qclm = [
    PANASSQ1, PANASSQ2, PANASSQ3, PANASSQ4, PANASSQ5,
    PANASSQ6, PANASSQ7, PANASSQ8, PANASSQ9, PANASSQ10,
    PANASSQ11, PANASSQ12, PANASSQ13, PANASSQ14, PANASSQ15,
    PANASSQ16, PANASSQ17, PANASSQ18, PANASSQ19, PANASSQ20,
]
panas_s_qclm_list = panas_s_qclm
