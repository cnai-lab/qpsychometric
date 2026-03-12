from qlatent.qclm.qclm import QCLM, SCALE, dict_pos_neg

heb_frequency_weights_1:SCALE = {
    'לעולם לא': -4,
    'לעיתים נדירות מאוד': -3,
    'לעיתים רחוקות': -2,
    'לעיתים רחוקות מאוד': -2,
    'לעיתים קרובות': 2,
    'לעיתים תכופות': 2,
    'לעיתים קרובות מאוד': 3,
    'תמיד': 4,
}

agreement_weights_he = {
    "מסכים במידה רבה" : 2,
    "מסכים" : 1,
    "ניטרלי" : 0,
    "לא מסכים" : -1,
    "לא מסכים במידה רבה" : -2
}
    

class BESQ1(QCLM):
    """
    BESQ1: My friend’s emotions don’t affect me much.
    """

    kw_pos=["מרגיש כמוהו", "מביע הזדהות"]
    kw_neg=["אדיש למצבו", "קר רוח"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: כשמישהו שקרוב אליך מרגיש רגש כלשהו, באיזה תדירות אתה {שאלה}? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"AE",
                          "Ordinal":1,
                          "Original": "כשמישהו קרוב אלי מרגיש משהו זה גורם לי גם להרגיש את אותו הדבר." #REVERSED
            },
            **kwargs,
        )



class BESQ2(QCLM):
    """
    BES2: After being with a friend who is sad about something, I usually feel sad
    """
    kw_pos=["מרגיש כמוהו", "מביע הזדהות"]
    kw_neg=["אדיש למצבו", "קר רוח"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(    
            template = r"שאלה: כשאתה נמצא עם אדם המרגיש עצב, באיזה תדירות אתה {שאלה}? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"AE",
                          "Ordinal":2,
                          "Original": 'אם אני נמצא עם מישהו שמרגיש עצב, גם אני מרגיש עצב.'
            },
            **kwargs,
        )    


class BESQ4(QCLM):
    """
    BESQ4: I get frightened when I watch characters in a good scary movie.
    """
    kw_pos=["מרגיש כמוהן","מזדהה איתן"]
    kw_neg=["אדיש לסיטואציה","מתעלם מרגשותיהן"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: כאשר אתה צופה בדמויות בסרט אימה, באיזה תדירות אתה {שאלה}? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"AE",
                          "Ordinal":4,
                          "Original": 'אם אני צופה בדמויות בסרט והן מרגישות משהו - גם אני מרגיש את אותו הדבר.'
            },
            **kwargs,
        )
    

class BESQ5(QCLM):
    """
    BESQ5: I get caught up in other people’s feelings easily.
    """
    kw_pos=["מעורב ב","מחובר ל", "קשור ב"]
    kw_neg=["מנותק מ","אדיש ל"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: באיזה תדירות אתה {שאלה}רגשות של אחרים? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"AE",
                          "Ordinal":5,
                          "Original": 'אני נעשה מעורב רגשית ברגשותיהם של אחרים.'
            },
            **kwargs,
        )    


class BESQ7(QCLM):
    """
    BESQ7: I don’t become sad when I see other people crying.
    """
    kw_pos=["מדוכדכך","עצוב", "מצוברח"]
    kw_neg=["קר רוח","אדיש"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"עד כמה אתה מסכים עם האימרה: אני {שאלה} כשאני רואה אחרים בוכים? תשובה: {תשובה}",
            dimensions={
                        "תשובה":agreement_weights_he,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"AE",
                          "Ordinal":7,
                          "Original": 'אם אני רואה אנשים אחרים בוכים - זה גורם לי להיות עצוב' #REVERSED
            },
            **kwargs,
        )    
    

class BESQ8(QCLM):
    """
    BESQ8: Other people’s feelings don’t bother me at all.
    """
    kw_pos=["מעצבים את", "מכתיבים את"]
    kw_neg=["חסרי השפעה על", "לא משנים את"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: באיזה תדירות רגשות של אחרים {שאלה} איך שאתה מרגיש? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"AE",
                          "Ordinal":8,
                          "Original": "רגשות של אנשים אחרים משפיעים על איך שאני מרגיש." #REVERSED
            },
            **kwargs,
        )    
    
    

