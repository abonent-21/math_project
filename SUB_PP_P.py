# SUB_PP_P.py
# Вычитание многочленов
# Автор: [Самигулин Денис] Группа - [ПМИ-3381]

from Types import pol, rat, ceil, nat_0
from SUB_QQ_Q import SUB_QQ_Q


def SUB_PP_P(P1: pol, P2: pol) -> pol:
    """
    Вычитает многочлен P2 из многочлена P1.

    :param P1: Уменьшаемое (pol)
    :param P2: Вычитаемое (pol)
    :return: Результат вычитания многочленов (pol)
    """
    # Находим максимальную степень многочлена
    max_degree = max(P1.m, P2.m)

    # Вычисляем разницу степеней для выравнивания коэффициентов
    delta_P1 = max_degree - P1.m
    delta_P2 = max_degree - P2.m

    # Выравниваем коэффициенты, добавляя нулевые коэффициенты слева
    zero_rat = rat(num=ceil([0], 1, 0), den=nat_0([1], 1))
    coeffs_P1 = [zero_rat] * delta_P1 + P1.coefficients
    coeffs_P2 = [zero_rat] * delta_P2 + P2.coefficients

    # Вычитаем коэффициенты
    result_coeffs = []
    for coef1, coef2 in zip(coeffs_P1, coeffs_P2):
        sub_coef = SUB_QQ_Q(coef1, coef2)
        result_coeffs.append(sub_coef)

    # Убираем ведущие нулевые коэффициенты
    while len(result_coeffs) > 1 and result_coeffs[0].num.array == [0]:
        result_coeffs.pop(0)
        max_degree -= 1

    # Создаем новый многочлен
    result_pol = pol(coefficients=result_coeffs, m=max_degree)
    return result_pol
