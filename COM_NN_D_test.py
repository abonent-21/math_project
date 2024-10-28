# COM_NN_D_test.py
# Тесты для модуля COM_NN_D
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from COM_NN_D import COM_NN_D
from Types import nat_0

def test_COM_NN_D_equal():
    # Тест на равенство чисел
    A = nat_0([1,2,3], 3)
    B = nat_0([1,2,3], 3)
    assert COM_NN_D(A, B) == 0

def test_COM_NN_D_greater():
    # Тест когда первое число больше второго
    A = nat_0([1,2,4], 3)
    B = nat_0([1,2,3], 3)
    assert COM_NN_D(A, B) == 2

def test_COM_NN_D_less():
    # Тест когда первое число меньше второго
    A = nat_0([1,2,3], 3)
    B = nat_0([1,2,4], 3)
    assert COM_NN_D(A, B) == 1

def test_COM_NN_D_different_lengths():
    # Тесты с числами разной длины
    A = nat_0([1,2,3,4], 4)
    B = nat_0([1,2,3], 3)
    assert COM_NN_D(A, B) == 2

    A = nat_0([1,2,3], 3)
    B = nat_0([1,2,3,4], 4)
    assert COM_NN_D(A, B) == 1

def test_COM_NN_D_leading_zeros():
    # Тесты с ведущими нулями
    A = nat_0([0,0,1,2,3], 5)
    B = nat_0([1,2,3], 3)
    assert COM_NN_D(A, B) == 2  # Оба числа равны после удаления ведущих нулей

    A = nat_0([0,0,1,2,4], 5)
    B = nat_0([1,2,3], 3)
    assert COM_NN_D(A, B) == 2  # A > B после удаления ведущих нулей

    A = nat_0([0,0,1,2,3], 5)
    B = nat_0([0,0,1,2,4], 5)
    assert COM_NN_D(A, B) == 1  # A < B после удаления ведущих нулей

def test_COM_NN_D_zero():
    # Тесты когда одно или оба числа равны нулю
    A = nat_0([0],1)
    B = nat_0([0],1)
    assert COM_NN_D(A, B) == 0

    A = nat_0([0],1)
    B = nat_0([1],1)
    assert COM_NN_D(A, B) == 1

    A = nat_0([1],1)
    B = nat_0([0],1)
    assert COM_NN_D(A, B) == 2

def test_COM_NN_D_large_numbers():
    # Тесты с большими числами
    A = nat_0([9]*1000, 1000)
    B = nat_0([9]*999 + [8], 1000)
    assert COM_NN_D(A, B) == 2
    assert COM_NN_D(B, A) == 1
    assert COM_NN_D(A, A) == 0
