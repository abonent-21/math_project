from Types import rat, ceil, nat_0, pol
from DER_P_P import DER_P_P

def test_derivative():
    # Тест 1: Простой многочлен
    p1 = pol([rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^0
              rat(ceil([3], 1, 0), nat_0([1], 1))], 1)  # 3 * x^1
    expected1 = pol([rat(ceil([3], 1, 0), nat_0([1], 1))], 0)  # 3 * x^0
    assert DER_P_P(p1) == expected1, "Test 1 failed"

    # Тест 2: Многочлен второй степени
    p2 = pol([rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
              rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^1
              rat(ceil([4], 1, 0), nat_0([1], 1))], 2)  # 4 * x^2
    expected2 = pol([rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^0
                     rat(ceil([8], 1, 0), nat_0([1], 1))], 1)  # 8 * x^1
    assert DER_P_P(p2) == expected2, "Test 2 failed"

    # Тест 3: Многочлен третьей степени
    p3 = pol([rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
              rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
              rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^2
              rat(ceil([4], 1, 0), nat_0([1], 1))], 3)  # 4 * x^3
    expected3 = pol([rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^0
                     rat(ceil([6], 1, 0), nat_0([1], 1)),  # 6 * x^1
                     rat(ceil([1,2], 2, 0), nat_0([1], 1))], 2)  # 12 * x^2
    assert DER_P_P(p3) == expected3, "Test 3 failed"

    # Тест 4: Многочлен с нулевыми коэффициентами
    p4 = pol([rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^0
              rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^1
              rat(ceil([5], 1, 0), nat_0([1], 1))], 2)  # 5 * x^2
    expected4 = pol([rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^0
                     rat(ceil([1, 0], 2, 0), nat_0([1], 1))], 1)  # 10 * x^1
    assert DER_P_P(p4) == expected4, "Test 4 failed"

    # Тест 5: Нулевой многочлен
    p5 = pol([rat(ceil([0], 1, 0), nat_0([1], 1))], 0)  # 0
    expected5 = pol([rat(ceil([0], 1, 0), nat_0([1], 1))], 0)  # 0
    assert DER_P_P(p5) == expected5, "Test 5 failed"

    print("All tests passed !")

if __name__ == "__main__":
    test_derivative()


