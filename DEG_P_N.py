# Автор: Марков М.М. Группа - ПМИ-3381

from Types import pol, nat_0


def DEG_P_N(P: pol) -> nat_0:
    # Функция для получения степени многочлена P.

    # Преобразование степени многочлена в nat_0
    degree = [int(digit) for digit in str(P.m)]
    return nat_0(degree, len(degree))  # Возвращаем объект степень как объект класса nat_0
