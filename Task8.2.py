"""Задача: написати функцію пошуку елемента у послідовності.

   Деталі:
            * функція приймає два аргумента - послідовність та елемен
            * функція повинна повернути індекс елемента у послідовності
              або -1 якщо не знайдено
            * це аналог функції str.find, list.index
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * search_linearly([1, 8, 7, 33, 9, 2], 8) -> повертає 1
            * search_linearly("hello world!", "!") -> повертає 11
            * search_linearly(tuple(range(10)), 10) -> повертає -1
"""
for i in range(5):
    subsequence= input("Введіть послідовність: ")
    element = input("Введите елемент: ")
    def search_linearly(subsequence, element):
        for i in range (len(subsequence)):
            if subsequence[i] == element:
                return i
        return -1
    print(search_linearly(subsequence, element))