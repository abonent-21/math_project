# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import pol
from DIV_PP_P import DIV_PP_P
from MUL_PP_P import MUL_PP_P
from SUB_PP_P import SUB_PP_P


def MOD_PP_P(a: pol, b: pol) -> pol: 
    """
    Функция для вычисления остатка от деления многочлена на многочлен при делении с остатком.
    """
    arr1 = a.copy()
    arr2 = b.copy()
    
    # Получаем частное от деления многочленов
    quotient = DIV_PP_P(arr1, arr2)
    
    # Остаток будет такой result = arr1 - (quotient * arr2)
    # Умножаем частное на делитель
    mid = MUL_PP_P(quotient, arr2)
    
    # Вычитаем полученное произведение из исходного многочлена
    result = SUB_PP_P(arr1, mid)
    
    return result