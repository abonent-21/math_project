# DIV_NN_N.py
# Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен от нуля)
# Автор: Бескончин М.А. Группа - ПМИ-3381

from Types import nat_0
from COM_NN_D import COM_NN_D
from DIV_NN_Dk import DIV_NN_Dk
from SUB_NN_N import SUB_NN_N
from ADD_NN_N import ADD_NN_N
from MUL_NN_N import MUL_NN_N
from NZER_N_B import NZER_N_B

def DIV_NN_N(A: nat_0, B: nat_0) -> nat_0:
    """
    Вычисляет частное от деления натурального числа A на натуральное число B.

    :param A: Делимое, тип nat_0
    :param B: Делитель, тип nat_0 (должен быть ненулевым)
    :return: Частное от деления A на B, тип nat_0
    :raises ValueError: Если делитель B равен нулю
    """
    # Проверка на деление на ноль
    if not NZER_N_B(B):
        raise ValueError("Делитель не может быть нулем")

    if COM_NN_D(A, B).value == 0:
        return nat_0([1], 1)  #
    elif COM_NN_D(A, B).value == 1:
        return nat_0([0], 1)  # Проверка, чтобы A было больше или равно B

    result = nat_0([0], 1)  # Инициализация результата с нулевым значением
    num1 = A.copy()
    num2 = B.copy()

    while NZER_N_B(num1) and COM_NN_D(num1, num2).value != 1:  # Пока num1 >= num2
        quotient = DIV_NN_Dk(num1, num2)  # Деление на первую цифру

        # num1 = num1 - num2 * quotient
        num1 = SUB_NN_N(num1, MUL_NN_N(num2, quotient))

        # result = result + quotient
        result = ADD_NN_N(result, quotient)


    return result



