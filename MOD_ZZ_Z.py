# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import ceil, dig
from POZ_Z_D import POZ_Z_D
from DIV_ZZ_Z import DIV_ZZ_Z
from MUL_ZZ_Z import MUL_ZZ_Z
from SUB_ZZ_Z import SUB_ZZ_Z
from ABS_Z_Z import ABS_Z_Z


def MOD_ZZ_Z(a: ceil, b: ceil) -> ceil:
    """
    Функция вычисляет остаток от деления одного целого числа на другое. 
    """
    # Проверка на деление на ноль(не смотря на условие задачи, проверка не будет лишней).
    if POZ_Z_D(b) == dig(0):
        raise ValueError("Делитель не может быть нулем")

    # Производим деление целых значений и получаем целую часть
    quotient = DIV_ZZ_Z(a, b) # целая часть от деления

    # Вычисляем произведение целой части на делитель
    product = MUL_ZZ_Z(quotient, b)

    # Остаток вычисляется как a - (b * quotient)
    remainder = SUB_ZZ_Z(a, product)

    # Если остаток отрицательный и делитель положительный, добавляем делитель к остатку
    if (POZ_Z_D(remainder) == dig(1) and POZ_Z_D(b) == dig(2)): 
        remainder = SUB_ZZ_Z(b, ABS_Z_Z(remainder))  # остаток = b - |остаток|

    return remainder