# Автор: Марков М.М. Группа - ПМИ-3381

from Types import pol, rat


def LED_P_Q(P: pol) -> rat:
    # Функция для получения старшего коэффициента многочлена с рациональными коэффициентами P.

    # Индекс старшего коэффициента — это значение степени многочлена P.m
    highest_degree_index = P.m

    # Возвращаем старший коэффициент
    return P.coefficients[highest_degree_index]
