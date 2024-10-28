# ADD_NN_N.py
# Сложение натуральных чисел
# Автор: Самигулин Д.А. Группа - ПМИ-3381

from Types import nat_0

def ADD_NN_N(A: nat_0, B: nat_0) -> nat_0:
    """
    Суммирует два натуральных числа A и B, представленные в виде объектов nat_0.
    """
    # Выравниваем длины чисел, добавляя ведущие нули к более короткому числу
    max_len = max(A.n, B.n)
    A_digits = [0]*(max_len - A.n) + A.array.copy()
    B_digits = [0]*(max_len - B.n) + B.array.copy()

    result = [0] * (max_len + 1)  # +1 для возможного переноса
    carry = 0  # Переменная для переноса

    # Сложение с конца
    for i in range(max_len - 1, -1, -1):
        total = A_digits[i] + B_digits[i] + carry
        result[i+1] = total % 10
        carry = total // 10

    # Обработка возможного переноса в самый старший разряд
    if carry:
        result[0] = carry
        result_len = max_len + 1
    else:
        result = result[1:]  # Удаляем незначащий ноль
        result_len = max_len

    return nat_0(result, result_len)
