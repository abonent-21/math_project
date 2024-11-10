# test_DIV_QQ_Q.py

import pytest
from DIV_QQ_Q import DIV_QQ_Q
from Types import rat, ceil, nat_0


@pytest.fixture
def build_rat():
    """
    Утилита для создания объекта rat.
    """

    def _build_rat(num_array, num_n, num_sign, den_array, den_n):
        num = ceil(array=num_array, n=num_n, sign=num_sign)
        den = nat_0(array=den_array, n=den_n)
        return rat(num=num, den=den)

    return _build_rat


def test_div_positive_fractions(build_rat):
    """
    Тестирование деления двух положительных дробей.
    (1/2) / (3/4) = (1/2) * (4/3) = (4/6) -> (2/3)
    """
    divisible = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[2], den_n=1)
    divider = build_rat(num_array=[3], num_n=1, num_sign=0, den_array=[4], den_n=1)
    expected = build_rat(num_array=[2], num_n=1, num_sign=0, den_array=[3], den_n=1)

    result = DIV_QQ_Q(divisible, divider)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_div_negative_divider(build_rat):
    """
    Тестирование деления дроби на отрицательную дробь.
    (1/3) / (-2/5) = (1/3) * (-5/2) = (-5/6)
    """
    divisible = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[3], den_n=1)
    divider = build_rat(num_array=[2], num_n=1, num_sign=1, den_array=[5], den_n=1)
    expected = build_rat(num_array=[5], num_n=1, num_sign=1, den_array=[6], den_n=1)

    result = DIV_QQ_Q(divisible, divider)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_div_both_negative_fractions(build_rat):
    """
    Тестирование деления двух отрицательных дробей.
    (-1/4) / (-3/5) = (1/4) * (5/3) = (5/12)
    """
    divisible = build_rat(num_array=[1], num_n=1, num_sign=1, den_array=[4], den_n=1)
    divider = build_rat(num_array=[3], num_n=1, num_sign=1, den_array=[5], den_n=1)
    expected = build_rat(num_array=[5], num_n=1, num_sign=0, den_array=[1, 2], den_n=2)

    result = DIV_QQ_Q(divisible, divider)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_dividend_zero(build_rat):
    """
    Тестирование деления нулевой дроби на любую дробь.
    (0/1) / (5/6) = (0/1)
    """
    divisible = build_rat(num_array=[0], num_n=1, num_sign=0, den_array=[1], den_n=1)
    divider = build_rat(num_array=[5], num_n=1, num_sign=0, den_array=[6], den_n=1)
    expected = build_rat(num_array=[0], num_n=1, num_sign=0, den_array=[1], den_n=1)

    result = DIV_QQ_Q(divisible, divider)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_divide_by_itself(build_rat):
    """
    Тестирование деления дроби на саму себя.
    (3/7) / (3/7) = (3/7) * (7/3) = (21/21) -> (1/1)
    """
    divisible = build_rat(num_array=[3], num_n=1, num_sign=0, den_array=[7], den_n=1)
    divider = build_rat(num_array=[3], num_n=1, num_sign=0, den_array=[7], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[1], den_n=1)

    result = DIV_QQ_Q(divisible, divider)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_divide_by_one(build_rat):
    """
    Тестирование деления дроби на 1.
    (2/5) / (1/1) = (2/5)
    """
    divisible = build_rat(num_array=[2], num_n=1, num_sign=0, den_array=[5], den_n=1)
    divider = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[1], den_n=1)
    expected = build_rat(num_array=[2], num_n=1, num_sign=0, den_array=[5], den_n=1)

    result = DIV_QQ_Q(divisible, divider)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_div_result_reduction(build_rat):
    """
    Тестирование, что результат сокращается до несократимой дроби.
    (4/6) / (2/3) = (4/6) * (3/2) = (12/12) -> (1/1)
    """
    divisible = build_rat(num_array=[4], num_n=1, num_sign=0, den_array=[6], den_n=1)
    divider = build_rat(num_array=[2], num_n=1, num_sign=0, den_array=[3], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[1], den_n=1)

    result = DIV_QQ_Q(divisible, divider)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_div_mixed_signs(build_rat):
    """
    Тестирование деления дробей с разными знаками.
    (1/3) / (-2/5) = (1/3) * (-5/2) = (-5/6)
    """
    divisible = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[3], den_n=1)
    divider = build_rat(num_array=[2], num_n=1, num_sign=1, den_array=[5], den_n=1)
    expected = build_rat(num_array=[5], num_n=1, num_sign=1, den_array=[6], den_n=1)

    result = DIV_QQ_Q(divisible, divider)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_div_large_numbers(build_rat):
    """
    Тестирование деления дробей с большими числами.
    (123/456) / (789/101112) = (123/456) * (101112/789) -> сокращение
    """
    divisible = build_rat(num_array=[1, 2, 3], num_n=3, num_sign=0, den_array=[4, 5, 6], den_n=3)
    divider = build_rat(num_array=[7, 8, 9], num_n=3, num_sign=0, den_array=[1, 0, 1, 1, 1, 2], den_n=6)

    # Преобразуем числители и знаменатели в целые числа
    num1 = int(''.join(map(str, divisible.num.array))) * (1 if divisible.num.sign == 0 else -1)
    den1 = int(''.join(map(str, divisible.den.array)))

    num2 = int(''.join(map(str, divider.num.array))) * (1 if divider.num.sign == 0 else -1)
    den2 = int(''.join(map(str, divider.den.array)))

    # Деление дробей: (a/b) / (c/d) = (a*d) / (b*c)
    product_num = num1 * den2
    product_den = den1 * num2

    # Проверка деления на ноль (если num2 == 0, но по условию делитель не равен нулю)
    if num2 == 0:
        pytest.fail("Деление на ноль не должно происходить по условию")

    # Сокращение дроби
    from math import gcd
    common_div = gcd(abs(product_num), abs(product_den))
    reduced_num = product_num // common_div
    reduced_den = product_den // common_div

    # Определение знака
    expected_sign = 0
    if (reduced_num < 0) != (reduced_den < 0):
        expected_sign = 1
    reduced_num = abs(reduced_num)
    reduced_den = abs(reduced_den)

    # Подготовка массивов цифр
    expected_num = list(map(int, str(reduced_num)))
    expected_den = list(map(int, str(reduced_den)))

    expected = build_rat(
        num_array=expected_num,
        num_n=len(expected_num),
        num_sign=expected_sign,
        den_array=expected_den,
        den_n=len(expected_den)
    )

    result = DIV_QQ_Q(divisible, divider)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_divide_by_zero(build_rat):
    """
    Тестирование деления дроби на нулевую дробь.
    (1/2) / (0/1) -> должно вызвать ValueError
    """
    divisible = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[2], den_n=1)
    divider = build_rat(num_array=[0], num_n=1, num_sign=0, den_array=[1], den_n=1)

    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        DIV_QQ_Q(divisible, divider)
