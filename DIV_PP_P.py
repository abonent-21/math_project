# DIV_PP_P.py
# Частное от деления многочлена на многочлен при делении с остатком
# Автор: Сычев Н.С. Группа - ПМИ-3381

# struct: Многочлен с рациональными коэффициентами m – степень многочлена и массив C коэффициентов (P)
# struct: rat = self, num: ceil, den: nat_0):

from Types import P, rat, ceil_nat_0
from DEG_P_N import DEG_P_N
from DIV_QQ_Q import DIV_QQ_Q
from MUL_PQ_P import MUL_PQ_P
from MUL_Pxk_P import MUL_Pxk_P
from SUB_PP_P import SUB_PP_P


def DIV_PP_P(a: P, b: P) -> P: # функцию писал в момент, когда еще не был сделан класс P. потом подстроюсь под него.
    """
    Функция для вычисления результата деления полиномов.
    """
    x = a.deepcopy() # глубокое копирование на всякий случай...
    if DEG_P_N(b) == 0:  # проверяем степень второго полинома, вдруг это просто число. 
        # чтобы не писать код деления, мы умножим первый многочлен на обратное значение
        divider = DIV_QQ_Q(rat(ceil([1], 1, 0), nat_0([1], 1)), x2.coefficients[0])
        return MUL_PQ_P(x, divider)
    
    coef = rat(ceil([0], 1, 0), nat_0([1], 1)) # коэффициент частного при делении полиномов
    diff = 0 # инициализация разницы степеней полиномов
    mid = P(0, [rat(ceil([0], 1, 0), nat_0([1], 1))])
    midcoef = [] # список, который используется для хранения коэффициентов
    result = P(0, [])
    
    y = b.deepcopy()
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
    
    
    