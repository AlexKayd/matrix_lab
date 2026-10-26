"""
Модуль операций над матрицами:
- транспонирование матрицы (2 способа)
- умножение двух матриц
- поэлементное сложение матриц
- поэлементное вычитание матриц
- умножение матрицы на скаляр
- вычисление определителя квадратной матрицы
- создание единичной матрицы
- возведение матрицы в натуральную степень
"""

OPS_COUNT = 0


def check_not_empty(matrix):
    """
    Вспомогательная функция для проверки матрицы на пустоту.
    """
    if not matrix or not matrix[0]:
        raise ValueError("Матрица пустая.")


def increment_ops():
    """
    Вспомогательная функция для счета количества операций.
    """
    global OPS_COUNT
    OPS_COUNT += 1


def get_stats():
    """
    Возвращает количество выполненных операций.

    return: количество операций
    """
    return OPS_COUNT


def transpose(matrix):
    """
    Транспонирование матрицы двумя способами:
    - через вложенные циклы.
    - через списочное выражение.
    Результаты сравниваются.

    return: кортеж из двух транспонированных матриц
    """
    check_not_empty(matrix)
    increment_ops()

    n = len(matrix)
    m = len(matrix[0])

    # Способ 1
    res_one = []
    for i in range(m):
        new_row = []
        for j in range(n):
            new_row.append(matrix[j][i])
        res_one.append(new_row)

    # Способ 2
    res_two = [[matrix[i][j] for i in range(n)] for j in range(m)]

    if res_one == res_two:
        print("Результаты транспонирования совпадают.")
    else:
        print("Результаты транспонирования различаются.")

    return res_one, res_two


def multiply(a, b):
    """
    Умножение двух матриц.
    Проверяется совместимость размеров.

    return: результат умножения list[list[int | float]]
    """
    if not a or not a[0] or not b or not b[0]:
        raise ValueError("Одна из матриц пустая.")

    n = len(a)
    m = len(a[0])
    n2 = len(b)
    m2 = len(b[0])

    if m != n2:
        raise ValueError(f"Матрицы несовместимы: {n}x{m} и {n2}x{m2}")

    increment_ops()

    res = []
    for i in range(n):
        new_row = []
        for j in range(m2):
            elem_sum = 0
            for k in range(m):
                elem_sum += a[i][k] * b[k][j]
            new_row.append(elem_sum)
        res.append(new_row)

    return res


def add(a, b):
    """
    Поэлементное сложение двух матриц.
    Проверяются размеры матриц.

    return: результат сложения list[list[int | float]]
    """
    if not a or not a[0] or not b or not b[0]:
        raise ValueError("Одна из матриц пустая.")

    n = len(a)
    m = len(a[0])
    n2 = len(b)
    m2 = len(b[0])

    if n2 != n or m2 != m:
        raise ValueError(f"Размеры не совпадают: {n}x{m} и {n2}x{m2}")

    increment_ops()

    res = []
    for i in range(n):
        new_row = []
        for j in range(m):
            new_row.append(a[i][j] + b[i][j])
        res.append(new_row)

    return res


def subtract(a, b):
    """
    Поэлементное вычитание двух матриц.
    Проверяются размеры матриц.

    return: результат вычитания list[list[int | float]]
    """
    if not a or not a[0] or not b or not b[0]:
        raise ValueError("Одна из матриц пустая.")

    n = len(a)
    m = len(a[0])
    n2 = len(b)
    m2 = len(b[0])

    if n2 != n or m2 != m:
        raise ValueError(f"Размеры не совпадают: {n}x{m} и {n2}x{m2}")

    increment_ops()

    res = []
    for i in range(n):
        new_row = []
        for j in range(m):
            new_row.append(a[i][j] - b[i][j])
        res.append(new_row)

    return res


def scalar_multiply(matrix, k):
    """
    Умножение матрицы на скаляр.

    return: результат умножения list[list[int | float]]
    """
    check_not_empty(matrix)
    increment_ops()

    res = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(elem * k)
        res.append(new_row)

    return res


