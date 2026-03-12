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

class IRIQ1(QCLM):
  kw_attitude_neg = ['ערני ל' , 'קשוב ל']
  kw_attitude_pos = ['חולם בהקיץ על ' , 'מפנטז על ']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}דברים שעלולים לקרות לך? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Fantasy",
                      "Ordinal":1,
                      "Original":'I daydream and fantasize, with some regularity, about things that might happen to me.'
        },
        **kwargs,
    )



class IRIQ5(QCLM):
  kw_attitude_neg = ['מנותק מ' , 'אדיש ל']
  kw_attitude_pos = ['מושפע מ' , 'נסחף מ']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}רגשותיהם של דמויות בספרים ובסרטים? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Fantasy",
                      "Ordinal":5,
                      "Original":'I really get involved with the feelings of the characters in a novel.'
        },
        **kwargs,
    )



class IRIQ7(QCLM):
  kw_attitude_neg = ['קשור רגשית ב' , 'מעורב רגשית ב']
  kw_attitude_pos = ['אובייקטיבי ל' , 'אדיש ל']
  dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}עלילה כשאתה צופה בסרט או הצגה? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Fantasy",
                      "Ordinal":7,
                      "Original":"I am usually objective when I watch a movie or play, and I don't often get completely caught up in it."
        },
        **kwargs,
    )                 



class IRIQ12(QCLM):
  kw_attitude_neg = ['מחובר' , 'קשור' ]
  kw_attitude_pos = ['מנותק' , 'אדיש']
  dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה} רגשית לספר שקראת? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Fantasy",
                      "Ordinal":12,
                      "Original":'Becoming extremely involved in a good book or movie is somewhat rare for me.'
        },
        **kwargs,
    ) 


class IRIQ16(QCLM):
  kw_attitude_neg = ["אפתי כלפי ה", "אדיש כלפי ה"]
  kw_attitude_pos = ['מרגיש חיבור ל' , 'מזדהה עם ה']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}דמויות בסרט או הצגה? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Fantasy",
                      "Ordinal":16,
                      "Original":'After seeing a play or movie, I have felt as though I were one of the characters.'
        },
        **kwargs,
    )



class IRIQ23(QCLM):
  kw_attitude_neg = ['באופן מאולץ'  , 'בקושי רב']
  kw_attitude_pos = ['בקלות' , 'בטבעיות']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: כשאתה צופה בסרט טוב, באיזה תדירות אתה {שאלה} שם את עצמך במקום הדמות הראשית? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Fantasy",
                      "Ordinal":23,
                      "Original":'When I watch a good movie, I can very easily put myself in the place of a leading character.'
        },
        **kwargs,
    )


class IRIQ26(QCLM):
  kw_attitude_neg = ['מתעלם מ', "אדיש ל"]
  kw_attitude_pos = ['מדמיין ', 'מפנטז ', 'מהרהר ']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: כשאתה קורא סיפור מעניין, באיזה תדירות אתה {שאלה}איך היית מרגיש אם האירועים בסיפור היו קורים לך? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Fantasy",
                      "Ordinal":26,
                      "Original":'When I am reading an interesting story or novel, I imagine how I would feel if the events in the story were happening to me.'
        },
        **kwargs,
    )



class IRIQ2(QCLM):
  kw_attitude_neg = [ 'ניכור' , 'חוסר איכפתיות']
  kw_attitude_pos = [ 'חמלה' , 'אהדה']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(  
        template = r"שאלה: באיזה תדירות אתה חש {שאלה} כלפי אנשים שיש להם פחות מזל מאשר יש לך? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Empathic Concern",
                      "Ordinal":2,
                      "Original":'I often have tender, concerned feelings for people less fortunate than me.'
        },
        **kwargs,
    )



class IRIQ9(QCLM):
  kw_attitude_neg = ['מתעלם' , 'לא מוטרד' , 'אדיש כלפיו']
  kw_attitude_pos = ['מגן עליו' , 'שומר עליו' , 'מסייע לו']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(   
        template = r"כמה אתה מסכים עם האימרה: כשאני רואה מישהו שמנצלים אותו אני {שאלה}? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Empathic Concern",
                      "Ordinal":9,
                      "Original":'When I see someone being taken advantage of, I feel kind of protective towards them.'
        },
        **kwargs,
    )



class IRIQ14(QCLM):
  kw_attitude_neg = ['מתבאס מ' , 'מוטרד מ']
  kw_attitude_pos = ['אדיש ל' , 'מתעלם מ' ]
  dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}חוסר המזל של אחרים? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Empathic Concern",
                      "Ordinal":14,
                      "Original":"Other people's misfortunes do not usually disturb me a great deal."
        },
        **kwargs,
    )


