# ADD_1N_N_test.py
# Тесты для модуля ADD_1N_N
# Автор: Самигулин Д.А. Группа - ПМИ-3381

from ADD_1N_N import ADD_1N_N  # Импортируем функцию ADD_1N_N
from Types import nat_0        # Импортируем класс nat_0
import pytest

def test_ADD_1N_N_simple():
    # Простые тесты
    A = nat_0([1, 2, 3], 3)              # Создаем число 123
    result = ADD_1N_N(A)                 # Добавляем 1
    expected = nat_0([1, 2, 4], 3)       # Ожидаемое число 124
    assert result == expected            # Проверяем равенство

    A = nat_0([9], 1)                    # Создаем число 9
    result = ADD_1N_N(A)                 # Добавляем 1
    expected = nat_0([1, 0], 2)          # Ожидаемое число 10
    assert result == expected

    A = nat_0([0], 1)                    # Создаем число 0
    result = ADD_1N_N(A)                 # Добавляем 1
    expected = nat_0([1], 1)             # Ожидаемое число 1
    assert result == expected

def test_ADD_1N_N_carry_over():
    # Тесты с переносом
    A = nat_0([1, 2, 9], 3)              # Число 129
    result = ADD_1N_N(A)                 # Добавляем 1
    expected = nat_0([1, 3, 0], 3)       # Ожидаемое число 130
    assert result == expected

    A = nat_0([9, 9, 9], 3)              # Число 999
    result = ADD_1N_N(A)                 # Добавляем 1
    expected = nat_0([1, 0, 0, 0], 4)    # Ожидаемое число 1000
    assert result == expected

def test_ADD_1N_N_large_number():
    # Тест с большим числом
    A = nat_0([9]*1000, 1000)            # Число с 1000 девятками
    result = ADD_1N_N(A)                 # Добавляем 1
    expected = nat_0([1] + [0]*1000, 1001)  # Ожидаемое число с 1 и 1000 нулями
    assert result == expected

# Тест с ведущими нулями удален, так как ведущих нулей быть не должно.