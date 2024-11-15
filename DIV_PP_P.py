# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import pol, rat, ceil, nat_0
from DEG_P_N import DEG_P_N
from SUB_NN_N import SUB_NN_N
from ADD_1N_N import ADD_1N_N
from DIV_QQ_Q import DIV_QQ_Q
from MUL_Pxk_P import MUL_Pxk_P
from MUL_PQ_P import MUL_PQ_P
from SUB_PP_P import SUB_PP_P


def DIV_PP_P(a: pol, b: pol) -> pol:
    """
    Функция для вычисления результата деления двух полиномов.
    """
    arr1 = a.copy()
    arr2 = b.copy()
    
    # проверяем степень второго полинома, вдруг это просто число 
    if DEG_P_N(arr2) == nat_0([0], 1):
        # Проверка на деление на ноль (не смотря на условие задачи, проверка не будет лишней).
        if arr2.coefficients[0] == rat(ceil([0], 1, 0), nat_0([1], 1)):
            raise ValueError("Делитель не может быть нулем")
            
        # чтобы не писать код деления, мы умножим первый многочлен на обратное значение
        divider = DIV_QQ_Q(rat(ceil([1], 1, 0), nat_0([1], 1)), arr2.coefficients[0])
        return MUL_PQ_P(arr1, divider)
    
    st1 = DEG_P_N(arr1)  # Степень первого многочлена
    st2 = DEG_P_N(arr2)  # Степень второго многочлена    
    ans_st = SUB_NN_N(st1, st2)  # Вычисляем разницу степеней
    ans_st = ADD_1N_N(ans_st) # Прибавляем единицу для правильного подсчета результата.
    
    ans_len = int(''.join(map(str, ans_st.array))) # Переводим в int для правильной инициализации итогового массива
    result = pol([rat(ceil([0], 1, 0), nat_0([1], 1)) for _ in range(ans_len)], ans_len - 1)
    
    while int(''.join(map(str, DEG_P_N(arr1).array))) >= int(''.join(map(str, DEG_P_N(arr2).array))):
        st1 = DEG_P_N(arr1)  # Степень первого многочлена
        st2 = DEG_P_N(arr2)  # Степень второго многочлена
        deg_diff = SUB_NN_N(st1, st2)  # Вычисляем разницу степеней
        deg_diff_int = int(''.join(map(str, deg_diff.array)))
        
        # Делим коэффициенты
        coef = DIV_QQ_Q(arr1.coefficients[-1], arr2.coefficients[-1])

        # Устанавливаем соответствующий коэффициент в частном
        result.coefficients[deg_diff_int] = coef

        # Умножаем второй полином на x^(разница степеней) и на коэффициент частного
        tmp_pol = MUL_Pxk_P(arr2, deg_diff)  # Умножаем на x^(разница степеней)
        arrSUB = MUL_PQ_P(tmp_pol, coef)  # Умножаем на коэффициент частного

        # Обновляем первый полином, вычитая из него результат умножения
        arr1 = SUB_PP_P(arr1, arrSUB)

        # Удаляем ведущие нули из первого полинома
        while arr1.coefficients and arr1.coefficients[-1] == rat(ceil([0], 1, 0), nat_0([1], 1)):
            arr1.coefficients.pop()
            
    return result
