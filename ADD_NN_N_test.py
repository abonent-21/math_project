# ADD_NN_N_test.py
# Тесты для модуля ADD_NN_N
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from ADD_NN_N import ADD_NN_N  # Импортируем функцию ADD_NN_N
from Types import nat_0        # Импортируем класс nat_0

def test_ADD_NN_N_simple():
    # Простые тесты сложения
    A = nat_0([1, 2, 3], 3)             # Число 123
    B = nat_0([4, 5, 6], 3)             # Число 456
    result = ADD_NN_N(A, B)             # Суммируем
    expected = nat_0([5, 7, 9], 3)      # Ожидаемое число 579
    assert result == expected

    A = nat_0([9, 9, 9], 3)             # Число 999
    B = nat_0([1], 1)                   # Число 1
    result = ADD_NN_N(A, B)             # Суммируем
    expected = nat_0([1, 0, 0, 0], 4)   # Ожидаемое число 1000
    assert result == expected

    A = nat_0([1, 0, 0], 3)             # Число 100
    B = nat_0([0], 1)                   # Число 0
    result = ADD_NN_N(A, B)             # Суммируем
    expected = nat_0([1, 0, 0], 3)      # Ожидаемое число 100
    assert result == expected

def test_ADD_NN_N_different_lengths():
    # Тесты с числами разной длины
    A = nat_0([1, 2, 3], 3)             # Число 123
    B = nat_0([4, 5], 2)                # Число 45
    result = ADD_NN_N(A, B)             # Суммируем
    expected = nat_0([1, 6, 8], 3)      # Ожидаемое число 168
    assert result == expected

    A = nat_0([9, 9], 2)                # Число 99
    B = nat_0([1, 1, 1], 3)             # Число 111
    result = ADD_NN_N(A, B)             # Суммируем
    expected = nat_0([2, 1, 0], 3)      # Ожидаемое число 210
    assert result == expected

def test_ADD_NN_N_large_numbers():
    # Тест с большими числами
    A = nat_0([9]*1000, 1000)           # Число с 1000 девятками
    B = nat_0([1], 1)                   # Число 1
    result = ADD_NN_N(A, B)             # Суммируем
    expected = nat_0([1] + [0]*1000, 1001)  # Ожидаемое число с 1 и 1000 нулями
    assert result == expected

def test_ADD_NN_N_zero():
    # Тесты с нулем
    A = nat_0([0], 1)
    B = nat_0([0], 1)
    result = ADD_NN_N(A, B)
    expected = nat_0([0], 1)
    assert result == expected

    A = nat_0([1, 2, 3], 3)
    B = nat_0([0], 1)
    result = ADD_NN_N(A, B)
    expected = nat_0([1, 2, 3], 3)
    assert result == expected

    A = nat_0([0], 1)
    B = nat_0([1, 2, 3], 3)
    result = ADD_NN_N(A, B)
    expected = nat_0([1, 2, 3], 3)
    assert result == expected

# Тест с ведущими нулями удален, так как ведущих нулей быть не должно.
