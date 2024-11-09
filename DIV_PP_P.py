# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import pol, rat, ceil_nat_0
from DEG_P_N import DEG_P_N
from DIV_QQ_Q import DIV_QQ_Q
from MUL_PQ_P import MUL_PQ_P
from MUL_Pxk_P import MUL_Pxk_P
from SUB_PP_P import SUB_PP_P


def DIV_PP_P(a: pol, b: pol) -> pol: 
    """
    Функция для вычисления результата деления полиномов.
    """
    x = a.deepcopy() 
    y = b.deepcopy()
    
    if DEG_P_N(b) == 0:  # проверяем степень второго полинома, вдруг это просто число. 
        # чтобы не писать сложный код деления, мы умножим первый многочлен на обратное значение
        divider = DIV_QQ_Q(rat(ceil([1], 1, 0), nat_0([1], 1)), y.coefficients[0])
        return MUL_PQ_P(x, divider)
    
    midcoef = [] # список, который используется для хранения коэффициентов
    result = pol([], 0) # для хранения результата деления.
    
    while DEG_P_N(x) >= DEG_P_N(y):  # пока степень первого больше или равна второго
        diff = DEG_P_N(x) - DEG_P_N(y)  # разница их степеней
        # деление старшего коэффициента первого и второго для определения коэффициента в частном
        coef = DIV_QQ_Q(x.coefficients[0], y.coefficients[0]) 
        mid = MUL_Pxk_P(y, diff)  # домножаем на степень
        mid = MUL_PQ_P(mid, coef)
        x = SUB_PP_P(x, mid)  # убираем старший член постепенно уменьшая степень
        midcoef.append(coef) # коэффициент добавляется в список коэффициентов частного.
    
    result.degree = len(midcoef) - 1
    result.coefficients = midcoef
    return result