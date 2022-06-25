"""Завдання: написати програму яка будет використовувати пакет створений у попередньому завданні.

Написати top-level Пайтон скрипт який буде використовувати будь-яку функцію з пакету.

Наприклад: запитати число у корисувача та вивести послідовність n за допомогою fizzbuzz(n)

    n = int(input())
    for el in fun.fizzbuzz(n):
        print(el)

"""

from toolset import sequences

seq = input('Введіть текст: ')
statistic = sequences.word_stats(seq, 0)
for word in statistic:
    print(f" '{word}': {statistic.get(word)} %")