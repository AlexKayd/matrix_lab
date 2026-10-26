"""
Модуль декораторов для матричных операций:
- замера времени выполнения функции (@timer)
- проверки матрицы на квадратность перед выполнением (@validate_square)
"""

import time


def timer(f):
    """
    Декоратор, принимает функцию f как аргумент.
    """
    def decorated(*args, **kwargs):
        """
        Замеряет время выполнения функции и выводит его в консоль.
        """
        start = time.perf_counter()
        res = f(*args, **kwargs)
        end = time.perf_counter()

        exec_time = end - start
        print(f"Время выполнения: {exec_time:.6f} сек")

        return res

    return decorated


def validate_square(f):
    """
    Декоратор, принимает функцию f как аргумент.
    """
    def decorated(*args, **kwargs):
        """
        Проверяет, что первый аргумент - квадратная матрица.
        Если нет - выбрасывает ValueError до вызова функции.
        """
        if args:
            matrix = args[0]
        elif "matrix" in kwargs:
            matrix = kwargs["matrix"]
        else:
            raise ValueError("Функция должна принимать матрицу.")
        
        if not matrix or not matrix[0]:
            raise ValueError("Матрица пустая.")

        n = len(matrix)
        m = len(matrix[0])

        if n != m:
            raise ValueError(f"Матрица не квадратная: {n}x{m}")

        return f(*args, **kwargs)

    return decorated
