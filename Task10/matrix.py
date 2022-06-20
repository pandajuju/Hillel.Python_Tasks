from quicksort import quicksort
import random


def generate_matrix(n, m):
    matrix = [[random.randrange(0, 10) for y in range(n)] for x in range(m)]
    return matrix


def sort_matrix(matrix, n):
    sort_mx = [j for i in matrix for j in i]
    quicksort(sort_mx, 0, len(sort_mx)-1)

    return [sort_mx[i:i+n] for i in range(0, len(sort_mx), n)]


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

