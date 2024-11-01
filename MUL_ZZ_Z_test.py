import pytest
from Types import ceil, nat_0, dig
from MUL_ZZ_Z import MUL_ZZ_Z

# MUL_ZZ_Z
def test_mul_zz_positive_numbers():
    # Тесты для положительных чисел
    a = ceil([1, 2, 3], 3, 0)  # Представляет положительное число 123
    b = ceil([4, 5, 6], 3, 0)  # Представляет положительное число 456
    result = MUL_ZZ_Z(a, b)
    assert result == ceil([5, 6, 0, 8, 8], 5, 0)  # ожидаемое значение 56088

def test_mul_zz_positive_number_and_zero():
    # Тест для положительного числа и нуля
    a = ceil([1, 2, 3], 3, 0)  # Представляет положительное число 123
    b = ceil([0], 1, 0)  # Представляет 0
    result = MUL_ZZ_Z(a, b)
    assert result == ceil([0], 1, 0)  # ожидаемое значение 0

def test_mul_zz_negative_numbers():
    # Тест для отрицательных чисел
    a = ceil([1, 2, 3], 3, 1)  # Представляет отрицательное число -123
    b = ceil([4, 5, 6], 3, 1)  # Представляет отрицательное число -456
    result = MUL_ZZ_Z(a, b)
    assert result == ceil([5, 6, 0, 8, 8], 5, 0)  # ожидаемое значение 56088

def test_mul_zz_negative_and_positive_numbers():
    # Тесты для положительного числа и отрицательного
    a = ceil([1, 2, 3], 3, 0)  # Представляет положительное число 123
    b = ceil([4, 5, 6], 3, 1)  # Представляет отрицательное число -456
    result = MUL_ZZ_Z(a, b)
    assert result == ceil([5, 6, 0, 8, 8], 5, 1)  # ожидаемое значение -56088
