# MOD_ZZ_Z.py
# Остаток от деления целого на целое (делитель отличен от нуля)
# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import ceil
from POZ_Z_D import POZ_Z_D
from ABS_Z_Z import ABS_Z_Z
from TRANS_Z_N import TRANS_Z_N
from DIV_NN_N import DIV_NN_N
from TRANS_N_Z import TRANS_N_Z
from MUL_ZM_Z import MUL_ZM_Z

def MOD_ZZ_Z(a: ceil, b: ceil) -> ceil:
    # Проверка на деление на ноль
    if POZ_Z_D(b) == 0:
        raise ValueError("Делитель не может быть нулем")
    
    # Получаем абсолютные значения чисел
    abs_a = ABS_Z_Z(a)
    abs_b = ABS_Z_Z(b)

    # Преобразовываем целые числа в натуральные
    nat_a = TRANS_Z_N(abs_a)
    nat_b = TRANS_Z_N(abs_b)

    # Производим деление целых значений и получаем целую часть
    quotient = DIV_ZZ_Z(abs_a, abs_b)

    # Вычисляем произведение целой части на делитель
    product = TRANS_N_Z(MUL_ZZ_Z(TRANS_N_Z(quotient), b))

    # Остаток вычисляется как a - (b * quotient)
    result = SUB_ZZ_Z(a, product)

    return result
