# ADD_1N_N.py
# Модуль ADD_1N_N
# Добавление 1 к натуральному числу

# Автор: Самигулин Д.А. Группа - ПМИ-3381

from Types import nat_0

def ADD_1N_N(A: nat_0) -> nat_0:
    """
    Добавляет 1 к натуральному числу A.

    :param A: натуральное число (объект nat_0)
    :return: новое натуральное число (объект nat_0), равное A + 1
    """
    A_copy = A.copy()  # Создаем копию числа A
    index = A_copy.n - 1  # Индекс последней цифры
    carry = 1  # Начинаем с переноса 1 (т.к. добавляем 1)

    # Проходим по цифрам с конца
    while index >= 0 and carry:
        total = A_copy.array[index] + carry  # Суммируем цифру и перенос
        A_copy.array[index] = total % 10  # Обновляем цифру
        carry = total // 10  # Обновляем перенос
        index -= 1  # Переходим к следующей цифре

    if carry:
        # Если после прохода остался перенос, добавляем его в начало
        A_copy.array = [carry] + A_copy.array
        A_copy.n += 1

    return A_copy  # Возвращаем новое число
