""" Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми. В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова. Все строки даны в нижнем регистре.

Входные данные: Последовательность строк.

Выходные данные: Текст, как строка.

"""


def left_join(src: tuple) -> str:
    return ','.join([s.replace('right', 'left') for s in src])

