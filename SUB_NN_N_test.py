# SUB_NN_N_test.py
# Тесты для модуля SUB_NN_N
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from SUB_NN_N import SUB_NN_N
from Types import nat_0

def test_SUB_NN_N_simple():
    # Простые тесты вычитания
    A = nat_0([1,2,3],3)
    B = nat_0([1,0,0],3)
    result = SUB_NN_N(A,B)
    expected = nat_0([0,2,3],3)
    assert result == expected

    A = nat_0([1,0,0,0],4)
    B = nat_0([9,9,9],3)
    result = SUB_NN_N(A,B)
    expected = nat_0([0,0,0,1],4)
    assert result == expected

def test_SUB_NN_N_equal_numbers():
    # Тест вычитания равных чисел
    A = nat_0([1,2,3],3)
    B = nat_0([1,2,3],3)
    result = SUB_NN_N(A,B)
    expected = nat_0([0],1)
    assert result == expected

def test_SUB_NN_N_large_numbers():
    # Тест с большими числами
    A = nat_0([1] + [0]*1000,1001)
    B = nat_0([1],1)
    result = SUB_NN_N(A,B)
    expected = nat_0([0] + [9]*1000,1001)
    assert result == expected

def test_SUB_NN_N_raises_error():
    # Тест на ошибку при A < B
    A = nat_0([1,0,0],3)
    B = nat_0([1,2,3],3)
    with pytest.raises(ValueError):
        SUB_NN_N(A,B)

def test_SUB_NN_N_leading_zeros():
    # Тест с ведущими нулями
    A = nat_0([0, 0, 1, 2, 3], 5)
    B = nat_0([0, 0, 0, 2, 3], 5)
    result = SUB_NN_N(A, B)
    expected = nat_0([0, 0, 1, 0, 0], 5)
    assert result == expected
