<<<<<<< HEAD
# ADD_1N_N_test.py
# Тесты для модуля ADD_1N_N
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from ADD_1N_N import ADD_1N_N
from Types import nat_0

def test_ADD_1N_N_simple():
    # Простые тесты
    A = nat_0([1,2,3],3)
    result = ADD_1N_N(A)
    expected = nat_0([1,2,4],3)
    assert result == expected

    A = nat_0([9],1)
    result = ADD_1N_N(A)
    expected = nat_0([1,0],2)
    assert result == expected

    A = nat_0([0],1)
    result = ADD_1N_N(A)
    expected = nat_0([1],1)
    assert result == expected

def test_ADD_1N_N_carry_over():
    # Тесты с переносом
    A = nat_0([1,2,9],3)
    result = ADD_1N_N(A)
    expected = nat_0([1,3,0],3)
    assert result == expected

    A = nat_0([9,9,9],3)
    result = ADD_1N_N(A)
    expected = nat_0([1,0,0,0],4)
    assert result == expected

def test_ADD_1N_N_large_number():
    # Тест с большим числом
    A = nat_0([9]*1000,1000)
    result = ADD_1N_N(A)
    expected = nat_0([1] + [0]*1000, 1001)
    assert result == expected

def test_ADD_1N_N_leading_zeros():
    # Тест с ведущими нулями
    A = nat_0([0,0,1,2,3],5)
    result = ADD_1N_N(A)
    expected = nat_0([0,0,1,2,4],5)
    assert result == expected
=======
# ADD_1N_N_test.py
# Тесты для модуля ADD_1N_N
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from ADD_1N_N import ADD_1N_N

def test_ADD_1N_N_simple():
    # Простые тесты
    assert ADD_1N_N([1,2,3]) == [1,2,4]
    assert ADD_1N_N([9]) == [1,0]
    assert ADD_1N_N([0]) == [1]

def test_ADD_1N_N_carry_over():
    # Тесты с переносом
    assert ADD_1N_N([1,2,9]) == [1,3,0]
    assert ADD_1N_N([9,9,9]) == [1,0,0,0]

def test_ADD_1N_N_large_number():
    # Тест с большим числом
    A = [9]*1000
    result = [1] + [0]*1000
    assert ADD_1N_N(A) == result

def test_ADD_1N_N_leading_zeros():
    # Тест с ведущими нулями
    assert ADD_1N_N([0,0,1,2,3]) == [0,0,1,2,4]
>>>>>>> f2084a7bb46ccf33f4f3e3ee438e972ad1923261
