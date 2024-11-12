# tests.py

import pytest
from Types import rat, ceil, nat_0, pol
from ADD_PP_P import ADD_PP_P
from SUB_PP_P import SUB_PP_P
from MUL_PQ_P import MUL_PQ_P

# Вспомогательные функции
def create_ceil(number: int) -> ceil:
    """
    Создаёт объект класса ceil из целого числа.
    :param number: Целое число (положительное или отрицательное).
    :return: Объект класса ceil.
    """
    if number == 0:
        array = [0]
        sign = 0
    else:
        sign = 0 if number > 0 else 1
        num = abs(number)
        array = [int(digit) for digit in str(num)]
    n = len(array)
    return ceil(array, n, sign)

def create_nat_0(number: int) -> nat_0:
    """
    Создаёт объект класса nat_0 из натурального числа.
    :param number: Натуральное число (>= 0).
    :return: Объект класса nat_0.
    """
    assert number >= 0, "Натуральное число должно быть >= 0"
    array = [int(digit) for digit in str(number)]
    n = len(array)
    return nat_0(array, n)

def create_rat(numerator: int, denominator: int) -> rat:
    """
    Создаёт объект класса rat из числителя и знаменателя.
    :param numerator: Целое число (может быть отрицательным).
    :param denominator: Натуральное число (> 0).
    :return: Объект класса rat.
    """
    assert denominator != 0, "Знаменатель не может быть равен 0"
    num = create_ceil(numerator)
    den = create_nat_0(denominator)
    return rat(num, den)

def create_polynomial(coefficients: list, degree: int) -> pol:
    """
    Создаёт объект класса pol из списка коэффициентов и степени.
    Коэффициенты должны быть упорядочены от младшего к старшему члену.
    :param coefficients: Список объектов класса rat.
    :param degree: Степень многочлена.
    :return: Объект класса pol.
    """
    return pol(coefficients=coefficients, m=degree)

# Тесты
def test_creation_small_polynomials():
    # Многочлен P1(x) = x + 1
    P1 = create_polynomial(
        coefficients=[
            create_rat(1, 1),  # x^0: 1/1
            create_rat(1, 1)   # x^1: 1/1
        ],
        degree=1
    )

    # Многочлен P2(x) = x^2 + x
    P2 = create_polynomial(
        coefficients=[
            create_rat(0, 1),  # x^0: 0/1
            create_rat(1, 1),  # x^1: 1/1
            create_rat(1, 1)   # x^2: 1/1
        ],
        degree=2
    )

    # Ожидаемые многочлены
    expected_P1 = create_polynomial(
        coefficients=[
            create_rat(1, 1),
            create_rat(1, 1)
        ],
        degree=1
    )

    expected_P2 = create_polynomial(
        coefficients=[
            create_rat(0, 1),
            create_rat(1, 1),
            create_rat(1, 1)
        ],
        degree=2
    )

    # Проверяем создание
    assert P1 == expected_P1, f"Ожидался P1: {expected_P1}, получен: {P1}"
    assert P2 == expected_P2, f"Ожидался P2: {expected_P2}, получен: {P2}"

def test_operations_small_polynomials():
    # Создание многочленов
    P1 = create_polynomial(
        coefficients=[
            create_rat(1, 1),  # x^0: 1/1
            create_rat(1, 1)   # x^1: 1/1
        ],
        degree=1
    )

    P2 = create_polynomial(
        coefficients=[
            create_rat(0, 1),  # x^0: 0/1
            create_rat(1, 1),  # x^1: 1/1
            create_rat(1, 1)   # x^2: 1/1
        ],
        degree=2
    )

    # Сложение P1 + P2 = x^2 + 2x + 1
    result_add = ADD_PP_P(P1, P2)
    expected_add = create_polynomial(
        coefficients=[
            create_rat(1, 1),      # x^0: 1 + 0 = 1/1
            create_rat(2, 1),      # x^1: 1 + 1 = 2/1
            create_rat(1, 1)       # x^2: 0 + 1 = 1/1
        ],
        degree=2
    )
    assert result_add == expected_add, f"Ожидалось P1 + P2: {expected_add}, получен: {result_add}"

    # Вычитание P1 - P2 = -x^2 + 0x + 1
    result_sub = SUB_PP_P(P1, P2)
    expected_sub = create_polynomial(
        coefficients=[
            create_rat(1, 1),      # x^0: 1 - 0 = 1/1
            create_rat(0, 1),      # x^1: 1 - 1 = 0/1
            create_rat(-1, 1)      # x^2: 0 - 1 = -1/1
        ],
        degree=2
    )
    assert result_sub == expected_sub, f"Ожидалось P1 - P2: {expected_sub}, получен: {result_sub}"

    # Умножение P1 * Q, где Q = 3/2: (x + 1) * 3/2 = (3/2)x + 3/2
    Q = create_rat(3, 2)
    result_mul = MUL_PQ_P(P1, Q)
    expected_mul = create_polynomial(
        coefficients=[
            create_rat(3, 2),      # x^0: 1 * 3/2 = 3/2
            create_rat(3, 2)       # x^1: 1 * 3/2 = 3/2
        ],
        degree=1
    )
    assert result_mul == expected_mul, f"Ожидалось P1 * Q: {expected_mul}, получен: {result_mul}"