class IRIQ18(QCLM):
  kw_attitude_neg = ['רחמים' , 'חמלה' ]
  kw_attitude_pos = ['חוסר איכפתיות' , 'ניכור']
  dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)
  def __init__(self, **kwargs):
    super().__init__( 
        template = r"שאלה: באיזה תדירות אתה חש {שאלה} כלפי אדם שמקבל יחס לא הוגן? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Empathic Concern",
                      "Ordinal":18,
                      "Original":"When I see someone being treated unfairly, I sometimes don't feel very much pity for them."
        },
        **kwargs,
    )


class IRIQ20(QCLM):
  kw_attitude_neg = ['אובייקטיבי ל' , 'מנותק מ' , 'אדיש ל']
  kw_attitude_pos = ['מחובר ל' , 'קשור רגשית ב' , 'מעורב רגשית ב']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}דברים שקורים? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Empathic Concern",
                      "Ordinal":20,
                      "Original":'I am often quite touched by things that I see happen.'
        },
        **kwargs,
    )


class IRIQ22(QCLM):
  kw_attitude_neg = ['אטום' , 'נוקשה' , 'חסר רגישות']
  kw_attitude_pos = ['רגיש' , 'פגיע']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"כמה אתה מסכים עם האימרה: אני מתאר את עצמי כאדם {שאלה}? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Empathic Concern",
                      "Ordinal":22,
                      "Original":"I would describe myself as a pretty soft-hearted person."
        },
        **kwargs,
    )


class IRIQ3(QCLM):
  kw_attitude_neg = ['מצליח' , 'חווה הצלחה']
  kw_attitude_pos = ['מתקשה' , 'נתקל בקושי']
  dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה} לראות דברים מנקודת מבטו של האחר? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Perspective Taking",
                      "Ordinal":3,
                      "Original":"I sometimes find it difficult to see things from the other guy's point of view."
        },
        **kwargs,
    )


class IRIQ4(QCLM):
  kw_attitude_neg = ['כאב' , 'צער' , 'סבל' , 'ייסורים']
  kw_attitude_pos = ['שמחה' , 'אושר' , 'שלווה' , 'נחת']
  dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה מרגיש {שאלה} על אנשים אחרים כאשר יש להם בעיות? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Perspective Taking",
                      "Ordinal":4,
                      "Original":"Sometimes I don't feel very sorry for other people when they are having problems."
        },
        **kwargs,
    )


class IRIQ8(QCLM):
  kw_attitude_neg = ['מזניח את ה' , 'מתעלם מ']
  kw_attitude_pos = ['מבין את ה' , 'מתייחס ל']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: כאשר יש אי הסכמה, באיזה תדירות אתה {שאלה}עמדות של כל הצדדים לפני גיבוש דעה? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Perspective Taking",
                      "Ordinal":8,
                      "Original":"I try to look at everybody's side of a disagreement before I make a decision."
        },
        **kwargs,
    )


class IRIQ11(QCLM):
  kw_attitude_neg = ['להתעלם מ' , 'להיות אדיש ל']
  kw_attitude_pos = ['להסתכל מ' , 'לאמץ את ']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"כמה אתה מסכים עם האימרה: כאשר אני רוצה להבין את חבריי, אני מנסה {שאלה}נקודת מבטם? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Perspective Taking",
                      "Ordinal":11,
                      "Original":'I sometimes try to understand my friends better by imagining how things look from their perspective.'
        },
        **kwargs,
    )



class IRIQ15(QCLM):
  kw_attitude_neg = ['מקשיב ל' , 'מתעניין ב' , 'מתייחס ל']
  kw_attitude_pos = ['מתעלם מ' , 'זונח את ']
  dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"כמה אתה מסכים עם האימרה: אם אני בטוח שאני צודק לגבי משהו, אני {שאלה}טיעוניהם של אחרים? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Perspective Taking",
                      "Ordinal":15,
                      "Original":"If I'm sure I'm right about something, I don't waste much time listening to other people's arguments."
        },
        **kwargs,
    )



class IRIQ21(QCLM):
  kw_attitude_neg = ['מתעלם מצד אחד' , 'מתמקד רק בצד אחד' , 'מזניח צד אחד']
  kw_attitude_pos = ['מסתכל על שניהם' , 'בוחן את שני הצדדים' ,  'סוקר את שניהם']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: לכל שאלה שני צדדים, באיזה תדירות אתה {שאלה}? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Perspective Taking",
                      "Ordinal":21,
                      "Original":'I believe that there are two sides to every question and try to look at them both.'
        },
        **kwargs,
    )


class IRIQ25(QCLM):
  kw_attitude_neg = ['אדיש למצבו' , 'לא מנסה להבין אותו']
  kw_attitude_pos = ['שם את עצמי בנעליו' , 'מזדהה עימו']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"עד כמה אתה מסכים עם האימרה: כשאני כועס על מישהו, אני {שאלה}? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Perspective Taking",
                      "Ordinal":25,
                      "Original":"When I'm upset at someone, I usually try to «put myself in his shoes for a while."
        },
        **kwargs,
    )



