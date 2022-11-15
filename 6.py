"""Розглянемо завдання на перевірку спаму в електронному листі або фільтрацію 
заборонених слів у повідомленні.

Нехай функція is_spam_words приймає рядок (параметр text), перевіряє його
 на вміст заборонених слів зі списку (параметр spam_words), і 
 повертає результат перевірки: True, якщо є хоч одне слово присутнє 
 зі списку, та False, якщо в тексті стоп-слів не виявлено.

Слова у параметрі text можуть бути у довільному регістрі, а 
значить функція is_spam_words, при пошуку заборонених слів, 
регістру незалежна і весь текст має зводитися до нижнього регістру. 
Для спрощення, будемо вважати, що в рядку є тільки одне заборонене слово.

Передбачити третій параметр функції space_around, який за замовчуванням 
дорівнює False. Він відповідатиме за те, що функція шукатиме окреме слово
 чи ні. Слово вважати, що стоїть окремо, якщо ліворуч від слова знаходиться 
 символ пробілу або воно розташоване на початку тексту, а праворуч від слова 
 знаходиться пробіл або символ крапки.
 space_around=False - не окреме слово
 space_around=True - окреме слово"""


def is_spam_words(text, spam_words, space_around=False):
    result = False
    new_text = text.lower()

    if not space_around:
        for i in spam_words:
            if new_text.find(i.lower()) != -1:
                result = True
    else:
        search_word = []
        first_word = []
        for i in spam_words:
            search_word.append(" " + i.lower() + ".")
            search_word.append(" " + i.lower() + " ")
            search_word.append("." + i.lower() + " ")
            first_word.append(i.lower() + " ")
        for i in search_word:
            if (new_text.find(i) != -1):
                result = True
        for i in first_word:
            if new_text.startswith(i):
                return True

    return result


is_spam_words('Молох бог ужасен.', ['лох'], True)
