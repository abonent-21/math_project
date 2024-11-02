# MOD_ZZ_Z.py
# Остаток от деления целого на целое (делитель отличен от нуля)
# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import ceil
from POZ_Z_D import POZ_Z_D
from ABS_Z_Z import ABS_Z_Z
from DIV_ZZ_Z import DIV_ZZ_Z
from TRANS_N_Z import TRANS_N_Z
from MUL_ZZ_Z import MUL_ZZ_Z
from SUB_ZZ_Z import SUB_ZZ_Z


def MOD_ZZ_Z(a: ceil, b: ceil) -> ceil:
    """
    Функция вычисляет остаток от деления одного целого числа на другое. 
    """
    # Проверка на деление на ноль(не смотря на условие задачи, проверка не будет лишней)
    if POZ_Z_D(b) == 0:
        raise ValueError("Делитель не может быть нулем")
    
    # Получаем абсолютные значения чисел
    abs_a = ABS_Z_Z(a)
    abs_b = ABS_Z_Z(b)

    # Производим деление целых значений и получаем целую часть
    quotient = DIV_ZZ_Z(abs_a, abs_b) # целая часть от деления

    # Вычисляем произведение целой части на делитель
    product = MUL_ZZ_Z(TRANS_N_Z(quotient), b)

    # Остаток вычисляется как a - (b * quotient)
    result = SUB_ZZ_Z(a, product)

    return result
