# test_SUB_QQ_Q.py

import pytest
from SUB_QQ_Q import SUB_QQ_Q
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


def test_sub_same_denominator(build_rat):
    """
    Тестирование вычитания дробей с одинаковыми знаменателями.
    (3/4) - (1/4) = (2/4) -> сокращается до (1/2)
    """
    minuend = build_rat(num_array=[3], num_n=1, num_sign=0, den_array=[4], den_n=1)
    subtrahend = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[4], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[2], den_n=1)

    result = SUB_QQ_Q(minuend, subtrahend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_sub_different_denominator(build_rat):
    """
    Тестирование вычитания дробей с разными знаменателями.
    (1/2) - (1/3) = (3/6 - 2/6) = (1/6)
    """
    minuend = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[2], den_n=1)
    subtrahend = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[3], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[6], den_n=1)

    result = SUB_QQ_Q(minuend, subtrahend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_sub_negative_result(build_rat):
    """
    Тестирование вычитания дробей, результат которой отрицателен.
    (1/4) - (3/4) = (-2/4) -> сокращается до (-1/2)
    """
    minuend = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[4], den_n=1)
    subtrahend = build_rat(num_array=[3], num_n=1, num_sign=0, den_array=[4], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=1, den_array=[2], den_n=1)

    result = SUB_QQ_Q(minuend, subtrahend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_sub_zero_numerator(build_rat):
    """
    Тестирование вычитания дробей, где минуенд имеет нулевой числитель.
    (0/1) - (1/2) = (-1/2)
    """
    minuend = build_rat(num_array=[0], num_n=1, num_sign=0, den_array=[1], den_n=1)
    subtrahend = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[2], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=1, den_array=[2], den_n=1)

    result = SUB_QQ_Q(minuend, subtrahend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_sub_result_reduction(build_rat):
    """
    Тестирование, что результат сокращается до несократимой дроби.
    (4/6) - (2/6) = (2/6) -> (1/3)
    """
    minuend = build_rat(num_array=[4], num_n=1, num_sign=0, den_array=[6], den_n=1)
    subtrahend = build_rat(num_array=[2], num_n=1, num_sign=0, den_array=[6], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[3], den_n=1)

    result = SUB_QQ_Q(minuend, subtrahend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_sub_mixed_signs(build_rat):
    """
    Тестирование вычитания дробей с разными знаками.
    (1/3) - (-1/6) = (1/3 + 1/6) = (2/6 + 1/6) = (3/6) -> (1/2)
    """
    minuend = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[3], den_n=1)
    subtrahend = build_rat(num_array=[1], num_n=1, num_sign=1, den_array=[6], den_n=1)
    expected = build_rat(num_array=[1], num_n=1, num_sign=0, den_array=[2], den_n=1)

    result = SUB_QQ_Q(minuend, subtrahend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"


def test_sub_large_numbers(build_rat):
    """
    Тестирование вычитания дробей с большими числами.
    (789/101112) - (123/456) -> проверка на большие значения и сокращение
    """
    minuend = build_rat(num_array=[7, 8, 9], num_n=3, num_sign=0, den_array=[1, 0, 1, 1, 1, 2], den_n=6)
    subtrahend = build_rat(num_array=[1, 2, 3], num_n=3, num_sign=0, den_array=[4, 5, 6], den_n=3)

    # Вычисление ожидаемого результата вручную или с помощью встроенных функций
    # Преобразуем числители и знаменатели в целые числа
    num1 = int(''.join(map(str, minuend.num.array))) * (1 if minuend.num.sign == 0 else -1)
    den1 = int(''.join(map(str, minuend.den.array)))

    num2 = int(''.join(map(str, subtrahend.num.array))) * (1 if subtrahend.num.sign == 0 else -1)
    den2 = int(''.join(map(str, subtrahend.den.array)))

    # Находим НОК знаменателей
    from math import gcd
    lcm_den = den1 * den2 // gcd(den1, den2)

    # Приводим числители к общему знаменателю и вычитаем
    sum_num = num1 * (lcm_den // den1) - num2 * (lcm_den // den2)

    # Сокращение
    common_div = gcd(abs(sum_num), lcm_den)
    sum_num_reduced = sum_num // common_div
    lcm_den_reduced = lcm_den // common_div

    # Определение знака
    expected_sign = 0 if sum_num_reduced >= 0 else 1

    # Подготовка массивов цифр
    expected_num = list(map(int, str(abs(sum_num_reduced))))
    expected_den = list(map(int, str(lcm_den_reduced)))

    expected = build_rat(
        num_array=expected_num,
        num_n=len(expected_num),
        num_sign=expected_sign,
        den_array=expected_den,
        den_n=len(expected_den)
    )

    result = SUB_QQ_Q(minuend, subtrahend)
    assert result == expected, f"Ожидалось {expected}, получено {result}"
