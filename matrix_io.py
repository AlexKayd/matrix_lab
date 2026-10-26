"""
Модуль генераторов для работы с матрицами:
- обход .txt файлов с матрицами в папке
- разворачивание матрицы в плоскую последовательность
- получение элементов главной диагонали
- обход матрицы по спирали
"""

import os
from matrix_utils import read_matrix_from_file


def matrices_generator(folder):
    """
    Генератор, который обходит все .txt-файлы в указанной папке  
    и по очереди возвращает прочитанные из них матрицы.

    yield: матрица list[list[int | float]]
    """
    files = os.listdir(folder)

    for filename in files:
        if filename.endswith(".txt"):
            filepath = os.path.join(folder, filename)

            matrix = read_matrix_from_file(filepath)
            yield matrix


def flatten(matrix):
    """
    Генератор, разворачивающий матрицу в плоскую последовательность элементов.

    yield: элементы матрицы построчно, слева направо
    """
    for row in matrix:
        for elem in row:
            yield elem


def diagonal(matrix):
    """
    Генератор, возвращающий элементы главной диагонали матрицы.

    yield: элементы главной диагонали
    """
    if not matrix or not matrix[0]:
        return

    n = len(matrix)
    m = len(matrix[0])
    min_size = min(n, m)

    for i in range(min_size):
        yield matrix[i][i]


def spiral(matrix):
    """
    Генератор, обходящий матрицу по спирали по часовой стрелке,
    начиная с левого верхнего угла.

    yield: элементы матрицы в порядке обхода по спирали
    """
    if not matrix or not matrix[0]:
        return

    top = 0
    down = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= down and left <= right:
        for j in range(left, right + 1):
            yield matrix[top][j]
        top += 1

        for i in range(top, down + 1):
            yield matrix[i][right]
        right -= 1

        if top <= down:
            for j in range(right, left - 1, -1):
                yield matrix[down][j]
            down -= 1

        if left <= right:
            for i in range(down, top - 1, -1):
                yield matrix[i][left]
            left += 1
