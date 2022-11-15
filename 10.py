import re


def find_word(text, word):
    result = re.search(word, text)
    if result:
        result_dict = {
            'result': True,
            'first_index': result.span()[0],
            'last_index': result.span()[1],
            'search_string': result.group(),
            'string': result.string
        }
    else:
        result_dict = {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        }
    return result_dict
