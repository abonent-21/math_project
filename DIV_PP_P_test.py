from Types import pol, rat, ceil, nat_0
from DIV_PP_P import DIV_PP_P

def test_div_pp_p():
    # Деление x^2 + 2x + 1 на x + 1
    p1 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)
    p2 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
    ], 1)
    result = DIV_PP_P(p1, p2)
    expected = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
    ], 1)
    assert result == expected 

    # Деление x^2 + 2x + 1 на 2
    p1 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)
    p2 = pol([
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^0 (что представляет собой просто число)
    ], 0)
    result = DIV_PP_P(p1, p2)
    expected = pol([
        rat(ceil([1], 1, 0), nat_0([2], 1)),  # 1 * x^0 / 2 = 0.5
        rat(ceil([1], 1, 0), nat_0([1], 1)),   # 2 * x^1 / 2 = 1 * x^1
        rat(ceil([1], 1, 0), nat_0([2], 1))  # 1 * x^2 / 2 = 0.5 * x^2
    ], 2)
    assert result == expected  # Ожидаемый результат: 0.5 + x + 0.5x^2

    # Деление x^3 + 2x^2 + 3x + 4 на x^2 + x + 1
    p1 = pol([
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 4 * x^0
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^1
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^2
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^3
    ], 3)
    p2 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)
    result = DIV_PP_P(p1, p2)
    expected = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
    ], 1)
    assert result == expected 

    # Деление 4x^3 + 3x^2 + 2x + 1 на 3x^2 + 2x + 1
    p1 = pol([
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 4 * x^0
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^1
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 1 * x^2
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 2 * x^3
    ], 3)
    p2 = pol([
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^0
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)
    result = DIV_PP_P(p1, p2)
    expected = pol([
        rat(ceil([0], 1, 0), nat_0([1], 1)),   # 0 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1)),   # 1 * x^1
    ], 1)
    assert result == expected
    
    # Деление x^4 + x^3 + x^2 + x + 1 на x + 1
    p1 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^2
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^3
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^4
    ], 4)
    p2 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
    ], 1)
    result = DIV_PP_P(p1, p2)
    expected = pol([ 
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^2
    ], 3)
    assert result == expected # x^3 + x
    
    # Деление многочлена на себя (должно дать 1)
    p1 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^2
    ], 2)
    p2 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^2
    ], 2)
    result = DIV_PP_P(p1, p2)
    expected = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
    ], 0)
    assert result == expected 
    
    # Деление многочлена длинного
    p1 = pol([
        rat(ceil([2, 1], 2, 0), nat_0([1], 1)),  # 21 * x^0
        rat(ceil([2, 0], 2, 0), nat_0([1], 1)),  # 20 * x^1
        rat(ceil([1, 9], 2, 0), nat_0([1], 1)),  # 19 * x^2
        rat(ceil([1, 8], 2, 0), nat_0([1], 1)),  # 18 * x^3
        rat(ceil([1, 7], 2, 0), nat_0([1], 1)),  # 17 * x^4
        rat(ceil([1, 6], 2, 0), nat_0([1], 1)),  # 16 * x^5
        rat(ceil([1, 5], 2, 0), nat_0([1], 1)),  # 15 * x^6
        rat(ceil([1, 4], 2, 0), nat_0([1], 1)),  # 14 * x^7
        rat(ceil([1, 3], 2, 0), nat_0([1], 1)),  # 13 * x^8
        rat(ceil([1, 2], 2, 0), nat_0([1], 1)),  # 12 * x^9
        rat(ceil([1, 1], 2, 0), nat_0([1], 1)),  # 11 * x^10
        rat(ceil([1, 0], 2, 0), nat_0([1], 1)),  # 10 * x^11
        rat(ceil([9], 1, 0), nat_0([1], 1)),     # 9 * x^12
        rat(ceil([8], 1, 0), nat_0([1], 1)),     # 8 * x^13
        rat(ceil([7], 1, 0), nat_0([1], 1)),     # 7 * x^14
        rat(ceil([6], 1, 0), nat_0([1], 1)),     # 6 * x^15
        rat(ceil([5], 1, 0), nat_0([1], 1)),     # 5 * x^16
        rat(ceil([4], 1, 0), nat_0([1], 1)),     # 4 * x^17
        rat(ceil([3], 1, 0), nat_0([1], 1)),     # 3 * x^18
        rat(ceil([2], 1, 0), nat_0([1], 1)),     # 2 * x^19
        rat(ceil([1], 1, 0), nat_0([1], 1))      # 1 * x^20
    ], 20)
    p2 = pol([
        rat(ceil([0], 1, 0), nat_0([1], 1)),     # 11 * x^0
        rat(ceil([0], 1, 0), nat_0([1], 1)),     # 10 * x^1
        rat(ceil([0], 1, 0), nat_0([1], 1)),     # 9 * x^2
        rat(ceil([0], 1, 0), nat_0([1], 1)),     # 8 * x^3
        rat(ceil([0], 1, 0), nat_0([1], 1)),     # 7 * x^4
        rat(ceil([0], 1, 0), nat_0([1], 1)),     # 6 * x^5
        rat(ceil([0], 1, 0), nat_0([1], 1)),     # 5 * x^6
        rat(ceil([0], 1, 0), nat_0([1], 1)),     # 4 * x^7
        rat(ceil([0], 1, 0), nat_0([1], 1)),     # 3 * x^8
        rat(ceil([0], 1, 0), nat_0([1], 1)),     # 2 * x^9
        rat(ceil([1], 1, 0), nat_0([1], 1))      # 1 * x^10
    ], 10)
    assert result == expected 
if __name__ == "__main__":
    test_div_pp_p()