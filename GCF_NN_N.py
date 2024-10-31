# GCF_NN_N.py
# НОД натуральных чисел
# Автор: Бескончин М.А. Группа - ПМИ-3381


from Types import nat_0
import NZER_N_B
import COM_NN_D
import MOD_NN_N


def GCF_NN_N(A: nat_0, B: nat_0) -> nat_0:
    if not(NZER_N_B(A) or NZER_N_B(B)):
        return nat_0([0], 1)
    num1 = A.copy()  # Создание копии числа A
    num2 = B.copy()  # Создание копии числа B

    while(NZER_N_B(num1) and NZER_N_B(num2)):
        if COM_NN_D(num1, num2):
            num1 = MOD_NN_N(num1, num2)
        else:
            num2 = MOD_NN_N(num2, num1)
    if NZER_N_B(num1):
        return num1
    else:
        return num2

