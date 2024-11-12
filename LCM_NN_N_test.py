# test_LCM_NN_N.py

import pytest
from LCM_NN_N import LCM_NN_N
from Types import nat_0


def nat0_to_int(nat: nat_0) -> int:
    """
    Преобразует объект nat_0 в целое число.

    :param nat: Объект nat_0
    :return: Целое число, представленное объектом nat_0
    """
    return int(''.join(map(str, nat.array)))


def int_to_nat0(number: int) -> nat_0:
    """
    Преобразует целое число в объект nat_0.

    :param number: Целое число (натуральное, включая 0)
    :return: Объект nat_0, представляющий число
    """
    if number == 0:
        return nat_0([0], 1)
    digits = [int(d) for d in str(number)]
    return nat_0(digits, len(digits))


def test_lcm_both_zero():
    """
    Проверка, что функция вызывает ValueError при вводе (0, 0)
    """
    A = nat_0([0], 1)
    B = nat_0([0], 1)
    with pytest.raises(ValueError):
        LCM_NN_N(A, B)


def test_lcm_first_zero():
    """
    Проверка, что LCM_NN_N(0, B) возвращает 0
    """
    A = nat_0([0], 1)
    B1 = nat_0([5], 1)
    B2 = nat_0([1, 2, 3], 3)
    expected = nat_0([0], 1)
    assert LCM_NN_N(A, B1) == expected
    assert LCM_NN_N(A, B2) == expected


def test_lcm_second_zero():
    """
    Проверка, что LCM_NN_N(A, 0) возвращает 0
    """
    B = nat_0([0], 1)
    A1 = nat_0([7], 1)
    A2 = nat_0([4, 5, 6], 3)
    expected = nat_0([0], 1)
    assert LCM_NN_N(A1, B) == expected
    assert LCM_NN_N(A2, B) == expected


def test_lcm_same_numbers():
    """
    Проверка, что LCM_NN_N(A, A) возвращает A
    """
    A1 = nat_0([1, 0], 2)  # 10
    A2 = nat_0([9, 9, 9], 3)  # 999
    assert LCM_NN_N(A1, A1) == A1
    assert LCM_NN_N(A2, A2) == A2


def test_lcm_prime_numbers():
    """
    Проверка, что LCM_NN_N двух взаимно простых чисел равен их произведению
    """
    A1 = nat_0([1, 3], 2)  # 13
    B1 = nat_0([1, 7], 2)  # 17
    expected1 = int_to_nat0(nat0_to_int(A1) * nat0_to_int(B1))  # 221

    A2 = nat_0([7], 1)  # 7
    B2 = nat_0([1, 1], 2)  # 11
    expected2 = int_to_nat0(nat0_to_int(A2) * nat0_to_int(B2))  # 77

    assert LCM_NN_N(A1, B1) == expected1
    assert LCM_NN_N(A2, B2) == expected2


def test_lcm_with_one():
    """
    Проверка, что LCM_NN_N(1, B) и LCM_NN_N(A, 1) возвращает B и A соответственно
    """
    A = nat_0([1], 1)  # 1
    B1 = nat_0([1, 0, 0], 3)  # 100
    B2 = nat_0([4, 5, 6], 3)  # 456
    C1 = nat_0([1, 0, 0], 3)  # 100
    C2 = nat_0([9, 9, 9], 3)  # 999
    expected1 = B1  # LCM(1, 100) = 100
    expected2 = B2  # LCM(1, 456) = 456
    expected3 = C1  # LCM(100,1) = 100
    expected4 = C2  # LCM(999,1) = 999

    assert LCM_NN_N(A, B1) == expected1
    assert LCM_NN_N(A, B2) == expected2
    assert LCM_NN_N(C1, A) == expected3
    assert LCM_NN_N(C2, A) == expected4


def test_lcm_multiple_common_divisors():
    """
    Проверка, что LCM_NN_N находит наименьшее общее кратное
    """
    A1 = nat_0([1, 2], 2)  # 12
    B1 = nat_0([1, 8], 2)  # 18
    expected1 = int_to_nat0((nat0_to_int(A1) * nat0_to_int(B1)) // 6)  # НОД(12,18)=6, LCM=36

    A2 = nat_0([2, 4], 2)  # 24
    B2 = nat_0([3, 6], 2)  # 36
    expected2 = int_to_nat0((nat0_to_int(A2) * nat0_to_int(B2)) // 12)  # НОД(24,36)=12, LCM=72

    assert LCM_NN_N(A1, B1) == expected1
    assert LCM_NN_N(A2, B2) == expected2


def test_lcm_large_numbers():
    """
    Проверка работы функции с большими числами
    """
    A1 = nat_0([1, 2, 3, 4, 5, 6], 6)  # 123456
    B1 = nat_0([7, 8, 9, 0, 1, 2], 6)  # 789012
    # Вычислим НОД(123456, 789012) = 12
    # LCM = (123456 * 789012) / 12 = 123456 * 65751 = 8117355456
    expected1 = int_to_nat0(8117355456)

    A2 = nat_0([9, 8, 7, 6, 5, 4, 3, 2, 1], 9)  # 987654321
    B2 = nat_0([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)  # 123456789
    expected2 = int_to_nat0(13548070123626141)

    assert LCM_NN_N(A1, B1) == expected1
    assert LCM_NN_N(A2, B2) == expected2

def test_lcm_with_large_prime():
    """
    Проверка, что LCM_NN_N с большим простым числом и другим числом работает корректно
    """
    A1 = nat_0([1, 0, 0], 3)  # 100
    B1 = nat_0([9, 7], 2)  # 97 (простое)
    # НОД(100, 97) = 1
    # LCM = 100 * 97 = 9700
    expected1 = int_to_nat0(nat0_to_int(A1) * nat0_to_int(B1))  # 9700

    A2 = nat_0([1, 0, 0, 0], 4)  # 1000
    B2 = nat_0([9, 9, 7], 3)  # 997 (простое)
    # НОД(1000, 997) = 1
    # LCM = 1000 * 997 = 997000
    expected2 = int_to_nat0(nat0_to_int(A2) * nat0_to_int(B2))  # 997000

    assert LCM_NN_N(A1, B1) == expected1
    assert LCM_NN_N(A2, B2) == expected2
