# SUB_NN_N_test.py
# Тесты для модуля SUB_NN_N
# Автор: Самигулин Д.А. Группа - ПМИ-3381

import pytest
from SUB_NN_N import SUB_NN_N  # Импортируем функцию SUB_NN_N
from Types import nat_0        # Импортируем класс nat_0

def test_SUB_NN_N_simple():
    # Простые тесты вычитания
    A = nat_0([1, 2, 3], 3)             # Число 123
    B = nat_0([1, 0, 0], 3)             # Число 100
    result = SUB_NN_N(A, B)             # Вычитаем
    expected = nat_0([2, 3], 2)         # Ожидаемый результат 23
    assert result == expected

    A = nat_0([1, 0, 0, 0], 4)          # Число 1000
    B = nat_0([9, 9, 9], 3)             # Число 999
    result = SUB_NN_N(A, B)             # Вычитаем
    expected = nat_0([1], 1)            # Ожидаемый результат 1 (1000 - 999)
    assert result == expected

def test_SUB_NN_N_equal_numbers():
    # Тест вычитания равных чисел
    A = nat_0([1, 2, 3], 3)
    B = nat_0([1, 2, 3], 3)
    result = SUB_NN_N(A, B)
    expected = nat_0([0], 1)
    assert result == expected

def test_SUB_NN_N_large_numbers():
    # Тест с большими числами
    A = nat_0([1] + [0]*1000, 1001)     # Число 1 и 1000 нулей
    B = nat_0([1], 1)                   # Число 1
    result = SUB_NN_N(A, B)
    expected = nat_0([9]*1000, 1000)    # Ожидаемый результат 999...9 (1000 девяток)
    assert result == expected

def test_SUB_NN_N_raises_error():
    # Тест на ошибку при A < B
    A = nat_0([1, 0, 0], 3)
    B = nat_0([1, 2, 3], 3)
    with pytest.raises(ValueError):
        SUB_NN_N(A, B)
