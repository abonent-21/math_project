# test_ADD_QQ_Q.py

import pytest
from ADD_QQ_Q import ADD_QQ_Q
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


def test_add_same_denominator(build_rat):
    """
    Тестирование сложения дробей с одинаковыми знаменателями.
    (1/4) + (1/4) = (2/4) -> сокращается до (1/2)
    """
    summand = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[4], den_n=1)
    addend = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[4], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[2], den_n=1)

    result = ADD_QQ_Q(summand, addend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_add_different_denominator(build_rat):
    """
    Тестирование сложения дробей с разными знаменателями.
    (1/3) + (1/6) = (2/6 + 1/6) = (3/6) -> сокращается до (1/2)
    """
    summand = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[3], den_n=1)
    addend = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[6], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[2], den_n=1)

    result = ADD_QQ_Q(summand, addend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_add_negative_numerator(build_rat):
    """
    Тестирование сложения дробей с отрицательными числителями.
    (-1/4) + (1/4) = (0/4) -> (0/1)
    """
    summand = build_rat(num_array=[1], num_n=1, num_sign=1, den_array=[4], den_n=1)
    addend = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[4], den_n=1)
    expected = build_rat(num_array=[0], num_n=1, num_sign=0, den_array=[1], den_n=1)

    result = ADD_QQ_Q(summand, addend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_add_zero_numerator(build_rat):
    """
    Тестирование сложения дробей, где одно из чисел имеет нулевой числитель.
    (0/1) + (1/2) = (1/2)
    """
    summand = build_rat(num_array=[0], num_n=1, num_sign=0, den_array=[1], den_n=1)
    addend = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[2], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[2], den_n=1)

    result = ADD_QQ_Q(summand, addend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_add_result_reduction(build_rat):
    """
    Тестирование, что результат сокращается до несократимой дроби.
    (2/4) + (2/4) = (4/4) -> (1/1)
    """
    summand = build_rat(num_array=[2], num_n=1, num_sign=0, den_array=[4], den_n=1)
    addend = build_rat(num_array=[2], num_n=1, num_sign=0, den_array=[4], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[1], den_n=1)

    result = ADD_QQ_Q(summand, addend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_add_mixed_signs(build_rat):
    """
    Тестирование сложения дробей с разными знаками.
    (1/3) + (-1/6) = (2/6 - 1/6) = (1/6)
    """
    summand = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[3], den_n=1)
    addend = build_rat(num_array=[1], num_n=1, num_sign=1, den_array=[6], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[6], den_n=1)

    result = ADD_QQ_Q(summand, addend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_add_large_numbers(build_rat):
    """
    Тестирование сложения дробей с большими числами.
    (123/456) + (789/101112) -> проверка на большие значения и сокращение
    """
    summand = build_rat(num_array=[1, 2, 3], num_n=3, num_sign=0, den_array=[4, 5, 6], den_n=3)
    addend = build_rat(num_array=[7, 8, 9], num_n=3, num_sign=0, den_array=[1, 0, 1, 1, 1, 2], den_n=6)

    # Для корректного теста необходимо вычислить ожидаемый результат вручную или с помощью другой функции
    # Например, используем Python для вычисления:

    # Преобразуем числители и знаменатели в целые числа
    num1 = int(''.join(map(str, summand.num.array))) * (1 if summand.num.sign == 0 else -1)
    den1 = int(''.join(map(str, summand.den.array)))

    num2 = int(''.join(map(str, addend.num.array))) * (1 if addend.num.sign == 0 else -1)
    den2 = int(''.join(map(str, addend.den.array)))

    # Сложение дробей
    from math import gcd
    lcm_den = den1 * den2 // gcd(den1, den2)
    sum_num = num1 * (lcm_den // den1) + num2 * (lcm_den // den2)

    # Сокращение
    common_div = gcd(abs(sum_num), lcm_den)
    sum_num_reduced = sum_num // common_div
    lcm_den_reduced = lcm_den // common_div

    # Подготовка ожидаемого результата
    expected_sign = 0 if sum_num_reduced >= 0 else 1
    expected_num = list(map(int, str(abs(sum_num_reduced))))
    expected_den = list(map(int, str(lcm_den_reduced)))

    expected = build_rat(
        num_array=expected_num,
        num_n=len(expected_num),
        num_sign=expected_sign,
        den_array=expected_den,
        den_n=len(expected_den)
    )

    result = ADD_QQ_Q(summand, addend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"
