# MOD_NN_N.py
# Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля)
# Автор: Бескончин М.А. Группа - ПМИ-3381

from Types import nat_0
from COM_NN_D import COM_NN_D
from DIV_NN_N import DIV_NN_N
from SUB_NN_N import SUB_NN_N
from MUL_NN_N import MUL_NN_N
from NZER_N_B import NZER_N_B

def MOD_NN_N(A: nat_0, B: nat_0) -> nat_0:
    """
    Вычисляет остаток от деления натурального числа A на натуральное число B.

    :param A: Делимое, тип nat_0
    :param B: Делитель, тип nat_0 (должен быть ненулевым)
    :return: Остаток от деления A на B, тип nat_0
    :raises ValueError: Если делитель B равен нулю
    """
    # Проверка на деление на ноль
    if not NZER_N_B(B):
        raise ValueError("Делитель не может быть нулем")

    # Проверка, чтобы A было больше или равно B
    if COM_NN_D(A, B).value == 1:
        return A.copy()
    elif COM_NN_D(A, B).value == 0:
        return nat_0([0], 1)

    num1 = A.copy()
    num2 = B.copy()

    integer = DIV_NN_N(num1, num2) # Вычисляем целую часть деления
    # Вычисляем остаток: A - (integer * B)
    result = SUB_NN_N(num1, MUL_NN_N(integer, num2))

    return result
