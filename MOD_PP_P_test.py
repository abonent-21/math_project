# Пример тестового файла для MUL_PP_P.py
from Types import pol, rat, ceil, nat_0
from MUL_PP_P import MUL_PP_P

def test_mul_pp_p():
    # Умножение (x + 1) на (x + 1)
    p = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
    ], 1)  
    q = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
    ], 1)  
    result = MUL_PP_P(p, q)
    expected = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)  
    assert result == expected
  
    # Умножение (x^4 + 3x^3 + 2x^2 + 4x + 5) на (3x + 3)
    p = pol([
        rat(ceil([5], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 4 * x^1
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 2 * x^2
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 3 * x^3
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^4
    ], 4)
    q = pol([
        rat(ceil([3], 1, 0), nat_0([1], 1)),  
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^0
    ], 1)
    result = MUL_PP_P(p, q)
    expected = pol([ 
        rat(ceil([1, 5], 2, 0), nat_0([1], 1)),    # 3 * x^0
        rat(ceil([2, 7], 2, 0), nat_0([1], 1)), # 15 * x^1 
        rat(ceil([2, 1], 2, 0), nat_0([1], 1)), # 18 * x^2
        rat(ceil([1, 5], 2, 0), nat_0([1], 1)), # 15 * x^3
        rat(ceil([9], 1, 0), nat_0([1], 1)), # 12 * x^4
        rat(ceil([3], 1, 0), nat_0([1], 1))     # 3 * x^5
    ], 5)
    assert result == expected

    # Умножение (x^2 + 0x + 1) на (x^2 + x + 1)
    p = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)

    q = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)
    result = MUL_PP_P(p, q)
    expected = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^2
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^3
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^4
    ], 4)
    assert result == expected

    # Умножение (x^4+3x^3+2x^2+4x+5) на (3x^2-2x+1)
    p = pol([
        rat(ceil([5], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 4 * x^1
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^2
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^3
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^4
    ], 4)

    q = pol([
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^0
        rat(ceil([2], 1, 1), nat_0([1], 1)),  # -2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)
    result = MUL_PP_P(p, q)
    expected = pol([
        rat(ceil([1, 5], 2, 0), nat_0([1], 1)),      # 3 * x^0
        rat(ceil([2, 2], 2, 0), nat_0([1], 1)),      # 8 * x^1
        rat(ceil([2, 2], 2, 0), nat_0([1], 1)),   # 14 * x^2
        rat(ceil([1, 6], 2, 0), nat_0([1], 1)),   # 20 * x^3
        rat(ceil([1, 0], 2, 0), nat_0([1], 1)),   # 26 * x^4
        rat(ceil([4], 1, 1), nat_0([1], 1)),   # 14 * x^5
        rat(ceil([1], 1, 0), nat_0([1], 1))       # 5 * x^6
    ], 6)
    assert result == expected
    
if __name__ == "__main__":
    test_mul_pp_p()