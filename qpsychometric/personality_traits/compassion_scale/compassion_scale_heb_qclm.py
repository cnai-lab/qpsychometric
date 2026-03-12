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


class CSQ1(QCLM):
  kw_attitude_pos = ['מזדהה עם ' , 'אמפתי ל']
  kw_attitude_neg = ['מנוכר ל' , 'קר רוח ל']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}אנשים שבוכים מולך? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"disengagement",
                      "Ordinal":1,
                      "Original":'when people cry in front of me, I often don’t feel anything at all.'
        },
        **kwargs,
    )




class CSQ7(QCLM):
  kw_attitude_pos = ['מקשיב ל' , 'מתעניין ב']
  kw_attitude_neg = ['מפסיק להקשיב ל' , 'נמנע מלהקשיב ל']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}אנשים המספרים לך על הצרות שלהם? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"disengagement",
                      "Ordinal":7,
                      "Original":'I often tune out when people tell me about their troubles.'
        },
        **kwargs,
    )
        



class CSQ19(QCLM):
  kw_attitude_pos = ['מתייחס ל' , 'מתעניין ב']
  kw_attitude_neg = ['מתעלם מ' , 'מזניח ' ]
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}צרות של אחרים? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"disengagement",
                      "Ordinal":19,
                      "Original":'I don’t think much about the concerns of others.'
        },
        **kwargs,
    )




class CSQ23(QCLM):
  kw_attitude_pos = ['מתקרב ל' , 'קשוב ל']
  kw_attitude_neg = [ 'מתרחק מ', 'נמנע מ']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}אנשים שחשים הרבה כאב? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"disengagement",
                      "Ordinal":23,
                      "Original":'I try to avoid people who are experiencing a lot of pain.'
        },
        **kwargs,
    )        


class CSQ2(QCLM):
  kw_attitude_pos = ['מזדהה עם ' , 'אמפתי ל']
  kw_attitude_neg = ['אדיש ל' , 'קר רוח ל']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}אנשים שמדברים על בעיותיהם? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"indifference",
                      "Ordinal":2,
                      "Original":'sometimes when people talk about their problems, I feel like I don’t care.'
        },
        **kwargs,
    )        



class CSQ12(QCLM):
  kw_attitude_pos = ['רגיש' , 'חם' , 'אמפתי']
  kw_attitude_neg = ['קר רוח' , 'אפתי' , 'חסר עניין']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה} כלפי אנשים כשהם מדוכאים? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"indifference",
                      "Ordinal":12,
                      "Original":'Sometimes I am cold to others when they are down and out.'
        },
        **kwargs,
    )        
        


class CSQ14(QCLM):
  kw_attitude_pos = ['מתייחס ל' , 'מתעניין ב']
  kw_attitude_neg = ['מתעלם מ' , 'מזניח ']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}בעיות של אנשים אחרים? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"indifference",
                      "Ordinal":14,
                      "Original":'I don’t concern myself with other people’s problems.'
        },
        **kwargs,
    )        



class CSQ18(QCLM):
  kw_attitude_pos = ['עוזר ל' , 'מסייע ל']
  kw_attitude_neg = ['מתעלם מ' , 'מתרחק מ' , 'נמנע מלטפל ב']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(   
        template = r"שאלה: באיזה תדירות אתה {שאלה}אנשים המרגישים טרודים? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"indifference",
                      "Ordinal":18,
                      "Original":'When others are feeling troubled, I usually let someone else attend to them.'
        },
        **kwargs,
    )        



class CSQ3(QCLM):
  kw_attitude_pos = ['מחובר רגשית'  , 'אמפתי']
  kw_attitude_neg = ['קר רוח' , 'מנוכר']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה} כלפי אנשים שסובלים? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"separation",
                      "Ordinal":3,
                      "Original":'I don’t feel emotionally connected to people in pain.'
        },
        **kwargs,
    )        


class CSQ5(QCLM):
  kw_attitude_pos = ['קשור ל', 'קרוב ל']
  kw_attitude_neg = ['מנותק מ' , 'מרוחק מ' ]
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__( 
        template = r"שאלה: באיזה תדירות אתה {שאלה}אנשים שמספרים לך על הצרות שלהם? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"separation",
                      "Ordinal":5,
                      "Original":'I feel detached from others when they tell me their tales of woe.'
        },
        **kwargs,
    )        


class CSQ10(QCLM):
  kw_attitude_neg = ['מתעלם מ' , 'מתרחק מ']
  kw_attitude_pos = ['מזדהה עם ' , 'מתקרב אל ' , 'מבין ']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}אדם עצוב? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"separation",
                      "Ordinal":10,
                      "Original":'When I see someone feeling down, I feel like I can’t relate to them.'
        },
        **kwargs,
    )        


class CSQ22(QCLM):
  kw_attitude_pos = ['מתחבר ל' , 'מזדהה עם ']
  kw_attitude_neg = ['מתנתק מ' , 'מתרחק מ' ]
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}אנשים אחרים כשהם סובלים? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"separation",
                      "Ordinal":22,
                      "Original":"I can’t really connect with other people when they’re suffering."
        },
        **kwargs,
    )        
        


class CSQ4(QCLM):
  kw_attitude_neg = ['מתעלם מ' , 'מתנתק מ']
  kw_attitude_pos = ['מתעניין ב' , 'מתמקד ב']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}אנשים שמדברים אליך? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"mindfulness",
                      "Ordinal":4,
                      "Original":'I pay careful attention when other people talk to me.'
        },
        **kwargs,
    )        


