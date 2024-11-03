# ADD_ZZ_Z_test.py
# Тесты для модуля ADD_ZZ_Z
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from ADD_ZZ_Z import ADD_ZZ_Z  # Импортируем функцию ADD_ZZ_Z
from Types import nat_0, ceil  # Импортируем классы nat_0 и ceil

def test_ADD_ZZ_Z_same_sign_positive():
    # Тест сложения двух положительных чисел
    A = ceil([1, 2, 3], 3, 0)  # Число +123
    B = ceil([4, 5, 6], 3, 0)  # Число +456
    result = ADD_ZZ_Z(A, B)
    expected = ceil([5, 7, 9], 3, 0)  # Ожидаемое число +579
    assert result == expected

def test_ADD_ZZ_Z_same_sign_negative():
    # Тест сложения двух отрицательных чисел
    A = ceil([1, 2, 3], 3, 1)  # Число -123
    B = ceil([4, 5, 6], 3, 1)  # Число -456
    result = ADD_ZZ_Z(A, B)
    expected = ceil([5, 7, 9], 3, 1)  # Ожидаемое число -579
    assert result == expected

def test_ADD_ZZ_Z_different_signs_positive_result():
    # Тест сложения чисел с разными знаками, результат положительный
    A = ceil([5, 0, 0], 3, 0)  # Число +500
    B = ceil([2, 5, 0], 3, 1)  # Число -250
    result = ADD_ZZ_Z(A, B)
    expected = ceil([2, 5, 0], 3, 0)  # Ожидаемое число +250
    assert result == expected

def test_ADD_ZZ_Z_different_signs_negative_result():
    # Тест сложения чисел с разными знаками, результат отрицательный
    A = ceil([2, 5, 0], 3, 1)  # Число -250
    B = ceil([1, 0, 0], 3, 0)  # Число +100
    result = ADD_ZZ_Z(A, B)
    expected = ceil([1, 5, 0], 3, 1)  # Ожидаемое число -150
    assert result == expected

def test_ADD_ZZ_Z_zero_result():
    # Тест, когда сумма равна нулю
    A = ceil([1, 2, 3], 3, 0)  # Число +123
    B = ceil([1, 2, 3], 3, 1)  # Число -123
    result = ADD_ZZ_Z(A, B)
    expected = ceil([0], 1, 0)  # Ожидаемое число 0
    assert result == expected

def test_ADD_ZZ_Z_large_numbers():
    # Тест с большими числами
    A = ceil([9]*1000, 1000, 0)  # Положительное число с 1000 девятками
    B = ceil([1], 1, 0)          # Число +1
    result = ADD_ZZ_Z(A, B)
    expected = ceil([1] + [0]*1000, 1001, 0)  # Ожидаемое число с 1 и 1000 нулями
    assert result == expected

def test_ADD_ZZ_Z_negative_and_positive_large():
    # Тест сложения большого отрицательного и положительного числа
    A = ceil([1] + [0]*1000, 1001, 1)  # Число -1000...0 (1 и