def test_creation_medium_polynomials():
    # Многочлен P3(x) = 2x^3 + 0x^2 + 5x + 3
    P3 = create_polynomial(
        coefficients=[
            create_rat(3, 1),      # x^0: 3/1
            create_rat(5, 1),      # x^1: 5/1
            create_rat(0, 1),      # x^2: 0/1
            create_rat(2, 1)       # x^3: 2/1
        ],
        degree=3
    )

    # Многочлен P4(x) = -x^4 + 4x^3 + x^2 - 2x + 1
    P4 = create_polynomial(
        coefficients=[
            create_rat(1, 1),      # x^0: 1/1
            create_rat(-2, 1),     # x^1: -2/1
            create_rat(1, 1),      # x^2: 1/1
            create_rat(4, 1),      # x^3: 4/1
            create_rat(-1, 1)      # x^4: -1/1
        ],
        degree=4
    )

    # Ожидаемые многочлены
    expected_P3 = create_polynomial(
        coefficients=[
            create_rat(3, 1),
            create_rat(5, 1),
            create_rat(0, 1),
            create_rat(2, 1)
        ],
        degree=3
    )

    expected_P4 = create_polynomial(
        coefficients=[
            create_rat(1, 1),
            create_rat(-2, 1),
            create_rat(1, 1),
            create_rat(4, 1),
            create_rat(-1, 1)
        ],
        degree=4
    )

    # Проверяем создание
    assert P3 == expected_P3, f"Ожидался P3: {expected_P3}, получен: {P3}"
    assert P4 == expected_P4, f"Ожидался P4: {expected_P4}, получен: {P4}"

def test_operations_medium_polynomials():
    # Создание многочленов
    P3 = create_polynomial(
        coefficients=[
            create_rat(3, 1),      # x^0: 3/1
            create_rat(5, 1),      # x^1: 5/1
            create_rat(0, 1),      # x^2: 0/1
            create_rat(2, 1)       # x^3: 2/1
        ],
        degree=3
    )

    P4 = create_polynomial(
        coefficients=[
            create_rat(1, 1),      # x^0: 1/1
            create_rat(-2, 1),     # x^1: -2/1
            create_rat(1, 1),      # x^2: 1/1
            create_rat(4, 1),      # x^3: 4/1
            create_rat(-1, 1)      # x^4: -1/1
        ],
        degree=4
    )

    # Сложение P3 + P4 = -x^4 + 6x^3 + 1x^2 + 3x + 4
    result_add = ADD_PP_P(P3, P4)
    expected_add = create_polynomial(
        coefficients=[
            create_rat(4, 1),      # x^0: 3 + 1 = 4/1
            create_rat(3, 1),      # x^1: 5 + (-2) = 3/1
            create_rat(1, 1),      # x^2: 0 + 1 = 1/1
            create_rat(6, 1),      # x^3: 2 + 4 = 6/1
            create_rat(-1, 1)      # x^4: 0 + (-1) = -1/1
        ],
        degree=4
    )
    assert result_add == expected_add, f"Ожидалось P3 + P4: {expected_add}, получен: {result_add}"

    # Вычитание P4 - P3 = -x^4 + 2x^3 + 1x^2 -7x -2
    result_sub = SUB_PP_P(P4, P3)
    expected_sub = create_polynomial(
        coefficients=[
            create_rat(-2, 1),     # x^0: 1 - 3 = -2/1
            create_rat(-7, 1),     # x^1: -2 - 5 = -7/1
            create_rat(1, 1),      # x^2: 1 - 0 = 1/1
            create_rat(2, 1),      # x^3: 4 - 2 = 2/1
            create_rat(-1, 1)      # x^4: 0 - 1 = -1/1
        ],
        degree=4
    )
    assert result_sub == expected_sub, f"Ожидалось P4 - P3: {expected_sub}, получен: {result_sub}"

    # Умножение P3 * Q, где Q = -2/3: (2x^3 + 0x^2 + 5x + 3) * (-2/3) = (-4/3)x^3 + 0x^2 + (-10/3)x + (-6/3) = (-4/3)x^3 - (10/3)x - 2
    Q = create_rat(-2, 3)
    result_mul = MUL_PQ_P(P3, Q)
    expected_mul = create_polynomial(
        coefficients=[
            create_rat(-2, 1),     # x^0: -6/3 = -2/1
            create_rat(-10, 3),    # x^1: 5 * (-2/3) = -10/3
            create_rat(0, 1),      # x^2: 0 * (-2/3) = 0/1
            create_rat(-4, 3)      # x^3: 2 * (-2/3) = -4/3
        ],
        degree=3
    )
    assert result_mul == expected_mul, f"Ожидалось P3 * Q: {expected_mul}, получен: {result_mul}"

if __name__ == '__main__':
    # Запускаем pytest при выполнении файла напрямую
    pytest.main()
