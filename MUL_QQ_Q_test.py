# test_MUL_QQ_Q.py

import pytest
from MUL_QQ_Q import MUL_QQ_Q
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


def test_mul_positive_fractions(build_rat):
    """
    Тестирование умножения двух положительных дробей.
    (1/2) * (3/4) = (3/8)
    """
    multiplier_one = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[2], den_n=1)
    multiplier_two = build_rat(num_array=[3], num_n=1, num_sign=0, den_array=[4], den_n=1)
    expected = build_rat(num_array=[3], num_n=1, num_sign=0, den_array=[8], den_n=1)

    result = MUL_QQ_Q(multiplier_one, multiplier_two)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_mul_negative_fraction(build_rat):
    """
    Тестирование умножения дроби на отрицательную дробь.
    (1/3) * (-2/5) = (-2/15)
    """
    multiplier_one = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[3], den_n=1)
    multiplier_two = build_rat(num_array=[2], num_n=1, num_sign=1, den_array=[5], den_n=1)
    expected = build_rat(num_array=[2], num_n=1, num_sign=1, den_array=[1, 5], den_n=2)  # Исправлено den_array

    result = MUL_QQ_Q(multiplier_one, multiplier_two)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_mul_both_negative_fractions(build_rat):
    """
    Тестирование умножения двух отрицательных дробей.
    (-1/4) * (-3/5) = (3/20)
    """
    multiplier_one = build_rat(num_array=[1], num_n=1, num_sign=1, den_array=[4], den_n=1)
    multiplier_two = build_rat(num_array=[3], num_n=1, num_sign=1, den_array=[5], den_n=1)
    expected = build_rat(num_array=[3], num_n=1, num_sign=0, den_array=[2, 0], den_n=2)  # Исправлено den_array

    result = MUL_QQ_Q(multiplier_one, multiplier_two)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_mul_with_zero_numerator(build_rat):
    """
    Тестирование умножения дроби с нулевым числителем.
    (0/1) * (5/6) = (0/1)
    """
    multiplier_one = build_rat(num_array=[0], num_n=1, num_sign=0, den_array=[1], den_n=1)
    multiplier_two = build_rat(num_array=[5], num_n=1, num_sign=0, den_array=[6], den_n=1)
    expected = build_rat(num_array=[0], num_n=1, num_sign=0, den_array=[1], den_n=1)

    result = MUL_QQ_Q(multiplier_one, multiplier_two)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_mul_result_reduction(build_rat):
    """
    Тестирование, что результат сокращается до несократимой дроби.
    (2/4) * (3/6) = (6/24) -> (1/4)
    """
    multiplier_one = build_rat(num_array=[2], num_n=1, num_sign=0, den_array=[4], den_n=1)
    multiplier_two = build_rat(num_array=[3], num_n=1, num_sign=0, den_array=[6], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[4], den_n=1)

    result = MUL_QQ_Q(multiplier_one, multiplier_two)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_mul_mixed_signs(build_rat):
    """
    Тестирование умножения дробей с разными знаками.
    (1/3) * (-2/5) = (-2/15)
    """
    multiplier_one = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[3], den_n=1)
    multiplier_two = build_rat(num_array=[2], num_n=1, num_sign=1, den_array=[5], den_n=1)
    expected = build_rat(num_array=[2], num_n=1, num_sign=1, den_array=[1, 5], den_n=2)  # Исправлено den_array

    result = MUL_QQ_Q(multiplier_one, multiplier_two)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_mul_large_numbers(build_rat):
    """
    Тестирование умножения дробей с большими числами.
    (123/456) * (789/101112) = (123*789)/(456*101112) -> сокращение
    """
    multiplier_one = build_rat(num_array=[1, 2, 3], num_n=3, num_sign=0, den_array=[4, 5, 6], den_n=3)
    multiplier_two = build_rat(num_array=[7, 8, 9], num_n=3, num_sign=0, den_array=[1, 0, 1, 1, 1, 2], den_n=6)

    # Вычисление ожидаемого результата вручную или с помощью встроенных функций
    # Преобразуем числители и знаменатели в целые числа
    num1 = int(''.join(map(str, multiplier_one.num.array))) * (1 if multiplier_one.num.sign == 0 else -1)
    den1 = int(''.join(map(str, multiplier_one.den.array)))

    num2 = int(''.join(map(str, multiplier_two.num.array))) * (1 if multiplier_two.num.sign == 0 else -1)
    den2 = int(''.join(map(str, multiplier_two.den.array)))

    # Умножение числителей и знаменателей
    product_num = num1 * num2
    product_den = den1 * den2

    # Сокращение дроби
    from math import gcd
    common_div = gcd(abs(product_num), product_den)
    reduced_num = product_num // common_div
    reduced_den = product_den // common_div

    # Определение знака
    expected_sign = 0 if reduced_num >= 0 else 1

    # Подготовка массивов цифр
    expected_num = list(map(int, str(abs(reduced_num))))
    expected_den = list(map(int, str(reduced_den)))

    expected = build_rat(
        num_array=expected_num,
        num_n=len(expected_num),
        num_sign=expected_sign,
        den_array=expected_den,
        den_n=len(expected_den)
    )

    result = MUL_QQ_Q(multiplier_one, multiplier_two)
    assert result == expected, f"Ожидалось {expected}, получено {result}"
