from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg

likert_weights: SCALE = {
    "not at all": -2,
    "somewhat": -1,
    "moderately": 1,
    "very much": 2
}

frequency_weights: SCALE = {
    'almost never': -2,
    'sometimes': -1,
    'often': 1,
    'almost always': 2,
}


# ── Part 1: State Anger (How I Feel Right Now) ──────────────────────────────

class STAXI2Q1(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['furious', 'enraged', 'livid'],
                                         ['calm', 'composed', 'serene'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 1,
                        "Original": "I am furious"},
            **kwargs
        )


class STAXI2Q2(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['irritated', 'annoyed', 'aggravated'],
                                         ['calm', 'unbothered', 'at ease'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 2,
                        "Original": "I feel irritated"},
            **kwargs
        )


class STAXI2Q3(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['angry', 'mad', 'wrathful'],
                                         ['calm', 'peaceful', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 3,
                        "Original": "I feel angry"},
            **kwargs
        )


class STAXI2Q4(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['like yelling at someone', 'like screaming at somebody', 'like shouting at someone'],
                                         ['like speaking calmly', 'composed and restrained', 'calm'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 4,
                        "Original": "I feel like yelling at somebody"},
            **kwargs
        )


class STAXI2Q5(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['like breaking things', 'like smashing something', 'destructive'],
                                         ['calm and controlled', 'composed', 'in control'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 5,
                        "Original": "I feel like breaking things"},
            **kwargs
        )


class STAXI2Q6(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['mad', 'furious', 'enraged'],
                                         ['calm', 'even-tempered', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 6,
                        "Original": "I am mad"},
            **kwargs
        )


class STAXI2Q7(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['like banging on the table', 'like hitting something', 'physically agitated'],
                                         ['calm', 'composed', 'physically controlled'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 7,
                        "Original": "I feel like banging on the table"},
            **kwargs
        )


class STAXI2Q8(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['like hitting someone', 'like striking someone', 'physically aggressive'],
                                         ['calm', 'non-violent', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 8,
                        "Original": "I feel like hitting someone"},
            **kwargs
        )


class STAXI2Q9(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['like swearing', 'like cursing', 'like using profanity'],
                                         ['calm', 'restrained', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 9,
                        "Original": "I feel like swearing"},
            **kwargs
        )


class STAXI2Q10(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['annoyed', 'aggravated', 'irritated'],
                                         ['unbothered', 'patient', 'at ease'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 10,
                        "Original": "I feel annoyed"},
            **kwargs
        )


class STAXI2Q11(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['like kicking somebody', 'like striking out at someone', 'like attacking someone'],
                                         ['calm', 'peaceful', 'non-aggressive'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 11,
                        "Original": "I feel like kicking somebody"},
            **kwargs
        )


class STAXI2Q12(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['like cursing out loud', 'like shouting profanity', 'verbally explosive'],
                                         ['calm', 'controlled', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 12,
                        "Original": "I feel like cursing out loud"},
            **kwargs
        )


class STAXI2Q13(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['like screaming', 'like yelling out', 'overwhelmed with rage'],
                                         ['calm', 'quiet', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 13,
                        "Original": "I feel like screaming"},
            **kwargs
        )


class STAXI2Q14(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['like pounding somebody', 'like physically attacking someone', 'violently aggressive'],
                                         ['calm', 'non-violent', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 14,
                        "Original": "I feel like pounding somebody"},
            **kwargs
        )


class STAXI2Q15(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: At this moment, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['like shouting out loud', 'like yelling loudly', 'like exploding verbally'],
                                         ['calm', 'quiet', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "state-anger",
                        "Ordinal": 15,
                        "Original": "I feel like shouting out loud"},
            **kwargs
        )


# ── Part 2: Trait Anger (How I Generally Feel) ───────────────────────────────

class STAXI2Q16(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, are you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['quick-tempered', 'short-fused', 'easily angered'],
                                         ['even-tempered', 'patient', 'slow to anger'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "trait-anger",
                        "Ordinal": 16,
                        "Original": "I am quick tempered"},
            **kwargs
        )


class STAXI2Q17(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you have a {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['fiery temper', 'hot temper', 'volatile temperament'],
                                         ['calm temper', 'mild-mannered temperament', 'even temperament'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "trait-anger",
                        "Ordinal": 17,
                        "Original": "I have a fiery temper"},
            **kwargs
        )


class STAXI2Q18(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, are you a {question} person? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['hotheaded', 'hot-tempered', 'impulsive'],
                                         ['cool-headed', 'level-headed', 'calm'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "trait-anger",
                        "Ordinal": 18,
                        "Original": "I am a hotheaded person"},
            **kwargs
        )


class STAXI2Q19(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question} when slowed down by others' mistakes? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['angry', 'frustrated', 'furious'],
                                         ['patient', 'tolerant', 'understanding'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "trait-anger",
                        "Ordinal": 19,
                        "Original": "I get angry when I'm slowed down by others' mistakes"},
            **kwargs
        )


