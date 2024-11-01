# MUL_ZZ_Z.py
# Умножение целых чисел.
# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import ceil
from POZ_Z_D import POZ_Z_D
from ABS_Z_Z import ABS_Z_Z
from TRANS_Z_N import TRANS_Z_N
from MUL_NN_N import MUL_NN_N
from TRANS_N_Z import TRANS_N_Z
from MUL_ZM_Z import MUL_ZM_Z


def MUL_ZZ_Z(a: ceil, b: ceil) -> ceil:
    # Проверка, является ли какой-то из множителей нулем.
    if POZ_Z_D(a) == 0 or POZ_Z_D(b) == 0: 
        return ceil([0], 1, 0) 
    
    # Получаем абсолютные значения чисел.
    abs_a = ABS_Z_Z(a)
    abs_b = ABS_Z_Z(b)
    
    # Преобразовываем целые числа в натуральные (учет знака будет произведен позже).
    nat_a = TRANS_Z_N(abs_a)
    nat_b = TRANS_Z_N(abs_b)
    
    # Умножаем абсолютные значения.
    result = MUL_NN_N(nat_a, nat_b)
    
    # Преобразовываем полученный результат в целое.
    result = TRANS_N_Z(result)
    
    # Определяем знак произведения.
    if POZ_Z_D(a) != POZ_Z_D(b):
        # Знаки разные, значит результат умножения отрицательный.
        result = MUL_ZM_Z(result)
    
    return result
