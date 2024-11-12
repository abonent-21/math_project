# Пример тестового файла для MUL_PP_P.py
from Types import pol, rat, ceil, nat_0
from MOD_PP_P import MOD_PP_P

def test_mod_pp_p():
    # Деление x^2 + 2x + 1 на x + 1. В примере остаток ноль.
    p1 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)
    p2 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
    ], 1)

    result = MOD_PP_P(p1, p2)
    expected = pol([  
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^0
    ], 0)

    assert result == expected
    
    # Деление 4x^3 + 2x^2 + 3x + 5 на x^2 + 1
    p1 = pol([
        rat(ceil([5], 1, 0), nat_0([1], 1)),  # 5 * x^0
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^1
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^2
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 4 * x^3
    ], 3)
    p2 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^2
    ], 2)

    result = MOD_PP_P(p1, p2)
    expected = pol([  
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 5 * x^0
        rat(ceil([1], 1, 1), nat_0([1], 1)),  # 3 * x^1
    ], 1)
    assert result == expected
    
    # Деление 5x^4 + 3x^3 + 2x^2 + x + 7 на x^2 + x + 1
    p1 = pol([
        rat(ceil([7], 1, 0), nat_0([1], 1)),  # 7 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^2
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^3
        rat(ceil([5], 1, 0), nat_0([1], 1)),  # 5 * x^4
    ], 4)
    p2 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^2
    ], 2)

    result = MOD_PP_P(p1, p2)
    expected = pol([  
        rat(ceil([8], 1, 0), nat_0([1], 1)),  # 8 * x^0
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 4 * x^1
    ], 1)
    assert result == expected

    p1 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)  # p1 = x^2 + 2x + 1

    p4 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^2
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^3
    ], 3)  # p4 = x^3 + x^2 + 1

    result = MOD_PP_P(p4, p1)
    expected = pol([rat(ceil([2], 1, 0), nat_0([1], 1))],
                   [rat(ceil([1], 1, 0), nat_0([1], 1))], 1)
    assert result == expected

if __name__ == "__main__":
    test_mod_pp_p()