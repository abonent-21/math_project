# LCM_NN_N.py
# НОК натуральных чисел
# Автор: Бескончин М.А. Группа - ПМИ-3381


from Types import nat_0
import NZER_N_B
import DIV_NN_N
import MUL_NN_N

def GCF_NN_N(A: nat_0, B: nat_0) -> nat_0:
    if not(NZER_N_B(A) or NZER_N_B(B)):
        return nat_0([0], 1)
    num1 = A.copy()  # Создание копии числа A
    num2 = B.copy()  # Создание копии числа B

    return DIV_NN_N(MUL_NN_N(num1,num2),GCF_NN_N(num1,num2))