class STAXI2Q20(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question} when not given recognition for doing good work? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['annoyed', 'resentful', 'bitter'],
                                         ['unbothered', 'indifferent', 'at ease'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "trait-anger",
                        "Ordinal": 20,
                        "Original": "I feel annoyed when I am not given recognition for doing good work"},
            **kwargs
        )


class STAXI2Q21(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['fly off the handle', 'lose your temper suddenly', 'explode in anger'],
                                         ['keep your cool', 'stay calm', 'remain composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "trait-anger",
                        "Ordinal": 21,
                        "Original": "I fly off the handle"},
            **kwargs
        )


class STAXI2Q22(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, when you get mad, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['say nasty things', 'say hurtful things', 'lash out verbally'],
                                         ['stay composed', 'hold back', 'speak calmly'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "trait-anger",
                        "Ordinal": 22,
                        "Original": "When I get mad, I say nasty things"},
            **kwargs
        )


class STAXI2Q23(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question} when criticized in front of others? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['furious', 'outraged', 'enraged'],
                                         ['calm', 'unbothered', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "trait-anger",
                        "Ordinal": 23,
                        "Original": "It makes me furious when I am criticized in front of others"},
            **kwargs
        )


class STAXI2Q24(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, when frustrated, do you feel {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['like hitting someone', 'violently aggressive', 'physically hostile'],
                                         ['calm', 'non-violent', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "trait-anger",
                        "Ordinal": 24,
                        "Original": "When I get frustrated, I feel like hitting someone"},
            **kwargs
        )


class STAXI2Q25(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: In general, do you feel {question} when you do a good job and receive a poor evaluation? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['infuriated', 'outraged', 'furious'],
                                         ['calm', 'accepting', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "trait-anger",
                        "Ordinal": 25,
                        "Original": "I feel infuriated when I do a good job and get a poor evaluation"},
            **kwargs
        )


# ── Part 3: Anger Expression & Control (How I Generally React When Angry) ────

class STAXI2Q26(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['lose your temper', 'give in to your anger', 'fail to stay controlled'],
                                         ['control your temper', 'keep yourself in check', 'stay composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-out",
                        "Ordinal": 26,
                        "Original": "I control my temper"},
            **kwargs
        )


class STAXI2Q27(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['express your anger outwardly', 'vent your anger', 'let your anger out'],
                                         ['hold back your anger', 'stay composed', 'keep it to yourself'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-out",
                        "Ordinal": 27,
                        "Original": "I express my anger"},
            **kwargs
        )


class STAXI2Q28(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['stay tense', 'remain agitated', 'keep fuming inside'],
                                         ['take a deep breath and relax', 'breathe and calm down', 'compose yourself'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-in",
                        "Ordinal": 28,
                        "Original": "I take a deep breath and relax"},
            **kwargs
        )


class STAXI2Q29(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['keep things in', 'bottle up your feelings', 'internalize your anger'],
                                         ['express what you feel', 'let it out appropriately', 'speak up'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-in",
                        "Ordinal": 29,
                        "Original": "I keep things in"},
            **kwargs
        )


class STAXI2Q30(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, are you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['impatient with others', 'intolerant', 'short with people'],
                                         ['patient with others', 'tolerant', 'understanding'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-out",
                        "Ordinal": 30,
                        "Original": "I am patient with others"},
            **kwargs
        )


class STAXI2Q31(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When someone annoys you, are you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['apt to tell them how angry you feel', 'quick to voice your displeasure', 'likely to confront them'],
                                         ['likely to keep it to yourself', 'quiet about how you feel', 'composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-out",
                        "Ordinal": 31,
                        "Original": "If someone annoys me, I'm apt to tell him or her how I feel"},
            **kwargs
        )


class STAXI2Q32(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['let your anger linger', 'stay upset', 'remain angry'],
                                         ['try to calm yourself as soon as possible', 'work to settle down quickly', 'soothe yourself'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-in",
                        "Ordinal": 32,
                        "Original": "I try to calm myself as soon as possible"},
            **kwargs
        )


class STAXI2Q33(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['pout or sulk', 'brood', 'withdraw sulkily'],
                                         ['stay upbeat', 'bounce back', 'remain engaged'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-in",
                        "Ordinal": 33,
                        "Original": "I pout or sulk"},
            **kwargs
        )


class STAXI2Q34(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['give in to the urge to express your anger', 'act on your anger impulsively', 'lose control'],
                                         ['control your urge to express your anger', 'restrain yourself', 'hold back'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-out",
                        "Ordinal": 34,
                        "Original": "I control my urge to express my angry feelings"},
            **kwargs
        )


class STAXI2Q35(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['lose your temper', 'blow up', 'explode'],
                                         ['keep your cool', 'stay controlled', 'remain composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-out",
                        "Ordinal": 35,
                        "Original": "I lose my temper"},
            **kwargs
        )


class STAXI2Q36(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['stay worked up', 'remain hot-headed', 'keep fuming'],
                                         ['try to simmer down', 'cool off', 'calm yourself'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-in",
                        "Ordinal": 36,
                        "Original": "I try to simmer down"},
            **kwargs
        )


class STAXI2Q37(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['withdraw from people', 'isolate yourself', 'pull away'],
                                         ['stay connected', 'remain engaged with others', 'stay present'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-in",
                        "Ordinal": 37,
                        "Original": "I withdraw from people"},
            **kwargs
        )


class STAXI2Q38(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['lose your cool', 'get heated', 'fail to stay calm'],
                                         ['keep your cool', 'stay composed', 'remain collected'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-out",
                        "Ordinal": 38,
                        "Original": "I keep my cool"},
            **kwargs
        )


class STAXI2Q39(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['make sarcastic remarks to others', 'say cutting things', 'be verbally aggressive'],
                                         ['stay respectful', 'speak kindly', 'hold back criticism'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-out",
                        "Ordinal": 39,
                        "Original": "I make sarcastic remarks to others"},
            **kwargs
        )


class STAXI2Q40(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['let your anger grow', 'feed your anger', 'stay agitated'],
                                         ['try to soothe your angry feelings', 'calm your inner anger', 'settle yourself'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-in",
                        "Ordinal": 40,
                        "Original": "I try to soothe my angry feelings"},
            **kwargs
        )


class STAXI2Q41(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['boil inside without showing it', 'suppress your anger internally', 'hide your anger'],
                                         ['feel calm inside', 'process your emotions openly', 'feel at peace internally'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-in",
                        "Ordinal": 41,
                        "Original": "I boil inside, but I don't show it"},
            **kwargs
        )


class STAXI2Q42(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['lose control of your behavior', 'act out impulsively', 'behave aggressively'],
                                         ['control your behavior', 'act composed', 'behave appropriately'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-out",
                        "Ordinal": 42,
                        "Original": "I control my behavior"},
            **kwargs
        )


class STAXI2Q43(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['do things like slam doors', 'act out physically', 'express anger through objects'],
                                         ['stay physically controlled', 'avoid physical outbursts', 'remain composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-out",
                        "Ordinal": 43,
                        "Original": "I do things like slam doors"},
            **kwargs
        )


class STAXI2Q44(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['stay angry', 'make no effort to calm down', 'remain worked up'],
                                         ['endeavor to become calm again', 'work to regain composure', 'try to settle down'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-in",
                        "Ordinal": 44,
                        "Original": "I endeavor to become calm again"},
            **kwargs
        )


class STAXI2Q45(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['harbor grudges that you keep to yourself', 'hold on to resentment silently', 'nurse hidden anger'],
                                         ['let go of grievances', 'forgive and move on', 'not hold grudges'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-in",
                        "Ordinal": 45,
                        "Original": "I tend to harbor grudges that I don't tell anyone about"},
            **kwargs
        )


class STAXI2Q46(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['fail to stop yourself from losing your temper', 'give in to anger', 'lose control'],
                                         ['stop yourself from losing your temper', 'maintain control', 'hold yourself back'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-out",
                        "Ordinal": 46,
                        "Original": "I can stop myself from losing my temper"},
            **kwargs
        )


class STAXI2Q47(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['argue with others', 'get into conflicts', 'confront others aggressively'],
                                         ['stay calm with others', 'avoid arguments', 'remain composed'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-out",
                        "Ordinal": 47,
                        "Original": "I argue with others"},
            **kwargs
        )


class STAXI2Q48(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['let your anger persist', 'hold on to anger', 'stay angry'],
                                         ['reduce your anger as soon as possible', 'let go of anger quickly', 'de-escalate internally'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-in",
                        "Ordinal": 48,
                        "Original": "I reduce my anger as soon as possible"},
            **kwargs
        )


class STAXI2Q49(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, are you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['secretly critical of others', 'silently judgmental', 'internally resentful'],
                                         ['accepting of others', 'non-judgmental', 'inwardly at peace'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-in",
                        "Ordinal": 49,
                        "Original": "I am secretly quite critical of others"},
            **kwargs
        )


class STAXI2Q50(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['become intolerant and critical', 'grow dismissive', 'become impatient'],
                                         ['try to be tolerant and understanding', 'stay empathetic', 'remain patient'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-out",
                        "Ordinal": 50,
                        "Original": "I try to be tolerant and understanding"},
            **kwargs
        )


class STAXI2Q51(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['strike out at whatever infuriates you', 'lash out at your anger trigger', 'act aggressively'],
                                         ['stay controlled', 'hold back', 'respond calmly'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-out",
                        "Ordinal": 51,
                        "Original": "I strike out at whatever infuriates me"},
            **kwargs
        )


class STAXI2Q52(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['stay tense and agitated', 'do nothing to calm yourself', 'remain wound up'],
                                         ['do something relaxing to calm down', 'engage in calming activities', 'self-soothe'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-in",
                        "Ordinal": 52,
                        "Original": "I do something relaxing to calm down"},
            **kwargs
        )


class STAXI2Q53(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, are you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['angrier than you are willing to admit', 'hiding more anger than you show', 'concealing your true anger'],
                                         ['honest about how angry you are', 'transparent about your emotions', 'self-aware about your anger'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-in",
                        "Ordinal": 53,
                        "Original": "I am angrier than I am willing to admit"},
            **kwargs
        )


class STAXI2Q54(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['lose control of your angry feelings', 'act on your anger', 'let anger overwhelm you'],
                                         ['control your angry feelings', 'manage your anger', 'keep anger in check'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-out",
                        "Ordinal": 54,
                        "Original": "I control my angry feelings"},
            **kwargs
        )


class STAXI2Q55(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['say nasty things', 'say hurtful things', 'verbally lash out'],
                                         ['stay respectful', 'hold back', 'speak calmly'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-out",
                        "Ordinal": 55,
                        "Original": "I say nasty things"},
            **kwargs
        )


class STAXI2Q56(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, do you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['stay tense', 'remain wound up', 'keep agitated'],
                                         ['try to relax', 'calm yourself down', 'let go of tension'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-control-in",
                        "Ordinal": 56,
                        "Original": "I try to relax"},
            **kwargs
        )


class STAXI2Q57(QCLM):
    def __init__(self, **kwargs):
        super().__init__(
            template="Question: When feeling angry or furious, are you {question}? Answer: {answer}",
            dimensions={
                "answer": frequency_weights,
                "question": dict_pos_neg(['more irritated than people are aware of', 'hiding more irritation than you show', 'concealing your true irritation'],
                                         ['as calm as people perceive you', 'genuinely at peace', 'not hiding inner anger'], 1.0),
            },
            descriptor={"Questionnair": "STAXI-2",
                        "Factor": "anger-expression-in",
                        "Ordinal": 57,
                        "Original": "I'm irritated a great deal more than people are aware of"},
            **kwargs
        )


staxi2_qclm = [
    STAXI2Q1,  STAXI2Q2,  STAXI2Q3,  STAXI2Q4,  STAXI2Q5,
    STAXI2Q6,  STAXI2Q7,  STAXI2Q8,  STAXI2Q9,  STAXI2Q10,
    STAXI2Q11, STAXI2Q12, STAXI2Q13, STAXI2Q14, STAXI2Q15,
    STAXI2Q16, STAXI2Q17, STAXI2Q18, STAXI2Q19, STAXI2Q20,
    STAXI2Q21, STAXI2Q22, STAXI2Q23, STAXI2Q24, STAXI2Q25,
    STAXI2Q26, STAXI2Q27, STAXI2Q28, STAXI2Q29, STAXI2Q30,
    STAXI2Q31, STAXI2Q32, STAXI2Q33, STAXI2Q34, STAXI2Q35,
    STAXI2Q36, STAXI2Q37, STAXI2Q38, STAXI2Q39, STAXI2Q40,
    STAXI2Q41, STAXI2Q42, STAXI2Q43, STAXI2Q44, STAXI2Q45,
    STAXI2Q46, STAXI2Q47, STAXI2Q48, STAXI2Q49, STAXI2Q50,
    STAXI2Q51, STAXI2Q52, STAXI2Q53, STAXI2Q54, STAXI2Q55,
    STAXI2Q56, STAXI2Q57,
]
staxi2_qclm_list = staxi2_qclm
