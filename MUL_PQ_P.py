# MUL_PQ_P.py
# Функция для умножения многочлена на рациональное число
# Автор: [Самигулин Денис] ПМИ-3381

from Types import pol, rat, ceil, nat_0
from MUL_QQ_Q import MUL_QQ_Q


def MUL_PQ_P(P: pol, Q: rat) -> pol:
    """
    Умножает многочлен P на рациональное число Q.

    :param P: Многочлен (pol)
    :param Q: Рациональное число (rat)
    :return: Результат умножения P * Q (pol)
    """
    # Умножаем каждый коэффициент на Q
    result_coeffs = []
    for coef in P.coefficients:
        multiplied = MUL_QQ_Q(coef, Q)
        result_coeffs.append(multiplied)

    # Степень остается неизменной
    max_degree = P.m

    return pol(coefficients=result_coeffs, m=max_degree)
