# ADD_NN_N.py
# Модуль ADD_NN_N
# Сложение натуральных чисел

# Автор: Самигулин Д.А. Группа - ПМИ-3381

from Types import nat_0  # Импортируем nat_0

def ADD_NN_N(A: nat_0, B: nat_0) -> nat_0:
    """
    Суммирует два натуральных числа A и B, представленные в виде объектов nat_0.

    :param A: первое натуральное число (объект nat_0)
    :param B: второе натуральное число (объект nat_0)
    :return: сумма A + B (объект nat_0)
    """
    # Определяем максимальную длину числа для сложения
    max_len = max(A.n, B.n)

    # Выравниваем длины чисел, добавляя ведущие нули к более короткому числу
    a_digits = [0] * (max_len - A.n) + A.array
    b_digits = [0] * (max_len - B.n) + B.array

    result = [0] * max_len  # Список для результата
    carry = 0  # Переменная для переноса

    # Сложение от младших цифр к старшим
    for i in range(max_len - 1, -1, -1):
        total = a_digits[i] + b_digits[i] + carry  # Суммируем соответствующие цифры и перенос
        result[i] = total % 10  # Записываем текущую цифру результата
        carry = total // 10  # Обновляем перенос

    # Если остался перенос, добавляем его в начало результата
    if carry:
        result = [carry] + result
        result_len = max_len + 1
    else:
        result_len = max_len

    # Возвращаем результат в виде объекта nat_0
    return nat_0(result, result_len)
