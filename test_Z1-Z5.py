# Автор: Козлов Георгий. Группа - ПМИ-3381

import pytest
from Types import ceil, nat_0, dig
from ABS_Z_Z import ABS_Z_Z
from POZ_Z_D import POZ_Z_D
from MUL_ZM_Z import MUL_ZM_Z
from TRANS_N_Z import TRANS_N_Z
from TRANS_Z_N import TRANS_Z_N

# ABS_Z_Z
def test_abs_positive_number():
    # Тест для положительного числа
    number = ceil([1, 2, 3], 3, 0)  # Представляет положительное число 123
    result = ABS_Z_Z(number)
    assert result == ceil([1, 2, 3], 3, 0), "ABS_Z_Z должна возвращать число без изменений для положительных чисел"


def test_abs_negative_number():
    # Тест для отрицательного числа
    number = ceil([1, 2, 3], 3, 1)  # Представляет отрицательное число -123
    result = ABS_Z_Z(number)
    assert result == ceil([1, 2, 3], 3, 0), "ABS_Z_Z должна возвращать положительное значение для отрицательных чисел"


def test_abs_zero():
    # Тест для нуля
    number = ceil([0], 1, 0)  # Представляет число 0
    result = ABS_Z_Z(number)
    assert result == ceil([0], 1, 0), "ABS_Z_Z должна возвращать 0 без изменений"

#POZ_Z_D

def test_poz_positive_number():
    # Тест для положительного числа
    number = ceil([1, 2, 3], 3, 0)  # Представляет положительное число 123
    result = POZ_Z_D(number)
    assert result == dig(2), "POZ_Z_D должна возвращать 2 для положительных чисел"

def test_poz_negative_number():
    # Тест для отрицательного числа
    number = ceil([1, 2, 3], 3, 1)  # Представляет отрицательное число -123
    result = POZ_Z_D(number)
    assert result == dig(1), "POZ_Z_D должна возвращать 1 для отрицательных чисел"

def test_poz_zero():
    # Тест для нуля
    number = ceil([0], 1, 0)  # Представляет число 0
    result = POZ_Z_D(number)
    assert result == dig(0), "POZ_Z_D должна возвращать 0 для числа 0"

#MUL_ZM_Z

def test_mul_zm_positive_number():
    # Тест для положительного числа
    number = ceil([1, 2, 3], 3, 0)  # Представляет положительное число 123
    result = MUL_ZM_Z(number)
    assert result == ceil([1, 2, 3], 3, 1), "MUL_ZM_Z должна возвращать отрицательное число для положительного числа"


def test_mul_zm_negative_number():
    # Тест для отрицательного числа
    number = ceil([1, 2, 3], 3, 1)  # Представляет отрицательное число -123
    result = MUL_ZM_Z(number)
    assert result == ceil([1, 2, 3], 3, 0), "MUL_ZM_Z должна возвращать положительное число для отрицательного числа"


def test_mul_zm_zero():
    # Тест для нуля
    number = ceil([0], 1, 0)  # Представляет число 0
    result = MUL_ZM_Z(number)
    assert result == ceil([0], 1, 0), "MUL_ZM_Z должна возвращать 0 без изменений"


# TRANS_N_Z

def test_trans_nz_small_number():
    # Тест для маленького натурального числа
    number = nat_0([1, 2, 3], 3)  # Представляет натуральное число 123
    result = TRANS_N_Z(number)
    expected = ceil(array=[1, 2, 3], n=3, sign=0)  # Ожидаемое значение (положительное целое)
    assert result == expected, "TRANS_N_Z должна возвращать правильное целое число для натурального числа"


def test_trans_nz_zero():
    # Тест для нуля как натурального числа (согласно определению nat_0, он не может быть нулем, но для теста добавим)
    number = nat_0([0], 1)  # Представляет натуральное число 0
    result = TRANS_N_Z(number)
    expected = ceil(array=[0], n=1, sign=0)  # Ожидаемое значение (ноль)
    assert result == expected, "TRANS_N_Z должна возвращать 0 для натурального числа 0"


def test_trans_nz_large_number():
    # Тест для большого натурального числа
    number = nat_0([9, 8, 7], 3)  # Представляет натуральное число 987
    result = TRANS_N_Z(number)
    expected = ceil(array=[9, 8, 7], n=3, sign=0)  # Ожидаемое значение (положительное целое)
    assert result == expected, "TRANS_N_Z должна возвращать правильное целое число для большого натурального числа"


# TRANS_Z_N

def test_trans_zn_positive_number():
    # Тест для положительного целого числа
    number = ceil([1, 2, 3], 3, 0)  # Представляет положительное целое число 123
    result = TRANS_Z_N(number)
    expected = nat_0(array=[1, 2, 3], n=3)  # Ожидаемое значение (натуральное число 123)
    assert result == expected, "TRANS_Z_N должна возвращать правильное натуральное число для положительного целого числа"


def test_trans_zn_zero():
    # Тест для нуля как целого числа
    number = ceil([0], 1, 0)  # Представляет целое число 0
    result = TRANS_Z_N(number)
    expected = nat_0(array=[0], n=1)  # Ожидаемое значение (натуральное число 0, если это допустимо)
    assert result == expected, "TRANS_Z_N должна возвращать 0 для целого числа 0"


def test_trans_zn_large_number():
    # Тест для большого положительного целого числа
    number = ceil([9, 8, 7], 3, 0)  # Представляет целое число 987
    result = TRANS_Z_N(number)
    expected = nat_0(array=[9, 8, 7], n=3)  # Ожидаемое значение (натуральное число 987)
    assert result == expected, "TRANS_Z_N должна возвращать правильное натуральное число для большого целого числа"


def test_trans_zn_negative_number():
    # Тест для отрицательного целого числа (должен быть обработан отдельно, если это предусмотрено)
    number = ceil([1, 2, 3], 3, 1)  # Представляет отрицательное целое число -123
    with pytest.raises(AssertionError):
        TRANS_Z_N(number)  # Ожидается, что будет ошибка при попытке преобразования отрицательного числа