class BESQ11(QCLM):
    """
    BESQ11: I often become sad when watching sad things on TV or in films.
    """
    kw_pos=["עצב","דיכאון"]
    kw_neg=["אדישות","קרות רוח"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"עד כמה אתה מסכים עם האימרה: אני מרגיש {שאלה} כאשר אני צופה בתכנים עצובים? תשובה: {תשובה}",
            dimensions={
                        "תשובה":agreement_weights_he,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"AE",
                          "Ordinal":11,
                          "Original": 'אם אני צופה בדבר מה עצוב או קורא דבר מה עצוב - אני נעשה עצוב בעצמי'
            },
            **kwargs,
        )    



class BESQ13(QCLM):
    """
    BESQ13: Seeing a person who has been angered has no effect on my feelings.
    """
    kw_pos=["מעצב את", "מכתיב את"]
    kw_neg=["לא משפיע על", "לא משנה את"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"עד כמה אתה מסכים עם האימרה: להיות בנוכחות אדם כועס, {שאלה} רגשותיי? תשובה: {תשובה}",
            dimensions={
                        "תשובה":agreement_weights_he,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"AE",
                          "Ordinal":13,
                          "Original": 'אם אני מדבר עם מישהו כועס - זה משפיע על רגשותי' #REVERSED
            },
            **kwargs,
        )    

        
class BESQ15(QCLM):
    """
    BESQ15: I tend to feel scared when I am with friends who are afraid.
    """
    kw_pos=["מפחד" , "מודאג"]
    kw_neg=["אדיש","קר רוח"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"עד כמה אתה מסכים עם האימרה: כאשר אנשים סביבי מפחדים, אני {שאלה}? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"AE",
                          "Ordinal":15,
                          "Original": 'אם אנשים מסביבי מפחדים - גם אני נעשה מפוחד.'
            },
            **kwargs,
        )    
    


class BESQ17(QCLM):
    """
    BESQ17: I often get swept up in my friend’s feelings.
    """
    kw_pos=["משפיעים על", "מכתיבים את"]
    kw_neg=["חסרי השפעה על", "לא משנים את"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: באיזה תדירות הרגשות של חבריך {שאלה} הרגשות שלך? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"AE",
                          "Ordinal":17,
                          "Original": 'הרגשות של חברי משפיעים עלי מאוד.'
            },
            **kwargs,
        )    
    


class BESQ18(QCLM):
    """
    BESQ18: My friend’s unhappiness doesn’t make me feel anything.
    """
    kw_pos=["מרגיש כמוהו", "מביע הזדהות"]
    kw_neg=["אדיש למצבו", "קר רוח"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: כאשר חברך עצוב, באיזה תדירות אתה {שאלה}? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"AE",
                          "Ordinal":18,
                          "Original": 'כאשר אדם שקרוב אלי עצוב - גם אני מרגיש עצוב.' #REVERSED
            },
            **kwargs,
        )    
    


class BESQ3(QCLM):
    """
    BESQ3: I can understand my friend’s happiness when she/he does well at something.
    """
    kw_pos = ["מבין את ", "קולט את "]
    kw_neg = ["אדיש ל" , "מתעלם מ"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"עד כמה אתה מסכים עם האימרה: כאשר אנשים מצליחים הם שמחים, אני {שאלה}שמחתם? תשובה: {תשובה}",
            dimensions={
                        "תשובה":agreement_weights_he,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"CE",
                          "Ordinal":3,
                          "Original": 'אני מבין למה אנשים אחרים שמחים כשהם מצליחים בדברים.'
            },
            **kwargs,
        )    
    


class BESQ6(QCLM):
    """
    BESQ6: I find it hard to know when my friends are frightened.
    """
    kw_pos = ["מבין את ", "קולט את "]
    kw_neg = ["אדיש ל" , "מתעלם מ"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: באיזה תדירות אתה {שאלה}תחושת הפחד של אחרים? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"CE",
                          "Ordinal":6,
                          "Original": 'קל לי להבין כשאנשים אחרים חשים פחד.'
            },
            **kwargs,
        )    
    


