# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import pol, rat, ceil_nat_0
from MUL_Pxk_P import MUL_Pxk_P
from MUL_Pxk_P import MUL_Pxk_P
from ADD_PP_P import ADD_PP_P


def MUL_PP_P(a: pol, b: pol) -> pol: # функцию писал в момент, когда еще не был сделан класс P. потом подстроюсь под него.
    """
    Функция для вычисления результата умножения полиномов.
    """
    x = a.deepcopy() 
    y = b.deepcopy() 
    result = pol([rat(ceil([0], 1, 0), nat_0([1], 1))], 0)  # для хранения результата умножения.
    
    # Массив для хранения промежуточных полиномов, полученных в процессе умножения.
    inter_pol = []

    # Перебираем каждый коэффициент второго полинома
    for i in range(y.m + 1):
        # k обеспечивает правильный порядок умножения 
        k = MUL_Pxk_P(x, i)  # Умножаем первый полином на x^i
        e = MUL_PQ_P(k, y.coefficients[y.degree - i])  # Умножаем на соответствующий коэффициент
        inter_pol.append(e)  # Добавляем в массив для последующего сложения

    # Складываем все промежуточные полиномы
    for i in inter_pol:
        result = ADD_PP_P(result, i)  # Прибавляем текущий полином к итоговому результату

    return result