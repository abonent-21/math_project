# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import pol, rat, ceil, nat_0
from DEG_P_N import DEG_P_N
from SUB_NN_N import SUB_NN_N
from DIV_QQ_Q import DIV_QQ_Q
from MUL_Pxk_P import MUL_Pxk_P
from MUL_PQ_P import MUL_PQ_P
from SUB_PP_P import SUB_PP_P


def DIV_PP_P(a: pol, b: pol) -> pol:
    """
    Функция для вычисления результата деления полиномов.
    """
    arr1 = a.copy()
    arr2 = b.copy()

    st1 = DEG_P_N(arr1)  # Степень первого многочлена
    st2 = DEG_P_N(arr2)  # Степень второго многочлена
        
    ans_st = SUB_NN_N(st1, st2) # Вычисляем разницу степеней
    ans_len = int(''.join(map(str, ans_st.array))) + 1 
    
    # Инициализируем ответ с начальными коэффициентами нулями
    ans = pol([rat(ceil([0], 1, 0), nat_0([1], 1)) for _ in range(ans_len)], ans_len - 1)
    
    # Расчет частного
    for i in range(ans_len):
        # Делим старший коэффициент первого полинома на старший коэффициент второго полинома
        tmp = DIV_QQ_Q(arr1.coefficients[0], arr2.coefficients[0])
        ans.coefficients[i] = tmp
        
        # Умножаем второй полином на соответствующую степень x, чтобы вычесть его из первого
        tmp_pol = MUL_Pxk_P(arr2, nat_0([ans_len - 1 - i], 1))  # Умножаем на x^(степень - i)
        arrSUB = MUL_PQ_P(tmp_pol, ans.coefficients[i]) # Умножаем второй полином на коэффициент частного


        # Обновляем первый полином, вычитая из него результат умножения
        arr1 = SUB_PP_P(arr1, arrSUB)
        
        # Удаляем ведущие нули из первого полинома
        while arr1.coefficients and arr1.coefficients[0] == rat(ceil([0], 1, 0), nat_0([1], 1)):
            arr1.coefficients.pop(0)

    return ans