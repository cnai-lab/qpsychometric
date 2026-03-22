from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg

likert_weights: SCALE = {
    "not at all": -2,
    "somewhat": -1,
    "moderately": 1,
    "very much": 2
}

# frequency_weights: SCALE = {
#     'almost never': -2,
#     'sometimes': -1,
#     'often': 1,
#     'almost always': 2,
# }


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
                "question": dict_pos_neg(['angry', 'mad'],
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
                "question": dict_pos_neg(['like yelling', 'like screaming', 'like shouting'],
                                         ['calm', 'restrained', 'composed'], 1.0),
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
                "question": dict_pos_neg(['like breaking things', 'like smashing things', 'destructive'],
                                         ['controlled', 'composed', 'in control'], 1.0),
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
                "question": dict_pos_neg(['like banging things', 'like hitting things', 'physically agitated'],
                                         ['calm', 'composed', 'controlled'], 1.0),
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
                "question": dict_pos_neg(['like hitting someone', 'like striking someone', 'aggressive'],
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
                "question": dict_pos_neg(['like swearing', 'like cursing', 'profane'],
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
                                         ['patient', 'at ease'], 1.0),
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
                "question": dict_pos_neg(['like kicking someone', 'like attacking someone', 'violent'],
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
                "question": dict_pos_neg(['like cursing aloud', 'like shouting obscenities', 'verbally explosive'],
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
                "question": dict_pos_neg(['like screaming', 'like yelling', 'enraged'],
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
                "question": dict_pos_neg(['like pounding someone', 'like attacking someone', 'violently aggressive'],
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
                "question": dict_pos_neg(['like shouting', 'like yelling loudly', 'verbally explosive'],
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
                "answer": likert_weights,
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
                "answer": likert_weights,
                "question": dict_pos_neg(['fiery temper', 'hot temper', 'volatile temper'],
                                         ['calm temper', 'mild temper', 'even temper'], 1.0),
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
                "answer": likert_weights,
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
                "answer": likert_weights,
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
            template="Question: In general, do you feel {question} when not given recognition for good work? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
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
                "answer": likert_weights,
                "question": dict_pos_neg(['fly off the handle', 'lose your temper', 'explode'],
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
                "answer": likert_weights,
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
                "answer": likert_weights,
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
                "answer": likert_weights,
                "question": dict_pos_neg(['like hitting someone', 'aggressive', 'hostile'],
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
                "answer": likert_weights,
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
                "answer": likert_weights,
                "question": dict_pos_neg(['lose your temper', 'give in to anger', 'lose control'],
                                         ['control your temper', 'keep in check', 'stay composed'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['express your anger', 'vent your anger', 'let your anger out'],
                                         ['hold back', 'stay composed', 'keep it inside'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['stay tense', 'remain agitated', 'keep fuming'],
                                         ['breathe and relax', 'calm down', 'compose yourself'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['keep things in', 'bottle it up', 'internalize'],
                                         ['express yourself', 'let it out', 'speak up'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['impatient', 'intolerant', 'short with people'],
                                         ['patient', 'tolerant', 'understanding'], 1.0),
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
            template="Question: When someone annoys you, do you {question}? Answer: {answer}",
            dimensions={
                "answer": likert_weights,
                "question": dict_pos_neg(['confront them', 'voice displeasure', 'tell them off'],
                                         ['keep it to yourself', 'stay quiet', 'hold back'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['let anger linger', 'stay upset', 'remain angry'],
                                         ['calm yourself quickly', 'settle down quickly', 'soothe yourself'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['pout', 'sulk', 'brood'],
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
                "answer": likert_weights,
                "question": dict_pos_neg(['give in to anger', 'act impulsively', 'lose control'],
                                         ['control your urge', 'restrain yourself', 'hold back'], 1.0),
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
                "answer": likert_weights,
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
                "answer": likert_weights,
                "question": dict_pos_neg(['stay worked up', 'remain heated', 'keep fuming'],
                                         ['simmer down', 'cool off', 'calm yourself'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['withdraw', 'isolate yourself', 'pull away'],
                                         ['stay connected', 'remain engaged', 'stay present'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['lose your cool', 'get heated', 'lose composure'],
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
                "answer": likert_weights,
                "question": dict_pos_neg(['make sarcastic remarks', 'say cutting things', 'be verbally hostile'],
                                         ['stay respectful', 'speak kindly', 'hold back'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['let anger grow', 'feed your anger', 'stay agitated'],
                                         ['soothe yourself', 'calm yourself', 'settle yourself'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['boil inside silently', 'suppress your anger', 'hide your anger'],
                                         ['feel calm inside', 'process openly', 'feel at peace'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['lose control', 'act impulsively', 'behave aggressively'],
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
                "answer": likert_weights,
                "question": dict_pos_neg(['slam doors', 'act out physically', 'throw things'],
                                         ['stay controlled', 'avoid outbursts', 'remain composed'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['stay angry', 'refuse to calm down', 'remain worked up'],
                                         ['seek calm again', 'regain composure', 'settle down'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['harbor secret grudges', 'resent silently', 'nurse hidden anger'],
                                         ['let go', 'forgive and move on', 'release resentment'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['fail to hold back', 'give in to anger', 'lose control'],
                                         ['hold yourself back', 'maintain control', 'stay restrained'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['argue with others', 'get into conflicts', 'confront aggressively'],
                                         ['stay calm', 'avoid arguments', 'remain composed'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['let anger persist', 'hold on to anger', 'stay angry'],
                                         ['reduce anger quickly', 'let go quickly', 'de-escalate'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['secretly critical', 'silently judgmental', 'internally resentful'],
                                         ['accepting', 'non-judgmental', 'at peace inside'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['become intolerant', 'grow dismissive', 'become impatient'],
                                         ['stay tolerant', 'stay empathetic', 'remain patient'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['explode at others', 'lash out', 'act aggressively'],
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
                "answer": likert_weights,
                "question": dict_pos_neg(['stay agitated', 'refuse to calm down', 'remain wound up'],
                                         ['do something relaxing', 'self-soothe', 'unwind'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['angrier than you admit', 'hiding your anger', 'concealing anger'],
                                         ['honest about your anger', 'emotionally transparent', 'self-aware'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['lose control', 'act on your anger', 'let anger overwhelm'],
                                         ['control your anger', 'manage your anger', 'keep anger in check'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['say nasty things', 'say hurtful things', 'lash out verbally'],
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
                "answer": likert_weights,
                "question": dict_pos_neg(['stay tense', 'remain wound up', 'keep agitated'],
                                         ['try to relax', 'calm down', 'let go of tension'], 1.0),
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
                "answer": likert_weights,
                "question": dict_pos_neg(['secretly irritated', 'hiding irritation', 'concealing irritation'],
                                         ['genuinely calm', 'openly at peace', 'truly unbothered'], 1.0),
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
