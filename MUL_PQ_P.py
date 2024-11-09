# MUL_PQ_P.py
# Умножение многочлена на рациональное число
# Автор: [Самигулин Денис] Группа - [ПМИ-3381]

from Types import pol, rat
from MUL_QQ_Q import MUL_QQ_Q

def MUL_PQ_P(P: pol, Q: rat) -> pol:
    """
    Умножает многочлен P на рациональное число Q.

    :param P: Многочлен (pol)
    :param Q: Рациональное число (rat)
    :return: Результат умножения многочлена на число (pol)
    """
    # Умножаем каждый коэффициент на рациональное число Q
    result_coeffs = []
    for coef in P.coefficients:
        mul_coef = MUL_QQ_Q(coef, Q)
        result_coeffs.append(mul_coef)

    # Степень многочлена остается неизменной
    result_pol = pol(coefficients=result_coeffs, m=P.m)
    return result_pol
