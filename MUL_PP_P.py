# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import pol, rat, ceil, nat_0
from DEG_P_N import DEG_P_N
from ADD_NN_N import ADD_NN_N
from ADD_1N_N import ADD_1N_N
from MUL_Pxk_P import MUL_Pxk_P
from MUL_PQ_P import MUL_PQ_P
from ADD_PP_P import ADD_PP_P


def MUL_PP_P(arr1: pol, arr2: pol) -> pol:
    """
    Умножает два многочлена P1 и P2.
    """
    st1 = DEG_P_N(arr1)  # Степень первого многочлена
    st2 = DEG_P_N(arr2)  # Степень второго многочлена
    ans_st = ADD_NN_N(st1, st2) # Вычисляем степень итогового полинома
    ans_st = ADD_1N_N(ans_st) # Прибавляем единицу для правильного подсчета результата.
    
    ans_len = int(''.join(map(str, ans_st.array))) # Переводим в int для правильной инициализации итогового массива
    result = pol([rat(ceil([0], 1, 0), nat_0([1], 1)) for _ in range(ans_len)], ans_len - 1)
    inter_pol = []
    
    ans_len2 = int(''.join(map(str, st2.array))) # Переводим для правильной работы цикла
    
    for i in range(ans_len2 + 1):
        k = MUL_Pxk_P(arr1, nat_0([arr2.m - i], 1)) # Умножение на степень x^k
        e = MUL_PQ_P(k, arr2.coefficients[arr2.m - i]) # Умножение на коэффициент второго полинома
        inter_pol.append(e)  # Добавляем промежуточный результат в массив
        
    # Проходим по каждому члену второго полинома
    for i in inter_pol:
        result = ADD_PP_P(result, i)
     
    return result

