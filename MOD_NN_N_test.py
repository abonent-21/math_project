import pytest
from Types import nat_0
from MOD_NN_N import MOD_NN_N

def test_mod_basic():
    A = nat_0([1, 2, 0, 0], 4)  # 1200
    B = nat_0([1, 6, 0], 3)     # 160
    expected_result = nat_0([8, 0], 2)  # Остаток 1200 % 160 = 40
    assert MOD_NN_N(A, B) == expected_result

def test_mod_exact_division():
    A = nat_0([1, 6, 0], 3)  # 160
    B = nat_0([4, 0], 2)     # 40
    expected_result = nat_0([0], 1)  # Остаток 160 % 40 = 0
    assert MOD_NN_N(A, B) == expected_result

def test_mod_no_remainder():
    A = nat_0([1, 0, 0], 3)  # 100
    B = nat_0([2, 5], 2)     # 25
    expected_result = nat_0([0], 1)  # Остаток 100 % 25 = 0
    assert MOD_NN_N(A, B) == expected_result

def test_mod_with_remainder():
    A = nat_0([1, 2, 3], 3)  # 123
    B = nat_0([1, 0], 2)     # 10
    expected_result = nat_0([3], 1)  # Остаток 123 % 10 = 3
    assert MOD_NN_N(A, B) == expected_result

