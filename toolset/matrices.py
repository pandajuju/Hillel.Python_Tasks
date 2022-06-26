# from sequences import quicksort
import random

def generate(n, m):
    return [[random.randrange(0, 10) for y in range(n)] for x in range(m)]


def flatten(r):
    return [j for i in r for j in i]


def sort(r):
    quicksort(r, 0, len(r)-1)
    return r


def roll(r, m, n):
    return [r[i:i + n] for i in range(m, len(r), n)]


