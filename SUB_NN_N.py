# SUB_NN_N.py
# Вычитание натуральных чисел (A >= B)
# Автор: Самигулин Д.А. Группа - ПМИ-3381

from COM_NN_D import COM_NN_D
from Types import nat_0

def SUB_NN_N(A: nat_0, B: nat_0) -> nat_0:
    """
    Вычитает из натурального числа A натуральное число B (A >= B).
    Сохраняет ведущие нули в результате.
    """
    # Копируем массивы цифр
    A_digits = A.array.copy()
    B_digits = B.array.copy()

    # Удаляем ведущие нули только для сравнения
    A_digits_cmp = A_digits.copy()
    B_digits_cmp = B_digits.copy()

    while len(A_digits_cmp) > 1 and A_digits_cmp[0] == 0:
        A_digits_cmp.pop(0)
    while len(B_digits_cmp) > 1 and B_digits_cmp[0] == 0:
        B_digits_cmp.pop(0)

    # Проверяем, что A >= B после удаления ведущих нулей
    temp_A = nat_0(A_digits_cmp, len(A_digits_cmp))
    temp_B = nat_0(B_digits_cmp, len(B_digits_cmp))
    if COM_NN_D(temp_A, temp_B) == 1:
        raise ValueError("Первое число должно быть больше или равно второму")

    # Выравниваем длины чисел без удаления ведущих нулей
    max_len = max(len(A_digits), len(B_digits))
    A_digits = [0]*(max_len - len(A_digits)) + A_digits
    B_digits = [0]*(max_len - len(B_digits)) + B_digits

    result_digits = [0]*max_len
    borrow = 0

    # Вычитание с конца, учитывая ведущие нули
    for i in range(max_len - 1, -1, -1):
        diff = A_digits[i] - B_digits[i] - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result_digits[i] = diff

    # Если результат ноль, возвращаем nat_0([0], 1)
    if all(d == 0 for d in result_digits):
        return nat_0([0], 1)

    # Возвращаем результат с сохранением ведущих нулей
    result_len = len(result_digits)
    return nat_0(result_digits, result_len)
