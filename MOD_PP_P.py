# MOD_PP_P.py
# Остаток от деления многочлена на многочлен при делении с остатком
# Автор: Сычев Н.С. Группа - ПМИ-3381

# struct: Многочлен с рациональными коэффициентами m – степень многочлена и массив C коэффициентов (P)
# struct: Q = ceil / nat_0

from Types import P, Q
from DIV_PP_P import DIV_PP_P
from MUL_PP_P import MUL_PP_P
from SUB_PP_P import SUB_PP_P


def MOD_PP_P(a: P, b: P) -> P: # функцию писал в момент, когда еще не были реализованы классы Q и P. потом подстроюсь под них.
    """
    Функция для вычисления остатка от деления многочлена на многочлен при делении с остатком.
    """
    # все эти комменты потом уберу, просто для удобства. 
    # в данной версии коэффициенты это объекты класса Q (на момент создания он еще не был определен в проекте)
    x = a.deepcopy()
    y = b.deepcopy()
    
    # Получаем частное от деления многочленов
    quotient = DIV_PP_P(a, b)
    
    # Остаток такой result = x - (quotient * y)
    # Умножаем частное на делитель
    mid = MUL_PP_P(quotient, y)
    
    # Вычитаем полученное произведение из исходного многочлена
    result = SUB_PP_P(x, mid)
    
    return result