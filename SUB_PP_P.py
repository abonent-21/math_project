# SUB_PP_P.py
# Функция для вычитания двух многочленов
# Автор: [Самигулин Денис] ПМИ-3381

from Types import pol, rat, ceil, nat_0
from SUB_QQ_Q import SUB_QQ_Q



def SUB_PP_P(P1: pol, P2: pol) -> pol:
    """
    Вычитает многочлен P2 из P1.

    :param P1: Первый многочлен (pol)
    :param P2: Второй многочлен (pol)
    :return: Результат вычитания P1 - P2 (pol)
    """
    # Определяем максимальную степень
    max_degree = max(P1.m, P2.m)

    # Создаем нулевой коэффициент
    zero_rat = rat(num=ceil([0], 1, 0), den=nat_0([1], 1))

    # Выравниваем длину коэффициентов, добавляя нули в конец
    coeffs_P1 = P1.coefficients.copy()
    coeffs_P2 = P2.coefficients.copy()

    while len(coeffs_P1) < max_degree + 1:
        coeffs_P1.append(zero_rat)
    while len(coeffs_P2) < max_degree + 1:
        coeffs_P2.append(zero_rat)

    # Вычитаем коэффициенты
    result_coeffs = []
    for c1, c2 in zip(coeffs_P1, coeffs_P2):
        subtracted = SUB_QQ_Q(c1, c2)
        result_coeffs.append(subtracted)

    # Удаляем трейлинг нули
    while len(result_coeffs) > 1 and result_coeffs[-1].num.array == [0]:
        result_coeffs.pop()
        max_degree -= 1

    return pol(coefficients=result_coeffs, m=max_degree)