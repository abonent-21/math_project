# ADD_PP_P.py
# Сложение многочленов
# Автор: [Самигулин Денис] Группа - [ПМИ-3381]

from Types import pol, rat, ceil, nat_0
from ADD_QQ_Q import ADD_QQ_Q


def ADD_PP_P(P1: pol, P2: pol) -> pol:
    """
    Складывает два многочлена P1 и P2.

    :param P1: Первый многочлен (pol)
    :param P2: Второй многочлен (pol)
    :return: Результат сложения многочленов (pol)
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

    # Суммируем коэффициенты
    result_coeffs = []
    for coef1, coef2 in zip(coeffs_P1, coeffs_P2):
        sum_coef = ADD_QQ_Q(coef1, coef2)
        result_coeffs.append(sum_coef)

    # Убираем ведущие нулевые коэффициенты
    while len(result_coeffs) > 1 and result_coeffs[0].num.array == [0]:
        result_coeffs.pop(0)
        max_degree -= 1

    # Создаем новый многочлен
    result_pol = pol(coefficients=result_coeffs, m=max_degree)
    return result_pol
