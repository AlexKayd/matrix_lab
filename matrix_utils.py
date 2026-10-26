"""
Модуль вспомогательных утилит для работы с матрицами:
- построчный ввод матрицы с клавиатуры
- чтение матрицы из файла
- запись матрицы в файл с выравниванием
- красивый вывод матрицы в консоль
"""
from sys import stdin

def read_matrix_from_console():
    """
    Построчный ввод матрицы с клавиатуры.

    Первая строка содержит размеры матрицы n и m.
    Далее идут n строк, каждая содержит по m чисел.

    return: матрица в виде list[list[float]]
    """
    n, m = map(int, stdin.readline().split())

    matrix = []
    for _ in range(n):
        row = list(map(float, stdin.readline().split()))
        if len(row) != m:
            raise ValueError(f"Ожидалось {m} чисел, получено {len(row)}")
        matrix.append(row)

    return matrix

def read_matrix_from_file(filename):
    """
    Чтение матрицы из текстового файла.

    Первая строка содержит размеры матрицы n и m.
    Далее идут n строк, каждая содержит по m чисел.

    return: матрица в виде list[list[float]]
    """
    with open(filename, "r", encoding="utf-8") as file_in:
        first_line = file_in.readline().split()
        if not first_line:
            raise ValueError("Файл пустой.")
            
        n, m = map(int, first_line)

        matrix = []
        for _ in range(n):
            row = list(map(float, file_in.readline().split()))
            if len(row) != m:
                raise ValueError(f"Ожидалось {m} чисел, получено {len(row)}")
            matrix.append(row)

    return matrix

def max_element_lena(matrix):
    """
    Возвращает ширину самого длинного элемента матрицы.
    """
    max_lena = 0
    for row in matrix:
        for elem in row:
            lena = len(str(elem))
            if lena > max_lena:
                max_lena = lena

    return max_lena

def write_matrix_to_file(matrix, filename):
    """
    Запись матрицы в файл с выравниванием столбцов.

    Первая строка файла содержит размеры n, m.
    Далее идут строки матрицы.
    """
    if not matrix or not matrix[0]:
        raise ValueError("Матрица пустая.")

    max_lena = max_element_lena(matrix)

    n = len(matrix)
    m = len(matrix[0])

    with open(filename, "w", encoding="utf-8") as file_out:
        file_out.write(f"{n} {m}\n")

        for row in matrix:
            line = " ".join(f"{elem:>{max_lena}}" for elem in row)
            file_out.write(f"{line}\n")

def print_matrix(matrix):
    """
    Красивый вывод матрицы в консоль с выравниванием по ширине элементов.
    """
    if not matrix or not matrix[0]:
        print("Матрица пустая.")
        return

    max_lena = max_element_lena(matrix)

    for row in matrix:
        line = " ".join(f"{elem:>{max_lena}}" for elem in row)
        print(line)