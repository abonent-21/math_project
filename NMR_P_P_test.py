# Автор: Козлов Г.Е. Группа - ПМИ-3381

from Types import *
from NMR_P_P import NMR_P_P


def test_NMR_P_P():
    p5 = pol([
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 4 * x^0
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1  * x^2
    ], 2) # x^2 + 4x + 4 = (x + 2)^2

    excepted = pol([rat(ceil([2], 1, 0), nat_0([1], 1)), rat(ceil([1], 1, 0), nat_0([1], 1))], 1)

    assert NMR_P_P(p5) == excepted, "Failed test 1"

    p6 = pol([
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 4 * x^0
        rat(ceil([4], 1, 1), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1  * x^2
    ], 2) # x^2 - 4x + 4 = (x - 2)^2

    excepted = pol([rat(ceil([2], 1, 1), nat_0([1], 1)), rat(ceil([1], 1, 0), nat_0([1], 1))], 1)

    assert NMR_P_P(p6) == excepted, "Failed test 2"

    p7 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^1
        rat(ceil([2], 1, 1), nat_0([1], 1)),  # -2 * x^2
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^4
    ], 4) # x^4 - 2x^2 + 1 -> (x+1)(x-1) -> x^2 - 1

    excepted = pol([rat(ceil([1], 1, 1), nat_0([1], 1)), rat(ceil([0], 1, 0), nat_0([1], 1)), rat(ceil([1], 1, 0), nat_0([1], 1))], 2)

    assert NMR_P_P(p7) == excepted, "Failed test 3"

    p8 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 0 * x^1
        rat(ceil([6], 1, 0), nat_0([1], 1)),  # -2 * x^2
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 0 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^4
    ], 4) # 1 + 4 x + 6 x^2 + 4 x^3 + x^4 -> x + 1

    excepted = pol([rat(ceil([1], 1, 0), nat_0([1], 1)), rat(ceil([1], 1, 0), nat_0([1], 1))], 1)

    assert NMR_P_P(p8) == excepted, "Failed test 4"

    p9 = pol([
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 4 * x^0
        rat(ceil([7], 1, 1), nat_0([1], 1)),  # -7 * x^1
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^2
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^3
    ], 3) # x^3 + 2 x^2 - 7 x + 4 -> x^2 + 3 x - 4

    excepted = pol([rat(ceil([4], 1, 1), nat_0([1], 1)), rat(ceil([3], 1, 0), nat_0([1], 1)), rat(ceil([1], 1, 0), nat_0([1], 1))], 2)

    assert NMR_P_P(p9) == excepted, "Failed test 5"

    p10 = pol([
        rat(ceil([6], 1, 0), nat_0([1], 1)),  # 4 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # -7 * x^1
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^2
    ], 2) # None

    assert NMR_P_P(p10) == None, "Failed test 6"

    print("Passed all test!")

if __name__ == '__main__':
    test_NMR_P_P()