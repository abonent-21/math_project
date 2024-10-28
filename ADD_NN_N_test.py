<<<<<<< HEAD
# ADD_NN_N_test.py
# Тесты для модуля ADD_NN_N
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from ADD_NN_N import ADD_NN_N
from Types import nat_0

def test_ADD_NN_N_simple():
    # Простые тесты сложения
    A = nat_0([1,2,3],3)
    B = nat_0([4,5,6],3)
    result = ADD_NN_N(A,B)
    expected = nat_0([5,7,9],3)
    assert result == expected

    A = nat_0([9,9,9],3)
    B = nat_0([1],1)
    result = ADD_NN_N(A,B)
    expected = nat_0([1,0,0,0],4)
    assert result == expected

    A = nat_0([1,0,0],3)
    B = nat_0([0],1)
    result = ADD_NN_N(A,B)
    expected = nat_0([1,0,0],3)
    assert result == expected

def test_ADD_NN_N_different_lengths():
    # Тесты с числами разной длины
    A = nat_0([1,2,3],3)
    B = nat_0([4,5],2)
    result = ADD_NN_N(A,B)
    expected = nat_0([1,6,8],3)
    assert result == expected

    A = nat_0([9,9],2)
    B = nat_0([1,1,1],3)
    result = ADD_NN_N(A,B)
    expected = nat_0([2,1,0],3)  # Исправленный ожидаемый результат
    assert result == expected

def test_ADD_NN_N_large_numbers():
    # Тест с большими числами
    A = nat_0([9]*1000,1000)
    B = nat_0([1],1)
    result = ADD_NN_N(A,B)
    expected = nat_0([1] + [0]*1000,1001)
    assert result == expected

def test_ADD_NN_N_zero():
    # Тесты с нулем
    A = nat_0([0],1)
    B = nat_0([0],1)
    result = ADD_NN_N(A,B)
    expected = nat_0([0],1)
    assert result == expected

    A = nat_0([1,2,3],3)
    B = nat_0([0],1)
    result = ADD_NN_N(A,B)
    expected = nat_0([1,2,3],3)
    assert result == expected

    A = nat_0([0],1)
    B = nat_0([1,2,3],3)
    result = ADD_NN_N(A,B)
    expected = nat_0([1,2,3],3)
    assert result == expected

def test_ADD_NN_N_leading_zeros():
    # Тест с ведущими нулями
    A = nat_0([0,0,1,2,3],5)
    B = nat_0([0,0,4,5,6],5)
    result = ADD_NN_N(A,B)
    expected = nat_0([0,0,5,7,9],5)
    assert result == expected
=======
# ADD_NN_N_test.py
# Тесты для модуля ADD_NN_N
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from ADD_NN_N import ADD_NN_N

def test_ADD_NN_N_simple():
    # Простые тесты сложения
    assert ADD_NN_N([1,2,3], [4,5,6]) == [5,7,9]
    assert ADD_NN_N([9,9,9], [1]) == [1,0,0,0]
    assert ADD_NN_N([1,0,0], [0]) == [1,0,0]

def test_ADD_NN_N_different_lengths():
    # Тесты с числами разной длины
    assert ADD_NN_N([1,2,3], [4,5]) == [1,6,8]
    assert ADD_NN_N([9,9], [1,1,1]) == [1,1,0,0]

def test_ADD_NN_N_large_numbers():
    # Тест с большими числами
    A = [9]*1000
    B = [1]
    result = [1] + [0]*1000
    assert ADD_NN_N(A, B) == result

def test_ADD_NN_N_zero():
    # Тесты с нулем
    assert ADD_NN_N([0], [0]) == [0]
    assert ADD_NN_N([1,2,3], [0]) == [1,2,3]
    assert ADD_NN_N([0], [1,2,3]) == [1,2,3]

def test_ADD_NN_N_leading_zeros():
    # Тест с ведущими нулями
    assert ADD_NN_N([0,0,1,2,3], [0,0,4,5,6]) == [0,0,5,7,9]
>>>>>>> f2084a7bb46ccf33f4f3e3ee438e972ad1923261
