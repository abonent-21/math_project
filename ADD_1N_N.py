# ADD_1N_N.py
# Добавление 1 к натуральному числу с сохранением ведущих нулей
# Автор: Самигулин Д.А. Группа - ПМИ-3381

from Types import nat_0

def ADD_1N_N(A: nat_0) -> nat_0:
    """
    Добавляет 1 к натуральному числу A, сохраняя ведущие нули.
    """
    # Копируем массив цифр
    A_digits = A.array.copy()
    original_length = A.n

    index = len(A_digits) - 1
    carry = 1

    # Добавляем 1 с конца
    while index >= 0 and carry:
        total = A_digits[index] + carry
        A_digits[index] = total % 10
        carry = total // 10
        index -= 1

    if carry:
        # Если после цикла остался перенос, добавляем его в начало массива
        A_digits = [carry] + A_digits
        result_len = len(A_digits)
    else:
        # Если переноса нет, длина остается прежней
        result_len = original_length

    return nat_0(A_digits, result_len)
