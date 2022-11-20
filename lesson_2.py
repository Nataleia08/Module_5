import re


def search_text(word, text, Flag=False):
    result = re.match(word, text)
    return result


print(search_text("The", "The Alise The from "))
