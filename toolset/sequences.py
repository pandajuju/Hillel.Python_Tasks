import random as rand


def count(seq, element):
    return seq.count(element)


def random(N, a, b):
    return [rand.randrange(a, b) for i in range(N)]


def bubble(N):
    for i in range(len(N) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if alist[j + 1] < alist[j]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                no_swap = False
        if no_swap:
            return


def quicksort(seq, i, j):

    if i >= j:
        return
    pivot = i

    for _ in range(i + 1, j + 1):
        if seq[_] < seq[i]:
            pivot += 1
            seq[_], seq[pivot] = seq[pivot], seq[_]
    seq[i], seq[pivot] = seq[pivot], seq[i]
    quicksort(seq, i, pivot-1)
    quicksort(seq, pivot+1, j)


def letter_stats(seq, letter):
    text_split = seq.split()
    char_dict = {}
    char_count = 0

    for w in text_split:
        char_count += len(w)

        for c in w:
            count_char = char_dict.get(c, 0)
            char_dict[c] = count_char + 1

    if letter != 0:
        return round((char_dict.get(letter) / len(char_dict)) * 100, 2)
    else:
        statistic_dict = {}
        for char in char_dict:
            statistic_dict[char] = round((char_dict.get(char) / len(char_dict)) * 100, 2)
        return statistic_dict


def word_stats(seq, word):
    text_split = seq.split()
    word_dict = {}

    for w in text_split:
        count_word = word_dict.get(w, 0)
        word_dict[w] = count_word + 1
    if word != 0:
        return {word: round((word_dict.get(word) / len(word_dict)) * 100, 2) }
    else:
        statistic_dict = {}
        for w in word_dict:
            statistic_dict[w] = round((word_dict.get(w) / len(word_dict)) * 100, 2)
        return statistic_dict


def search_linearly(seq, element):
    for i in range (len(seq)):
        if seq[i] == element:
            return i
    return -1


def binary_search(seq, element):
    mid = 0
    start = 0
    end = len(seq)
    step = 0

    while (start <= end):
        step = step + 1
        mid = (start + end) // 2

        if element == seq[mid]:
            return mid

        if element < seq[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

