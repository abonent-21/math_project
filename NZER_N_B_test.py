<<<<<<< HEAD
# NZER_N_B_test.py
# Тесты для модуля NZER_N_B
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from NZER_N_B import NZER_N_B
from Types import nat_0

def test_NZER_N_B_zero():
    # Тесты когда число равно нулю
    A = nat_0([0], 1)
    assert NZER_N_B(A) == False

    A = nat_0([0,0,0], 3)
    assert NZER_N_B(A) == False

def test_NZER_N_B_nonzero():
    # Тесты когда число не равно нулю
    A = nat_0([1],1)
    assert NZER_N_B(A) == True

    A = nat_0([0,0,1], 3)
    assert NZER_N_B(A) == True

    A = nat_0([0,0,0,2], 4)
    assert NZER_N_B(A) == True

def test_NZER_N_B_large_number():
    # Тест с большим числом
    A = nat_0([0]*1000 + [1], 1001)
    assert NZER_N_B(A) == True

def test_NZER_N_B_all_nines():
    # Тест когда все цифры - девятки
    A = nat_0([9]*1000, 1000)
    assert NZER_N_B(A) == True
=======
# NZER_N_B_test.py
# Тесты для модуля NZER_N_B
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from NZER_N_B import NZER_N_B

def test_NZER_N_B_zero():
    # Тесты когда число равно нулю
    assert NZER_N_B([0]) == False
    assert NZER_N_B([0,0,0]) == False

def test_NZER_N_B_nonzero():
    # Тесты когда число не равно нулю
    assert NZER_N_B([1]) == True
    assert NZER_N_B([0,0,1]) == True
    assert NZER_N_B([0,0,0,2]) == True

def test_NZER_N_B_large_number():
    # Тест с большим числом
    A = [0]*1000 + [1]
    assert NZER_N_B(A) == True

def test_NZER_N_B_all_nines():
    # Тест когда все цифры - девятки
    A = [9]*1000
    assert NZER_N_B(A) == True
>>>>>>> f2084a7bb46ccf33f4f3e3ee438e972ad1923261