def determinant_recursive(matrix):
    """
    Рекурсивное вычисление определителя через разложение по первой строке.
    """
    n = len(matrix)

    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            minor = []
            for j in range(1, n):
                minor_row = []
                for k in range(n):
                    if k != i:
                        minor_row.append(matrix[j][k])
                minor.append(minor_row)

            sign = (-1) ** i
            det += sign * matrix[0][i] * determinant_recursive(minor)

        return det


def determinant(matrix):
    """
    Вычисление определителя квадратной матрицы рекурсивно (метод миноров).
    Для матриц 1х1 и 2x2 - базовые случаи.

    return: определитель, float
    """
    check_not_empty(matrix)

    n = len(matrix)
    m = len(matrix[0])

    if n != m:
        raise ValueError(f"Матрица не квадратная: {n}x{m}")

    increment_ops()

    return float(determinant_recursive(matrix))


def identity(n):
    """
    Создание единичной матрицы размера n x n.

    return: единичная матрица list[list[int | float]]
    """
    if n <= 0:
        raise ValueError("Размер должен быть положительным.")

    increment_ops()

    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def power_recursive(matrix, k):
    """
    Быстрое возведение в степень.
    """
    if k == 1:
        return [row[:] for row in matrix]

    half = power_recursive(matrix, k // 2)
    half_squared = multiply(half, half)

    if k % 2 == 0:
        return half_squared
    
    return multiply(half_squared, matrix)


def power(matrix, k, *, mod=None):
    """
    Возведение квадратной матрицы в натуральную степень k
    через быстрое возведение в степень (рекурсивно).
    При передаче mod результат берётся по модулю.

    return: результат возведения в степень list[list[int | float]]
    """
    check_not_empty(matrix)

    n = len(matrix)
    m = len(matrix[0])

    if n != m:
        raise ValueError(f"Матрица не квадратная: {n}x{m}")

    if k < 1:
        raise ValueError("Степень должна быть натуральной.")

    res = power_recursive(matrix, k)

    if mod is not None:
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = res[i][j] % mod

    increment_ops()

    return res


def apply_to_matrix(matrix, func):
    """
    Применение произвольной функции к каждому элементу матрицы.

    return: новая матрица с примененной функцией list[list[int | float]]
    """
    check_not_empty(matrix)
    increment_ops()

    res = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(func(elem))
        res.append(new_row)

    return res


def matrix_stats(matrix) -> dict:
    """
    Вычисление статистики матрицы.

    Возвращает словарь со статистикой:
    - min: минимальный элемент
    - max: максимальный элемент
    - sum: сумма всех элементов
    - unique_count: число уникальных элементов
    - most_common: самый частый элемент

    return: словарь со статистикой
    """
    check_not_empty(matrix)
    increment_ops()

    all_elem = []
    for row in matrix:
        for elem in row:
            all_elem.append(elem)

    min_val = min(all_elem)
    max_val = max(all_elem)
    sum_val = sum(all_elem)

    unique_elem = set(all_elem)
    unique_count = len(unique_elem)

    counts = {}
    for elem in all_elem:
        counts[elem] = counts.get(elem, 0) + 1

    most_common = max(counts, key=counts.get)

    return {
        "min": min_val,
        "max": max_val,
        "sum": sum_val,
        "unique_count": unique_count,
        "most_common": most_common
    }


def min_max_positions(matrix) -> tuple:
    """
    Нахождение позиций минимального и максимального элементов матрицы.

    return: кортеж позиций минимума и максимума
    """
    check_not_empty(matrix)
    increment_ops()

    n = len(matrix)
    m = len(matrix[0])

    min_val = matrix[0][0]
    max_val = matrix[0][0]
    min_pos = (0, 0)
    max_pos = (0, 0)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_pos = (i, j)
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_pos = (i, j)

    return (min_pos, max_pos)
