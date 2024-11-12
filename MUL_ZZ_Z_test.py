import pytest
from Types import ceil, nat_0, dig
from MUL_ZZ_Z import MUL_ZZ_Z

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

def test_mul_zz_number_and_one():
    # Тест для отрицательных чисел
    a = ceil([1, 2, 3, 4 , 5], 5, 0)  # Представляет положительное число 12345
    b = ceil([1], 1, 0)  # Представляет положительное число 1
    result = MUL_ZZ_Z(a, b)
    assert result == ceil([1, 2, 3, 4 , 5], 5, 0)  # ожидаемое значение 12345

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

def test_mul_zz_big_size_numbers():
    # Тест для чисел большого размера
    a = ceil([8, 7, 6, 5, 4, 3, 2, 1], 8, 0)  # Представляет положительное число 87654321
    b = ceil([9, 8, 7, 6, 5, 4], 6, 0)        # Представляет положительное число 987654
    result = MUL_ZZ_Z(a, b)
    expected_num = ceil([8, 6, 5, 7, 2, 1, 4, 0, 7, 5, 2, 9, 3, 4], 14, 0)
    assert result == expected_num


if __name__ == "__main__":
    test_mul_zz_positive_numbers()
    test_mul_zz_positive_number_and_zero()
    test_mul_zz_number_and_one()
    test_mul_zz_negative_numbers()
    test_mul_zz_negative_and_positive_numbers()
    test_mul_zz_big_size_numbers()