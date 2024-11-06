# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import pol
from DIV_PP_P import DIV_PP_P
from MUL_PP_P import MUL_PP_P
from SUB_PP_P import SUB_PP_P


def MOD_PP_P(a: pol, b: pol) -> pol: 
    """
    Функция для вычисления остатка от деления многочлена на многочлен при делении с остатком.
    """
    x = a.deepcopy()
    y = b.deepcopy()
    
    # Получаем частное от деления многочленов
    quotient = DIV_PP_P(a, b)
    
    # Остаток будет такой result = x - (quotient * y)
    # Умножаем частное на делитель
    mid = MUL_PP_P(quotient, y)
    
    # Вычитаем полученное произведение из исходного многочлена
    result = SUB_PP_P(x, mid)
    
    return result