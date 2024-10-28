# NZER_N_B.py
# Проверка на неравенство нулю
# Автор: Самигулин Д.А. Группа - ПМИ-3381

from Types import nat_0

def NZER_N_B(A: nat_0) -> bool:
    """
    Проверяет, является ли натуральное число A ненулевым.
    Возвращает True, если A != 0, иначе False.
    """
    # Удаляем ведущие нули
    A_digits = A.array.copy()
    while len(A_digits) > 1 and A_digits[0] == 0:
        A_digits.pop(0)

    # Проверяем, равно ли число нулю
    return not (len(A_digits) == 1 and A_digits[0] == 0)