class BESQ9(QCLM):
    """
    BESQ9: When someone is feeling down I can usually understand how she/he feels.
    """
    kw_pos = ["מבין את ", "קולט את "]
    kw_neg = ["אדיש ל" , "מתעלם מ"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: באיזה תדירות אתה {שאלה}תחושת העצב של אחרים? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"CE",
                          "Ordinal":9,
                          "Original": 'אם מישהו מרגיש עצוב אני יכול להבין איך הוא מרגיש.'
            },
            **kwargs,
        )
    



class BESQ10(QCLM):
    """
    BESQ10: I can usually work out when my friends are scared.
    """
    kw_pos = ["מבין את ה", "קולט את ה"]
    kw_neg = ["אדיש ל" , "מתעלם מה"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: באיזה תדירות אתה {שאלה}פחד של חבריך? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"CE",
                          "Ordinal":10,
                          "Original": 'אני מבין מתי חבריי מרגישים פחד.'
            },
            **kwargs,
        )
        
        
    
class BESQ12(QCLM):
    """
    BESQ12: I can often understand how people are feeling even before they tell me.
    """
    kw_pos = ["מבין ", "קולט "]
    kw_neg = ["מפספס " , "מתעלם מ"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"עד כמה אתה מסכים עם האימרה: אני {שאלה}רגשות של אחרים לפני שהם אומרים? תשובה: {תשובה}",
            dimensions={
                        "תשובה":agreement_weights_he,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"CE",
                          "Ordinal":12,
                          "Original": 'אני מבין מה אנשים אחרים מרגישים גם אם הם לא אומרים לי את זה בצורה ישירה.'
            },
            **kwargs,
        ) 
        
        
    
class BESQ14(QCLM):
    """
    BESQ14: I can usually work out when people are cheerful.
    """
    kw_pos=["קלה","פשוטה"]
    kw_neg=["מאתגרת","מסובכת"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: באיזה תדירות תחושת שמחה של אחרים היא {שאלה} לזיהוי בעבורך? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"CE",
                          "Ordinal":14,
                          "Original": 'אני יודע מתי אנשים אחרים שמחים.'
            },
            **kwargs,
        ) 
        
        
    
class BESQ16(QCLM):
    """
    BESQ16: I can usually realize quickly when a friend is angry.
    """
    kw_pos=["קלה","פשוטה"]
    kw_neg=["מאתגרת","מסובכת"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: באיזה תדירות תחושת הכעס של חבריך היא {שאלה} לזיהוי בעבורך? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"CE",
                          "Ordinal":16,
                          "Original": 'אני מבין במהירות אם החברים שלי חשים כעס.'
            },
            **kwargs,
        ) 
        
    
    
class BESQ19(QCLM):
    """
    BESQ19: I am not usually aware of my friend’s feelings.
    """
    kw_pos=["מובנים","ברורים"]
    kw_neg=["מעורפלים","נסתרים"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: באיזה תדירות הרגשות של אנשים סביבך {שאלה} לך? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"CE",
                          "Ordinal":19,
                          "Original": 'אני יודע איך אנשים שסביבי מרגישים.' #REVERSED
            },
            **kwargs,
        ) 
        
    
    
class BESQ20(QCLM):
    """
    BESQ20: I have trouble figuring out when my friends are happy.
    """
    kw_pos=["קלה","פשוטה"]
    kw_neg=["מאתגרת","מסובכת"]
    dict_attitude = dict_pos_neg(kw_pos,kw_neg,1)
    def __init__(self, **kwargs):
        super().__init__(
            template = r"שאלה: באיזה תדירות תחושת השמחה של חבריך {שאלה} לזיהוי עבורך? תשובה: {תשובה}",
            dimensions={
                        "תשובה":heb_frequency_weights_1,
                        "שאלה":self.dict_attitude,
            },
            descriptor = {"Questionnair":"BES",
                          "Factor":"CE",
                          "Ordinal":20,
                          "Original": 'אני מבין בקלות מתי האנשים הסובבים אותי מרגישים שמחה.' # REVERSED
            },
            **kwargs,
        )    
    
      
    
basic_empathy_scale_heb_qclm_list = [BESQ1, BESQ2, BESQ3, BESQ4, BESQ5, BESQ6, BESQ7, BESQ8, BESQ9, BESQ10, BESQ11, BESQ12, BESQ13, BESQ14, BESQ15, BESQ16, BESQ17, BESQ18, BESQ19, BESQ20]