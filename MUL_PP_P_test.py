# Пример тестового файла для MUL_PP_P.py
from Types import pol, rat, ceil, nat_0
from MUL_PP_P import MUL_PP_P

def test_mul_pp_p():
    # Тестирование функции MUL_PP_P

    # Умножение (x + 1) на (x + 2)
    p = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^0
    ], 1)

    q = pol([
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^0
    ], 1)

    result = MUL_PP_P(p, q)
    expected = pol([
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^2
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^1
        rat(ceil([2], 1, 0), nat_0([1], 1))   # 2 * x^0
    ], 2)  # Ожидаемый результат: x^2 + 3x + 2

    assert result == expected # Ожидаемый результат: x^2 + 3x + 2


    # Умножение (x^2 + 2x + 3) на (x + 1)
    p = pol([
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^2
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^0
    ], 2)

    q = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^0
    ], 1)

    result = MUL_PP_P(p, q)
    expected = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^3
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^2
        rat(ceil([5], 1, 0), nat_0([1], 1)),  # 5 * x^1
        rat(ceil([3], 1, 0), nat_0([1], 1))   # 3 * x^0
    ], 3)  # Ожидаемый результат: x^3 + 3x^2 + 5x + 3

    assert result == expected
    
    # Умножение (2x^2 + 3x + 4) на (x^2 + x + 1)
    p = pol([
        rat(ceil([4], 1, 0), nat_0([1], 1)),  # 4 * x^2
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^1
        rat(ceil([2], 1, 0), nat_0([1], 1))   # 2 * x^0
    ], 2)

    q = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^2
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^0
    ], 2)

    result = MUL_PP_P(p, q)
    expected = pol([
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^4
        rat(ceil([5], 1, 0), nat_0([1], 1)),  # 5 * x^3
        rat(ceil([9], 1, 0), nat_0([1], 1)),  # 9 * x^2
        rat(ceil([7], 1, 0), nat_0([1], 1)),  # 7 * x^1
        rat(ceil([4], 1, 0), nat_0([1], 1))   # 4 * x^0
    ], 4) 

    assert result == expected  # Ожидаемый результат: 2x^4 + 5x^3 + 9x^2 + 7x + 4

if __name__ == "__main__":
    test_mul_pp_p()