# COM_NN_D.py
# Сравнение натуральных чисел: A ? B
# Автор: Самигулин Д.А. Группа - ПМИ-3381

from Types import nat_0

def COM_NN_D(A: nat_0, B: nat_0) -> int:
    """
    Сравнивает два натуральных числа A и B в структуре nat_0.
    Возвращает:
    - 2, если A > B
    - 0, если A == B
    - 1, если A < B
    """
    # Удаляем ведущие нули для сравнения
    A_digits = A.array.copy()
    B_digits = B.array.copy()

    while len(A_digits) > 1 and A_digits[0] == 0:
        A_digits.pop(0)
    while len(B_digits) > 1 and B_digits[0] == 0:
        B_digits.pop(0)

    # Сравниваем длины
    if len(A_digits) > len(B_digits):
        return 2
    elif len(A_digits) < len(B_digits):
        return 1

    # Сравниваем цифры
    for a_digit, b_digit in zip(A_digits, B_digits):
        if a_digit > b_digit:
            return 2
        elif a_digit < b_digit:
            return 1
    return 0
