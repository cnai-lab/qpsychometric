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

agreement_weights: SCALE = {
    'strongly disagree': -2,
    'disagree': -1,
    'agree': 1,
    'strongly agree': 2,
}

# Disengagement

class CSQ1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel {question} when people cry in front of you? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["moved", "touched", "emotional"],
                    ["nothing", "numb", "detached"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Disengagement",
                        "Ordinal": 1,
                        "Original": "When people cry in front of me, I often don't feel anything at all."
                        },
            **kwargs,
        )


class CSQ7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} when people tell you about their troubles? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["listen attentively", "stay engaged", "pay attention"],
                    ["tune out", "zone out", "disengage"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Disengagement",
                        "Ordinal": 7,
                        "Original": "I often tune out when people tell me about their troubles."
                        },
            **kwargs,
        )


class CSQ19(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} the concerns of others? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["think about", "consider", "reflect on"],
                    ["ignore", "dismiss", "overlook"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Disengagement",
                        "Ordinal": 19,
                        "Original": "I don't think much about the concerns of others."
                        },
            **kwargs,
        )


class CSQ23(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} people who are experiencing a lot of pain? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["approach", "support", "stay with"],
                    ["avoid", "stay away from", "withdraw from"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Disengagement",
                        "Ordinal": 23,
                        "Original": "I try to avoid people who are experiencing a lot of pain."
                        },
            **kwargs,
        )


# Indifference

class CSQ2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel {question} when people talk about their problems? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["care", "concerned", "involved"],
                    ["indifferent", "uninterested", "detached"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Indifference",
                        "Ordinal": 2,
                        "Original": "Sometimes when people talk about their problems, I feel like I don't care."
                        },
            **kwargs,
        )


class CSQ12(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often are you {question} to others when they are down and out? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["warm", "kind", "compassionate"],
                    ["cold", "harsh", "distant"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Indifference",
                        "Ordinal": 12,
                        "Original": "Sometimes I am cold to others when they are down and out."
                        },
            **kwargs,
        )


class CSQ14(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} other people's problems? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["concern yourself with", "engage with", "attend to"],
                    ["ignore", "dismiss", "disregard"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Indifference",
                        "Ordinal": 14,
                        "Original": "I don't concern myself with other people's problems."
                        },
            **kwargs,
        )


class CSQ18(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} others who are feeling troubled? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["attend to", "help", "support"],
                    ["leave to others", "pass on", "ignore"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Indifference",
                        "Ordinal": 18,
                        "Original": "When others are feeling troubled, I usually let someone else attend to them."
                        },
            **kwargs,
        )


# Separation

class CSQ3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel emotionally {question} people in pain? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["connected to", "close to", "bonded with"],
                    ["disconnected from", "detached from", "distant from"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Separation",
                        "Ordinal": 3,
                        "Original": "I don't feel emotionally connected to people in pain."
                        },
            **kwargs,
        )


class CSQ5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel {question} others when they tell you their tales of woe? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["engaged with", "connected to", "present with"],
                    ["detached from", "distant from", "removed from"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Separation",
                        "Ordinal": 5,
                        "Original": "I feel detached from others when they tell me their tales of woe."
                        },
            **kwargs,
        )


class CSQ10(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel {question} when you see someone feeling down? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["able to relate", "in tune", "connected"],
                    ["unable to relate", "out of touch", "disconnected"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Separation",
                        "Ordinal": 10,
                        "Original": "when I see someone feeling down, I feel like I can't relate to them."
                        },
            **kwargs,
        )


class CSQ22(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you feel {question} with other people when they are suffering? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["able to connect", "in sync", "bonded"],
                    ["unable to connect", "out of sync", "disconnected"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Separation",
                        "Ordinal": 22,
                        "Original": "I can't really connect with other people when they're suffering."
                        },
            **kwargs,
        )


# Mindfulness

class CSQ4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} when other people talk to you? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["pay careful attention", "listen attentively", "focus"],
                    ["ignore them", "tune out", "lose focus"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Mindfulness",
                        "Ordinal": 4,
                        "Original": "I pay careful attention when other people talk to me."
                        },
            **kwargs,
        )


