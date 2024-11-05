# Автор: Марков М.М. Группа - ПМИ-3381

from Types import pol, rat, nat_0, ceil


def MUL_Pxk_P(P: pol, k: nat_0) -> pol:
    # Функция для умножения многочлена с рациональными коэффициентами P на x^k.

    # Преобразуем степень `k` из nat_0 в целое число
    k_value = int(''.join(map(str, k.array)))

    # Вычисляем новую степень многочлена
    new_degree = P.m + k_value

    # Создаем новый массив коэффициентов с добавлением k нулевых коэффициентов
    zero_rat = rat(ceil([0], 1, 0), nat_0([1], 1))  # Нулевое рациональное число
    new_coefficients = [zero_rat] * k_value + P.coefficients

    # Возвращаем новый многочлен с обновлённой степенью и коэффициентами
    return pol(new_coefficients, new_degree)
