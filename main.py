"""
Главный модуль программы.
Реализует интерактивное меню для работы с матрицами.
"""

from matrix_utils import (
    read_matrix_from_console,
    read_matrix_from_file,
    write_matrix_to_file,
    print_matrix
)
from matrix_ops import (
    transpose,
    multiply,
    determinant,
    power,
    apply_to_matrix,
    get_stats,
    min_max_positions,
    matrix_stats
)
from matrix_io import diagonal, spiral
from decorators import timer, validate_square


@timer
def determinant_with_timer(matrix):
    """
    Вычисление определителя с замером времени.
    """
    return determinant(matrix)


@validate_square
def power_validated(matrix, k, **kwargs):
    """
    Возведение в степень с проверкой на квадратность матрицы.
    """
    return power(matrix, k, **kwargs)


def main():
    """
    Реализует интерактивное меню.
    """
    matrix = None

    while True:
        print("\n")
        print("-" * 50)
        print(f"МЕНЮ РАБОТЫ С МАТРИЦАМИ (операций выполнено: {get_stats()})")
        print("1. Ввести матрицу с клавиатуры")
        print("2. Загрузить матрицу из файла")
        print("3. Транспонировать текущую матрицу (выбор способа: циклы / списочное выражение)")
        print("4. Умножить две матрицы")
        print("5. Возвести матрицу в степень k")
        print("6. Найти определитель")
        print("7. Вывести элементы главной диагонали")
        print("8. Вывести матрицу по спирали")
        print("9. Сохранить результат в файл")
        print("10. Выход")
        print("11. Применить произвольную функцию к каждому элементу (возведение в квадрат / замена отрицательных значений на 0)")
        print("12. Показать статистику матрицы")
        print("13. Показать позиции минимума и максимума")
        print("-" * 50)

        try:
            choice = int(input("Введите пункт меню: "))
        except ValueError:
            print("Ошибка: введите число от 1 до 13.")
            continue

        if choice == 1:
            try:
                matrix = read_matrix_from_console()
                print("\nВведенная матрица:")
                print_matrix(matrix)

            except ValueError as e:
                print(f"Ошибка ввода: {e}")

        elif choice == 2:
            try:
                filename = input("Введите имя файла (например, data/input.txt): ")
                matrix = read_matrix_from_file(filename)
                print("\nЗагруженная матрица:")
                print_matrix(matrix)

            except FileNotFoundError:
                print(f"Ошибка: файл '{filename}' не найден.")

            except ValueError as e:
                print(f"Ошибка чтения файла: {e}")

        elif choice == 3:
            if not matrix:
                print("Ошибка: сначала загрузите или введите матрицу.")
                continue
            else:
                print("\nТекущая матрица:")
                print_matrix(matrix)

            print("\nВыберите способ транспонирования:")
            print("1. Через вложенные циклы")
            print("2. Через списочное выражение")

            try:
                variant = int(input("Введите номер способа: "))

                if variant not in [1, 2]:
                    print("Ошибка: введите 1 или 2.")
                    continue

                res_one, res_two = transpose(matrix)

                if variant == 1:
                    print("\nРезультат (через циклы):")
                    print_matrix(res_one)
                    matrix = res_one
                else:
                    print("\nРезультат (через списочное выражение):")
                    print_matrix(res_two)
                    matrix = res_two

            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 4:
            if not matrix:
                print("Ошибка: сначала загрузите или введите первую матрицу.")
                continue
            else:
                print("\nПервая матрица:")
                print_matrix(matrix)

            try:
                print("\nВведите вторую матрицу:")
                second_matrix = read_matrix_from_console()

                res = multiply(matrix, second_matrix)
                print("\nРезультат умножения:")
                print_matrix(res)
                matrix = res

            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 5:
            if not matrix:
                print("Ошибка: сначала загрузите или введите матрицу.")
                continue
            else:
                print("\nТекущая матрица:")
                print_matrix(matrix)

            try:
                k = int(input("Введите натуральную степень k: "))
                if k < 1:
                    print("Ошибка: степень должна быть натуральным числом.")
                    continue

                mod_input = input("Введите модуль (Enter — без модуля): ").strip()
                if mod_input:
                    mod = int(mod_input)
                    result = power_validated(matrix, k, mod=mod)
                else:
                    result = power_validated(matrix, k)

                print("\nРезультат возведения в степень:")
                print_matrix(result)
                matrix = result

            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 6:
            if not matrix:
                print("Ошибка: сначала загрузите или введите матрицу.")
                continue
            else:
                print("\nТекущая матрица:")
                print_matrix(matrix)

            try:
                det = determinant_with_timer(matrix)
                print(f"Определитель матрицы: {det}")

            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 7:
            if not matrix:
                print("Ошибка: сначала загрузите или введите матрицу.")
                continue
            else:
                print("\nТекущая матрица:")
                print_matrix(matrix)

            print("\nЭлементы главной диагонали:")
            diag_res = list(diagonal(matrix))
            print(", ".join(str(elem) for elem in diag_res))

        elif choice == 8:
            if not matrix:
                print("Ошибка: сначала загрузите или введите матрицу.")
                continue
            else:
                print("\nТекущая матрица:")
                print_matrix(matrix)

            print("\nЭлементы матрицы по спирали:")
            spiral_res = list(spiral(matrix))
            print(", ".join(str(elem) for elem in spiral_res))

        elif choice == 9:
            if not matrix:
                print("Ошибка: сначала загрузите или введите матрицу.")
                continue
            else:
                print("\nТекущая матрица:")
                print_matrix(matrix)

            try:
                filename = input("Введите имя файла для сохранения (например, data/output.txt): ")
                write_matrix_to_file(matrix, filename)
                print(f"Матрица успешно сохранена в файл '{filename}'.")

            except ValueError as e:
                print(f"Ошибка записи: {e}")

        elif choice == 10:
            print("Выход.")
            break

        elif choice == 11:
            if not matrix:
                print("Ошибка: сначала загрузите матрицу.")
                continue
            else:
                print("\nТекущая матрица:")
                print_matrix(matrix)

            print("\nВыберите действие с матрицей:")
            print("1. Возведение в квадрат (lambda x: x ** 2)")
            print("2. Замена отрицательных значений на 0 (lambda x: x if x > 0 else 0)")

            try:
                variant = int(input("Выберите действие: "))
                if variant == 1:
                    res = apply_to_matrix(matrix, lambda x: x ** 2)
                elif variant == 2:
                    res = apply_to_matrix(matrix, lambda x: x if x > 0 else 0)
                else:
                    print("Ошибка: введите 1 или 2.")
                    continue

                print("\nРезультат:")
                print_matrix(res)
                matrix = res

            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 12:
            if not matrix:
                print("Ошибка: сначала загрузите матрицу.")
                continue
            else:
                print("\nТекущая матрица:")
                print_matrix(matrix)

            stats = matrix_stats(matrix)
            print("\nСтатистика матрицы:")
            print(f"min = {stats['min']}")
            print(f"max = {stats['max']}")
            print(f"sum = {stats['sum']}")
            print(f"unique_count = {stats['unique_count']}")
            print(f"most_common = {stats['most_common']}")

        elif choice == 13:
            if not matrix:
                print("Ошибка: сначала загрузите матрицу.")
                continue
            else:
                print("\nТекущая матрица:")
                print_matrix(matrix)

            min_pos, max_pos = min_max_positions(matrix)
            print(f"\nПозиция минимума: {min_pos}")
            print(f"Позиция максимума: {max_pos}")

        else:
            print("Ошибка: введите число от 1 до 13.")


if __name__ == "__main__":
    main()
