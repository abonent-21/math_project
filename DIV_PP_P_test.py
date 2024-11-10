from Types import pol, rat, ceil, nat_0
from DIV_PP_P import DIV_PP_P

def test_div_pp_p():
    # Тест 1: Деление x^2 + 3x + 2 на x + 1
    p1 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^2
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^1
        rat(ceil([2], 1, 0), nat_0([1], 1))   # 2 * x^0
    ], 2)
    p2 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^0
    ], 1)
    result = DIV_PP_P(p1, p2)
    expected = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^0
    ], 1)
    assert result == expected

    # Деление x^3 + 2x^2 + 3x + 4 на x^2 + x + 1
    p1 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^3
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^2
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^1
        rat(ceil([4], 1, 0), nat_0([1], 1))   # 4 * x^0
    ], 3)
    p2 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^2
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^0
    ], 2)
    result = DIV_PP_P(p1, p2)
    expected = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^0
    ], 1)
    assert result == expected # Ожидаемый результат:  x + 1

if __name__ == "__main__":
    test_div_pp_p()