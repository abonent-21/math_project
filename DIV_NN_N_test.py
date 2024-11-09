# test_DIV_NN_N.py

import pytest
from Types import nat_0
from DIV_NN_N import DIV_NN_N


def nat0_to_int(nat: nat_0) -> int:
    """
    Преобразует объект nat_0 в целое число.

    :param nat: Объект nat_0
    :return: Целое число, представленное объектом nat_0
    """
    return int(''.join(map(str, nat.array)))


def int_to_nat0(number: int) -> nat_0:
    """
    Преобразует целое число в объект nat_0.

    :param number: Целое число (натуральное, включая 0)
    :return: Объект nat_0, представляющий число
    """
    if number == 0:
        return nat_0([0], 1)
    digits = [int(d) for d in str(number)]
    return nat_0(digits, len(digits))


def test_division_basic():
    """
    Базовый тест деления: 123 / 10 = 12
    """
    A = nat_0([1, 2, 3], 3)  # 123
    B = nat_0([1, 0], 2)  # 10
    expected_result = nat_0([1, 2], 2)  # 12
    assert DIV_NN_N(A, B) == expected_result


def test_division_exact():
    """
    Тест точного деления: 120 / 10 = 12
    """
    A = nat_0([1, 2, 0], 3)  # 120
    B = nat_0([1, 0], 2)  # 10
    expected_result = nat_0([1, 2], 2)  # 12
    assert DIV_NN_N(A, B) == expected_result


def test_division_with_remainder():
    """
    Тест деления с остатком: 100 / 3 = 33
    """
    A = nat_0([1, 0, 0], 3)  # 100
    B = nat_0([3], 1)  # 3
    expected_result = nat_0([3, 3], 2)  # 33
    assert DIV_NN_N(A, B) == expected_result


def test_division_large_numbers():
    """
    Тест деления больших чисел: 10000 / 25 = 400
    """
    A = nat_0([1, 0, 0, 0, 0], 5)  # 10000
    B = nat_0([2, 5], 2)  # 25
    expected_result = nat_0([4, 0, 0], 3)  # 400
    assert DIV_NN_N(A, B) == expected_result


def test_division_with_one():
    """
    Тест деления на 1: 987 / 1 = 987
    """
    A = nat_0([9, 8, 7], 3)  # 987
    B = nat_0([1], 1)  # 1
    expected_result = A  # Деление на 1 должно вернуть само число
    assert DIV_NN_N(A, B) == expected_result


def test_division_same_numbers():
    """
    Тест деления одинаковых чисел: 75 / 75 = 1
    """
    A = nat_0([7, 5], 2)  # 75
    B = nat_0([7, 5], 2)  # 75
    expected_result = nat_0([1], 1)  # 1
    assert DIV_NN_N(A, B) == expected_result


def test_division_smaller_divisor():
    """
    Тест деления, когда делитель больше делимого: 2 / 5 = 0
    """
    A = nat_0([2], 1)  # 2
    B = nat_0([5], 1)  # 5
    expected_result = nat_0([0], 1)  # 0
    assert DIV_NN_N(A, B) == expected_result


def test_division_zero_result():
    """
    Тест деления нуля на число: 0 / 9 = 0
    """
    A = nat_0([0], 1)  # 0
    B = nat_0([9], 1)  # 9
    expected_result = nat_0([0], 1)  # 0
    assert DIV_NN_N(A, B) == expected_result


def test_division_large_divisor():
    """
    Тест деления с делителем больше, чем делимое: 500 / 1000 = 0
    """
    A = nat_0([5, 0, 0], 3)  # 500
    B = nat_0([1, 0, 0, 0], 4)  # 1000
    expected_result = nat_0([0], 1)  # 0
    assert DIV_NN_N(A, B) == expected_result


def test_division_zero_divisor():
    """
    Тест деления на ноль: 50 / 0 -> ValueError
    """
    A = nat_0([5, 0], 2)  # 50
    B = nat_0([0], 1)  # 0 (некорректный делитель)
    with pytest.raises(ValueError, match="Делитель не может быть нулем"):
        DIV_NN_N(A, B)


# Дополнительные Тесты для Больших Чисел

def test_division_large_number_divided_by_small_number():
    """
    Тест деления большого числа на малое число: 12345678901234567890 / 10 = 1234567890123456789
    """
    A_int = 12345678901234567890
    B_int = 10
    expected_int = A_int // B_int
    A = int_to_nat0(A_int)
    B = int_to_nat0(B_int)
    expected_result = int_to_nat0(expected_int)
    assert DIV_NN_N(A, B) == expected_result


def test_division_large_number_divided_by_large_number():
    """
    Тест деления двух очень больших чисел: 98765432109876543210 / 12345678901234567890 = 8
    """
    A_int = 98765432109876543210
    B_int = 12345678901234567890
    expected_int = A_int // B_int  # 8
    A = int_to_nat0(A_int)
    B = int_to_nat0(B_int)
    expected_result = int_to_nat0(expected_int)
    assert DIV_NN_N(A, B) == expected_result


def test_division_large_numbers_with_remainder():
    """
    Тест деления больших чисел с остатком: 10000000000000000000 / 3 = 3333333333333333333
    """
    A_int = 10000000000000000000
    B_int = 3
    expected_int = A_int // B_int  # 3333333333333333333
    A = int_to_nat0(A_int)
    B = int_to_nat0(B_int)
    expected_result = int_to_nat0(expected_int)
    assert DIV_NN_N(A, B) == expected_result


def test_division_large_numbers_exact_division():
    """
    Тест деления больших чисел без остатка: 1000000000000 / 1000 = 1000000000
    """
    A_int = 1000000000000
    B_int = 1000
    expected_int = A_int // B_int  # 1000000000
    A = int_to_nat0(A_int)
    B = int_to_nat0(B_int)
    expected_result = int_to_nat0(expected_int)
    assert DIV_NN_N(A, B) == expected_result


def test_division_large_numbers_zero_result():
    """
    Тест деления больших чисел, когда делитель больше делимого: 999999999999 / 1000000000000 = 0
    """
    A_int = 999999999999
    B_int = 1000000000000
    expected_int = A_int // B_int  # 0
    A = int_to_nat0(A_int)
    B = int_to_nat0(B_int)
    expected_result = int_to_nat0(expected_int)
    assert DIV_NN_N(A, B) == expected_result
