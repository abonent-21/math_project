# SUB_NN_N_test.py
# Тесты для модуля SUB_NN_N
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from SUB_NN_N import SUB_NN_N

def test_SUB_NN_N_simple():
    # Простые тесты вычитания
    assert SUB_NN_N([1,2,3], [1,0,0]) == [2,3]
    assert SUB_NN_N([1,0,0,0], [9,9,9]) == [0,0,1]

def test_SUB_NN_N_equal_numbers():
    # Тест вычитания равных чисел
    assert SUB_NN_N([1,2,3], [1,2,3]) == [0]

def test_SUB_NN_N_large_numbers():
    # Тест с большими числами
    A = [1] + [0]*1000
    B = [1]
    result = [9]*1000
    assert SUB_NN_N(A, B) == result

def test_SUB_NN_N_raises_error():
    # Тест на ошибку при A < B
    with pytest.raises(ValueError):
        SUB_NN_N([1,0,0], [1,2,3])

def test_SUB_NN_N_leading_zeros():
    # Тест с ведущими нулями
    assert SUB_NN_N([0,0,1,2,3], [0,0,0,2,3]) == [0,0,1,0,0]