class CSQ9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} when people are upset? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["notice", "perceive", "recognize"],
                    ["miss it", "overlook it", "fail to notice"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Mindfulness",
                        "Ordinal": 9,
                        "Original": "I notice when people are upset, even if they don't say anything."
                        },
            **kwargs,
        )


class CSQ13(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} when people tell you their problems? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["listen patiently", "hear them out", "stay attentive"],
                    ["interrupt", "rush them", "lose patience"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Mindfulness",
                        "Ordinal": 13,
                        "Original": "I tend to listen patiently when people tell me their problems."
                        },
            **kwargs,
        )


class CSQ21(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you keep a {question} perspective when people tell you about their problems? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["balanced", "reasonable", "impartial"],
                    ["biased", "skewed", "unbalanced"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Mindfulness",
                        "Ordinal": 21,
                        "Original": "when people tell me about their problems, I try to keep a balanced perspective on the situation."
                        },
            **kwargs,
        )


# Kindness

class CSQ6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often are you {question} people who are going through a difficult time? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["caring toward", "kind to", "sympathetic toward"],
                    ["indifferent to", "cold to", "uncaring toward"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Kindness",
                        "Ordinal": 6,
                        "Original": "If I see someone going through a difficult time, I try to be caring toward that person."
                        },
            **kwargs,
        )


class CSQ8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} for others in times of difficulty? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["show up", "stand by them", "make yourself available"],
                    ["stay away", "withdraw", "make yourself unavailable"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Kindness",
                        "Ordinal": 8,
                        "Original": "I like to be there for others in times of difficulty."
                        },
            **kwargs,
        )


class CSQ16(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often does your heart {question} people who are unhappy? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["go out to", "reach out to", "feel for"],
                    ["stay closed to", "remain indifferent to", "feel nothing for"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Kindness",
                        "Ordinal": 16,
                        "Original": "My heart goes out to people who are unhappy."
                        },
            **kwargs,
        )


class CSQ24(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: How often do you {question} others when they feel sadness? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(
                    ["comfort", "console", "soothe"],
                    ["ignore", "dismiss", "leave alone"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Kindness",
                        "Ordinal": 24,
                        "Original": "when others feel sadness, I try to comfort them."
                        },
            **kwargs,
        )


# Common Humanity  (agreement-based, not frequency)

class CSQ11(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you agree that feeling down is {question} part of being human? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(
                    ["an important", "an essential", "a significant"],
                    ["an insignificant", "an unimportant", "an irrelevant"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Common Humanity",
                        "Ordinal": 11,
                        "Original": "Everyone feels down sometimes, it is part of being human."
                        },
            **kwargs,
        )


class CSQ15(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you agree that recognizing all people have weaknesses is {question} part of life? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(
                    ["an important", "an essential", "a significant"],
                    ["an insignificant", "an unimportant", "an irrelevant"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Common Humanity",
                        "Ordinal": 15,
                        "Original": "it's important to recognize that all people have weaknesses and no one's perfect."
                        },
            **kwargs,
        )


class CSQ17(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you agree that knowing all people feel pain is {question} part of life? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(
                    ["an important", "an essential", "a significant"],
                    ["an insignificant", "an unimportant", "an irrelevant"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Common Humanity",
                        "Ordinal": 17,
                        "Original": "Despite my differences with others, I know that everyone feels pain just like me."
                        },
            **kwargs,
        )


class CSQ20(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: Do you agree that suffering is {question} part of the common human experience? Answer: {answer}",
            dimensions={
                "answer": agreement_weights,
                "question": dict_pos_neg(
                    ["an important", "an essential", "a significant"],
                    ["an insignificant", "an unimportant", "an irrelevant"], 1.0),
            },
            descriptor={"Questionnair": "CS",
                        "Factor": "Common Humanity",
                        "Ordinal": 20,
                        "Original": "Suffering is just a part of the common human experience."
                        },
            **kwargs,
        )


compassion_scale_qclm_list = [
    CSQ1, CSQ2, CSQ3, CSQ4, CSQ5, CSQ6, CSQ7, CSQ8, CSQ9, CSQ10,
    CSQ11, CSQ12, CSQ13, CSQ14, CSQ15, CSQ16, CSQ17, CSQ18, CSQ19, CSQ20,
    CSQ21, CSQ22, CSQ23, CSQ24,
]