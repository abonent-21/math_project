# DIV_NN_N.py
# Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен от нуля)
# Автор: Бескончин М.А. Группа - ПМИ-3381

from Types import nat_0
import COM_NN_D
import DIV_NN_Dk
import SUB_NDN_N
import ADD_NN_N


def DIV_NN_N(A: nat_0, B: nat_0) -> nat_0:
    # Проверка на деление на ноль
    if B.array == [0]:
        raise ValueError("Делитель не может быть нулем")

    # Проверка, чтобы A было больше или равно B
    if COM_NN_D(A, B) == 1:
        raise ValueError("2 число больше 1")

    result = nat_0([0], 1)  # Инициализация результата с нулевым значением
    num1 = A.copy()  # Создание копии числа A
    num2 = B.copy()  # Создание копии числа B

    while (num1.array != [0]) and (COM_NN_D(num1, num2) in [2, 0]):  # Пока num1 >= num2
        quotient = DIV_NN_Dk(num1, num2)  # Деление на первую цифру

        # num1 = num1 - num2 * quotient
        num1 = SUB_NDN_N(num1, num2, quotient)

        # result = result + quotient
        result = ADD_NN_N(result, quotient)

    return result



