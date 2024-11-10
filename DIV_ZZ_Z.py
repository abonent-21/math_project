# MUL_ZZ_Z.py
# Возвращает частное от деления целого на целое (делитель отличен от нуля)
# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import ceil, dig
from POZ_Z_D import POZ_Z_D
from ABS_Z_Z import ABS_Z_Z
from TRANS_Z_N import TRANS_Z_N
from DIV_NN_N import DIV_NN_N
from TRANS_N_Z import TRANS_N_Z
from MUL_ZM_Z import MUL_ZM_Z


def DIV_ZZ_Z(a: ceil, b: ceil) -> ceil:
    """
    Функция для деления двух целых чисел.
    """
    # Проверка на деление на ноль (не смотря на условие задачи, проверка не будет лишней).
    if POZ_Z_D(b) == dig(0):
        raise ValueError("Делитель не может быть нулем")
        
    # Получаем абсолютные значения чисел (учет знака будет произведен позже).
    abs_a = ABS_Z_Z(a)
    abs_b = ABS_Z_Z(b)
    
    # Преобразовываем целые числа в натуральные (учет знака будет произведен позже).
    nat_a = TRANS_Z_N(abs_a)
    nat_b = TRANS_Z_N(abs_b)
    
    # Производим деление абсолютных значений.
    result = DIV_NN_N(nat_a, nat_b)
    
    # Преобразовываем полученный результат в целое.
    result = TRANS_N_Z(result)
    
    # Определяем знак полученного результата.
    if POZ_Z_D(a) != POZ_Z_D(b):
        # Знаки разные, значит результат деления отрицательный.
        result = MUL_ZM_Z(result) # Меняем знак результата.
    
    return result