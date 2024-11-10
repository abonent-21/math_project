from Types import pol, rat, ceil, nat_0
from FAC_P_Q import FAC_P_Q

def test_fac_p_q():
    # Тестирование функции FAC_P_Q

    # x^2 + 2x + 3
    p = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^2
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([3], 1, 0), nat_0([1], 1))   # 3 * x^0
    ], 2)

    result = FAC_P_Q(p)
    expected = rat(ceil([1], 1, 0), nat_0([1], 1))  # НОД = 1, НОК = 1, результат = 1 / 1
    assert result == expected

    # 4/6*x^3+8/12*x^2+10/15*x^1+2/3
    # пример интересен тем, что НОД = 2, НОК = 60. Данный вариант показывает, что итоговая дробь сокращается
    p = pol([
    rat(ceil([4], 1, 0), nat_0([6], 1)),        # 4/6 * x^3
    rat(ceil([8], 1, 0), nat_0([1, 2], 2)),     # 8/12 * x^2
    rat(ceil([1, 0], 2, 0), nat_0([1, 5], 2)),  # 10/15 * x^1
    rat(ceil([2], 1, 0), nat_0([3], 1))         # 2/3 * x^0
    ], 3)

    result = FAC_P_Q(p)
    expected = rat(ceil([1], 1, 0), nat_0([3, 0], 2))  # НОД = 1, НОК = 30, результат = 1 / 30
    assert result == expected

    # 2x^2 + 3x + 4
    p = pol([
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^2
        rat(ceil([3], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([4], 1, 0), nat_0([1], 1))   # 4 * x^0
    ], 2)

    result = FAC_P_Q(p)
    expected = rat(ceil([1], 1, 0), nat_0([1], 1))  # НОД = 1, НОК = 1, результат = 1 / 1
    assert result == expected


    # (1/2)x^2 + (3/4)x + (5/6)
    p = pol([
        rat(ceil([1], 1, 0), nat_0([2], 1)),  # 1/2 * x^2
        rat(ceil([3], 1, 0), nat_0([4], 1)),  # 3/4 * x^1
        rat(ceil([5], 1, 0), nat_0([6], 1))   # 5/6 * x^0
    ], 2)

    result = FAC_P_Q(p)
    expected = rat(ceil([1], 1, 0), nat_0([1, 2], 2))  # НОД = 1, НОК = 12, результат = 1 / 12
    assert result == expected
    
    # x^3 + x^2 + x^1 + 1
    p = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1/1 * x^3
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1/1 * x^2
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1/1 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1/1 * x^0
    ], 3)
    result = FAC_P_Q(p)
    expected = rat(ceil([1], 1, 0), nat_0([1], 1))  # НОД = 1, НОК = 1, результат = 1 / 1
    assert result == expected

if __name__ == "__main__":
    test_fac_p_q()