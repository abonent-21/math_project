# test_GCF_NN_N.py

import pytest
from GCF_NN_N import GCF_NN_N
from Types import nat_0, dig

def test_gcd_both_zero():
    """
    Проверка, что функция вызывает ValueError при вводе (0, 0)
    """
    A = nat_0([0], 1)
    B = nat_0([0], 1)
    with pytest.raises(ValueError):
        GCF_NN_N(A, B)

def test_gcd_first_zero():
    """
    Проверка, что GCF_NN_N(0, B) возвращает B
    """
    B1 = nat_0([5], 1)      # Представляет число 5
    B2 = nat_0([1, 2, 3], 3)  # Представляет число 123
    A = nat_0([0], 1)
    assert GCF_NN_N(A, B1) == B1
    assert GCF_NN_N(A, B2) == B2

def test_gcd_second_zero():
    """
    Проверка, что GCF_NN_N(A, 0) возвращает A
    """
    A1 = nat_0([7], 1)        # Представляет число 7
    A2 = nat_0([4, 5, 6], 3)  # Представляет число 456
    B = nat_0([0], 1)
    assert GCF_NN_N(A1, B) == A1
    assert GCF_NN_N(A2, B) == A2

def test_gcd_same_numbers():
    """
    Проверка, что GCF_NN_N(A, A) возвращает A
    """
    A1 = nat_0([1, 0], 2)    # Представляет число 10
    A2 = nat_0([9, 9, 9], 3) # Представляет число 999
    assert GCF_NN_N(A1, A1) == A1
    assert GCF_NN_N(A2, A2) == A2

def test_gcd_prime_numbers():
    """
    Проверка, что GCF_NN_N двух взаимно простых чисел возвращает 1
    """
    A1 = nat_0([1, 3], 2)    # Представляет число 13
    B1 = nat_0([1, 7], 2)    # Представляет число 17
    A2 = nat_0([7], 1)       # Представляет число 7
    B2 = nat_0([1, 1], 2)    # Представляет число 11
    expected = nat_0([1], 1) # Представляет число 1
    assert GCF_NN_N(A1, B1) == expected
    assert GCF_NN_N(A2, B2) == expected

def test_gcd_with_one():
    """
    Проверка, что GCF_NN_N(1, B) и GCF_NN_N(A, 1) возвращает 1
    """
    A = nat_0([1], 1)          # Представляет число 1
    B1 = nat_0([1, 0, 0], 3)  # Представляет число 100
    B2 = nat_0([4, 5, 6], 3)  # Представляет число 456
    C1 = nat_0([1, 0, 0], 3)  # Представляет число 100
    C2 = nat_0([9, 9, 9], 3)  # Представляет число 999
    expected = nat_0([1], 1)   # Представляет число 1
    assert GCF_NN_N(A, B1) == expected
    assert GCF_NN_N(A, B2) == expected
    assert GCF_NN_N(C1, A) == expected
    assert GCF_NN_N(C2, A) == expected

def test_gcd_multiple_common_divisors():
    """
    Проверка, что GCF_NN_N находит наибольший общий делитель
    """
    A1 = nat_0([1, 2], 2)    # Представляет число 12
    B1 = nat_0([1, 8], 2)    # Представляет число 18
    A2 = nat_0([2, 4], 2)    # Представляет число 24
    B2 = nat_0([3, 6], 2)    # Представляет число 36
    expected1 = nat_0([6], 1)  # Представляет число 6
    expected2 = nat_0([1, 2], 2) # Представляет число 12
    assert GCF_NN_N(A1, B1) == expected1
    assert GCF_NN_N(A2, B2) == expected2

def test_gcd_large_numbers():
    """
    Проверка работы функции с большими числами
    """
    A1 = nat_0([1, 2, 3, 4, 5, 6], 6)       # Представляет число 123456
    B1 = nat_0([7, 8, 9, 0, 1, 2], 6)       # Представляет число 789012
    A2 = nat_0([9, 8, 7, 6, 5, 4, 3, 2, 1], 9)  # Представляет число 987654321
    B2 = nat_0([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)  # Представляет число 123456789
    expected1 = nat_0([1, 2], 2)                  # Представляет число 12
    expected2 = nat_0([9], 1)                     # Представляет число 9
    assert GCF_NN_N(A1, B1) == expected1
    assert GCF_NN_N(A2, B2) == expected2

def test_gcd_with_ones():
    """
    Дополнительная проверка, что GCF_NN_N(1, 1) возвращает 1
    """
    A = nat_0([1], 1)        # Представляет число 1
    B = nat_0([1], 1)        # Представляет число 1
    expected = nat_0([1], 1) # Представляет число 1
    assert GCF_NN_N(A, B) == expected

def test_gcd_with_large_prime():
    """
    Проверка, что GCF_NN_N с большим простым числом и другим числом работает корректно
    """
    A1 = nat_0([1, 0, 0], 3)    # Представляет число 100
    B1 = nat_0([9, 7], 2)       # Представляет число 97 (простое)
    A2 = nat_0([1, 0, 0, 0], 4) # Представляет число 1000
    B2 = nat_0([9, 9, 7], 3)    # Представляет число 997 (простое)
    expected = nat_0([1], 1)     # Представляет число 1
    assert GCF_NN_N(A1, B1) == expected
    assert GCF_NN_N(A2, B2) == expected