class CSQ9(QCLM):
  kw_attitude_neg = ['מחמיץ את ה' , 'מפספס את ה' ]
  kw_attitude_pos = ['שם לב ל' , 'מבחין ב' ]
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}כעס של אנשים, גם אם הם לא אומרים דבר? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"mindfulness",
                      "Ordinal":9,
                      "Original":'I notice when people are upset, even if they don’t say anything.'
        },
        **kwargs,
    )        
        


class CSQ13(QCLM):
  kw_attitude_neg = ['חוסר איפוק' , 'עצבנות']
  kw_attitude_pos = [ 'רוגע', 'מתינות' , 'איפוק']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"כמה אתה מסכים עם האימרה: אני מקשיב ב{שאלה} כאשר אנשים מספרים לי על הבעיות שלהם? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"mindfulness",
                      "Ordinal":13,
                      "Original":'I tend to listen patiently when people tell me their problems.'
        },
        **kwargs,
    )        


class CSQ21(QCLM):
  kw_attitude_neg = ['קיצונית' , 'מעוותת' , 'לא מדודה']
  kw_attitude_pos = ['מאוזנת' , 'שקולה' , 'הוגנת']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה שומר על פרספקטיבה {שאלה} של המצב, כאשר אנשים מספרים לך על הבעיות שלהם? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"mindfulness",
                      "Ordinal":21,
                      "Original":'when people tell me about their problems, I try to keep a balanced perspective on the situation.'
        },
        **kwargs,
    )        



class CSQ6(QCLM):
  kw_attitude_neg = ['לנטוש ' , 'להתעלם מ']
  kw_attitude_pos = ['לדאוג ל' , 'לעזור ל' ]
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה רוצה {שאלה}אדם העובר תקופה קשה? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"kindness",
                      "Ordinal":6,
                      "Original":'If I see someone going through a difficult time, I try to be caring toward that person.'
        },
        **kwargs,
    )        



class CSQ8(QCLM):
  kw_attitude_neg = ['לזנוח ' , 'לנטוש ' ]
  kw_attitude_pos = ['לתמוך ב' , 'לסייע ל' , 'ללוות ']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה אוהב {שאלה}אנשים העוברים תקופה קשה? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"kindness",
                      "Ordinal":8,
                      "Original":'I like to be there for others in times of difficulty.'
        },
        **kwargs,
    )        


class CSQ16(QCLM):
  kw_attitude_neg = ['ניכור' , 'אפתיה' , 'חוסר איכפתיות']
  kw_attitude_pos = ['סימפתיה' , 'הזדהות' , 'אהדה']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה מרגיש {שאלה} כלפי אנשים עצובים? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"kindness",
                      "Ordinal":16,
                      "Original":'My heart goes out to people who are unhappy.'
        },
        **kwargs,
    )        



class CSQ24(QCLM):
  kw_attitude_neg = ['להקשות על ' , 'להזיק ל']
  kw_attitude_pos = ['לעודד ' , 'להרגיע ' ]
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה מנסה {שאלה}אנשים החשים עצב? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"kindness",
                      "Ordinal":24,
                      "Original":'when others feel sadness, I try to comfort them.'
        },
        **kwargs,
    )        




class CSQ11(QCLM):
  kw_attitude_neg = ['חסר רגשות' , 'לא אנושי']
  kw_attitude_pos = ['אנושי' , 'טבעי' ]
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: כמה אתה מסכים עם האימרה שלהיות עצוב זה חלק מלהיות {שאלה}? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"common humanity",
                      "Ordinal":11,
                      "Original":'Everyone feels down sometimes, it is part of being human.'
        },
        **kwargs,
    )        



class CSQ15(QCLM):
  kw_attitude_neg = ['חסר ערך' , 'חסר משמעות' , 'שולי']
  kw_attitude_pos = ['חשוב' , 'משמעותי']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: כמה אתה מסכים עם האימרה שזה {שאלה} להכיר בכך שלכל האנשים יש חולשות ואף אחד לא מושלם? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"common humanity",
                      "Ordinal":15,
                      "Original":"It’s important to recognize that all people have weaknesses and no one’s perfect."
        },
        **kwargs,
    )       
        


class CSQ17(QCLM):
  kw_attitude_neg = ['אחר' , 'שונה']
  kw_attitude_pos = ['זהה' , 'דומה']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: כמה אתה מסכים עם האימרה שכולם מרגישים כאב באופן {שאלה}? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"common humanity",
                      "Ordinal":17,
                      "Original":'Despite my differences with others, I know that everyone feels pain just like me.'
        },
        **kwargs,
    )        
        


class CSQ20(QCLM):
  kw_attitude_neg = ['חסר ערך' , 'חסר משמעות']
  kw_attitude_pos = ['חשוב'  , 'משמעותי']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: כמה אתה מסכים עם האימרה שסבל הוא חלק {שאלה} בחוויה האנושית? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"CS",
                      "Factor":"common humanity",
                      "Ordinal":20,
                      "Original":'Suffering is just a part of the common human experience.'
        },
        **kwargs,
    )       
        
                 
        
compassion_scale_heb_qclm_list = [CSQ1, CSQ2, CSQ3, CSQ4, CSQ5, CSQ6, CSQ7, CSQ8, CSQ9, CSQ10, CSQ11, CSQ12, CSQ13, CSQ14, CSQ15, CSQ16, CSQ17, CSQ18, CSQ19, CSQ20, CSQ21, CSQ22, CSQ23, CSQ24]