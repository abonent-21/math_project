# LCM_NN_N.py
# НОК натуральных чисел
# Автор: Бескончин М.А. Группа - ПМИ-3381

from Types import nat_0
from NZER_N_B import NZER_N_B
from DIV_NN_N import DIV_NN_N
from MUL_NN_N import MUL_NN_N
from GCF_NN_N import GCF_NN_N


def LCM_NN_N(A: nat_0, B: nat_0) -> nat_0:
    """
    Вычисляет наименьшее общее кратное (НОК) двух натуральных чисел A и B.

    :param A: Первое натуральное число, тип nat_0
    :param B: Второе натуральное число, тип nat_0
    :return: НОК чисел A и B, тип nat_0
    :raises ValueError: Если оба числа A и B равны нулю
    """
    # Если оба числа равны нулю, НОК не определен
    if NZER_N_B(A) == 0 and NZER_N_B(B) == 0:
        raise ValueError("НОК (0,0) - не определен")

    # Если одно из чисел равно нулю, НОК равен нулю
    if not NZER_N_B(A):
        return nat_0([0], 1)
    if not NZER_N_B(B):
        return nat_0([0], 1)

    # Создаем глубокие копии чисел, чтобы избежать изменения исходных данных
    num1 = A.copy()
    num2 = B.copy()

    # Вычисляем НОК по формуле: НОК(A, B) = (A * B) / НОД(A, B)
    zn = MUL_NN_N(num1, num2)
    ll = GCF_NN_N(num1, num2)
    return DIV_NN_N(zn, ll)