class IRIQ28(QCLM):
  kw_attitude_neg = ['זונח את מצבו' , 'מתעלם מרגשותיו' ]
  kw_attitude_pos = ['מבין את רגשותיו' , 'שם את עצמך במקומו']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: לפני שאתה מעביר ביקורת על אדם, באיזה תדירות אתה {שאלה}? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Perspective Taking",
                      "Ordinal":28,
                      "Original":'Before criticizing somebody, I try to imagine how I would feel if I were in their place.'
        },
        **kwargs,
    )



class IRIQ6(QCLM):
  kw_attitude_neg = ['שלו' , 'רגוע' , 'נינוח']
  kw_attitude_pos = ['לחוץ' , 'חרד' , 'מתוח']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה מרגיש {שאלה} במצבי חירום? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Personal Distress",
                      "Ordinal":6,
                      "Original":'In emergency situations, I feel apprehensive and ill-at-ease.'
        },
        **kwargs,
    )



class IRIQ10(QCLM):
  kw_attitude_neg = ['בעל יכולת' , 'מסוגלות']
  kw_attitude_pos = ['חסר אונים' , 'אובד עצות']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: כשאתה נמצא במצב מאוד רגיש, באיזה תדירות אתה חש {שאלה}? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Personal Distress",
                      "Ordinal":10,
                      "Original":"I sometimes feel helpless when I am in the middle of a very emotional situation."
        },
        **kwargs,
    )


class IRIQ13(QCLM):
  kw_attitude_neg = ['לחוץ' , 'מתוח' , 'נסער']
  kw_attitude_pos = ['רגוע' , 'שליו']
  dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה}אנשים שבוכים מולך? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Personal Distress",
                      "Ordinal":13,
                      "Original":'When I see someone get hurt, I tend to remain calm..'
        },
        **kwargs,
    )


class IRIQ17(QCLM):
  kw_attitude_neg = ['רגוע' , 'בטוח' , 'שליו']
  kw_attitude_pos = ['מפחד' , 'חושש' , 'חרד']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה {שאלה} כשאתה במצבים מתוחים מבחינה רגשית? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Personal Distress",
                      "Ordinal":17,
                      "Original":'Being in a tense emotional situation scares me.'
        },
        **kwargs,
    )




class IRIQ19(QCLM):
  kw_attitude_neg = ['מתקשה' , 'חסר תועלת' , 'נלחץ']
  kw_attitude_pos = ['יעיל' , 'טוב']
  dict_attitude = dict_pos_neg(kw_attitude_neg, kw_attitude_pos, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"כמה אתה מסכים עם האימרה: אני {שאלה} בהתמודדות עם מצבי חירום? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Personal Distress",
                      "Ordinal":19,
                      "Original":'I am usually pretty effective in dealing with emergencies.'
        },
        **kwargs,
    )




class IRIQ24(QCLM):
  kw_attitude_neg = ['באופן כושל' , 'רע']
  kw_attitude_pos = ['טוב' , 'היטב' , 'כראוי']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"שאלה: באיזה תדירות אתה מתפקד {שאלה} במצבי לחץ? תשובה: {תשובה}",
        dimensions={
                    "תשובה":heb_frequency_weights_1,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Personal Distress",
                      "Ordinal":24,
                      "Original":'I tend to lose control during emergencies.'
        },
        **kwargs,
    )




class IRIQ27(QCLM):
  kw_attitude_neg = ['יציב' , 'חסין']
  kw_attitude_pos = ['נשבר' , 'מתפרק']
  dict_attitude = dict_pos_neg(kw_attitude_pos, kw_attitude_neg, 1.0)
  def __init__(self, **kwargs):
    super().__init__(
        template = r"עד כמה אתה מסכים עם האימרה: כשאני רואה אדם שצריך עזרה בעת מצב חירום, אני {שאלה}? תשובה: {תשובה}",
        dimensions={
                    "תשובה":agreement_weights_he,
                    "שאלה":self.dict_attitude,
        },
        descriptor = {"Questionnair":"IRI",
                      "Factor":"Personal Distress",
                      "Ordinal":27,
                      "Original":'When I see someone who badly needs help in an emergency, I go to pieces.'
        },
        **kwargs,
    )



interpersonal_reactive_index_heb_qclm_list = [IRIQ1, IRIQ2, IRIQ3, IRIQ4, IRIQ5, IRIQ6, IRIQ7, IRIQ8, IRIQ9, IRIQ10, IRIQ11, IRIQ12, IRIQ13, IRIQ14, IRIQ15, IRIQ16, IRIQ17, IRIQ18, IRIQ19, IRIQ20, IRIQ21, IRIQ22, IRIQ23, IRIQ24, IRIQ25, IRIQ26, IRIQ27, IRIQ28]