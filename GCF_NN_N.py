# GCF_NN_N.py
# НОД натуральных чисел
# Автор: Бескончин М.А. Группа - ПМИ-3381

from Types import nat_0
from NZER_N_B import NZER_N_B
from COM_NN_D import COM_NN_D
from MOD_NN_N import MOD_NN_N

def GCF_NN_N(A: nat_0, B: nat_0) -> nat_0:
    """
    Вычисляет наибольший общий делитель (НОД) двух натуральных чисел A и B.

    :param A: Первое натуральное число, тип nat_0
    :param B: Второе натуральное число, тип nat_0
    :return: НОД чисел A и B, тип nat_0
    :raises ValueError: Если оба числа A и B равны нулю
    """
    #Проверка на ноль
    if NZER_N_B(A) == 0 and NZER_N_B(B) == 0:
        raise ValueError("НОД (0,0) - не определен")
    #Если А = 0, то НОД = B, аналогично и для B
    if not(NZER_N_B(A)):
        return B.copy()
    elif not(NZER_N_B(B)):
        return A.copy()

    num1 = A.copy()
    num2 = B.copy()

    #Вычисления НОД с помощью алгоритма Евклида
    #Пока любое из чисел не станет равным нулю
    while NZER_N_B(num1) and NZER_N_B(num2):
        # Большее число равняется остатку от деления большего числа на меньшее
        if COM_NN_D(num1, num2).value == 2:
            num1 = MOD_NN_N(num1, num2)
        else:
            num2 = MOD_NN_N(num2, num1)

    # НОД равняется не нулевому значению
    if NZER_N_B(num1):
        return num1
    else:
        return num2