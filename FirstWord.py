""" Дана строка и нужно найти ее первое слово. 

    При решении задачи обратите внимание на следующие моменты:
        В строке могут встречатся точки и запятые
        Строка может начинаться с буквы или, к примеру, с пробела или точки
        В слове может быть апостроф и он является частью слова
        Весь текст может быть представлен только одним словом и все
"""


def first_word(source: str) -> str:
    ret = source.replace(',', ' ').replace('.', ' ').split()
    return ret[0] if len(ret) else ''
