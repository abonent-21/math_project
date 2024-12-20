from Types import pol, ceil, rat, nat_0
from GCF_PP_P import GCF_PP_P

def test_GCF_PP_P():
    # Определяем полиномы
    p1 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)  # p1 = x^2 + 2x + 1

    p2 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
    ], 1)  # p2 = x + 1

    p3 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)  # p3 = x^2 + 1

    p4 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^2
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^3
    ], 3)  # p4 = x^3 + x^2 + 1

    p5 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)  # p5 = x^2 + 2x + 1

    p6 = pol([
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # 0 * x^1
        rat(ceil([1], 1, 1), nat_0([1], 1))  # -1 * x^2
    ], 2)  # p6 = -x^2 + 1

    p7 = pol([
        rat(ceil([1], 1, 1), nat_0([1], 1)),  # -1 * x^0
        rat(ceil([3], 1, 0), nat_0([1], 1)),   # 3 * x^1
        rat(ceil([3], 1, 1), nat_0([1], 1)),  # -3 * x^2
        rat(ceil([1], 1, 0), nat_0([1], 1))    # 1 * x^3
    ], 3)  # p7 = x^3 - 3x^2 + 3x - 1

    # Пары для проверки НОД (больше вариаций делений)
    polynomials = [
        (p1, p2),  # x^2 + 2x + 1 и x + 1
        (p1, p3),  # x^2 + 2x + 1 и x^2 + 1
        (p1, p4),  # x^2 + 2x + 1 и x^3 + x^2 + 1 
        (p1, p5),  # x^2 + 2x + 1 и x^2 + 2x + 1
        (p1, p6),  # x^2 + 2x + 1 и -x^2 + 1
    ]

    # Ожидаемые результаты для каждой пары (примерные значения НОД)
    expected_gcds = [
        p2,  # НОД(x^2 + 2x + 1, x + 1) = x + 1
        pol([rat(ceil([1], 1, 0), nat_0([1], 1))], 0),  # НОД(x^2 + 2x + 1, x^2 + 1) = 1
        pol([rat(ceil([1], 1, 0), nat_0([1], 1))], 0),  # НОД(x^2 + 2x + 1, x^3 + x^2 + 1) = 1
        p5,  # НОД(x^2 + 2x + 1, x^2 + 2x + 1) = x^2 + 2x + 1
        pol([rat(ceil([2], 1, 0), nat_0([1], 1)), rat(ceil([2], 1, 0), nat_0([1], 1))], 1),  # НОД(x^2 + 2x + 1, -x^2 + 1) = x + 1
    ]

    # Проверка всех случаев
    count = 0
    for (p1, p2), expected_gcd in zip(polynomials, expected_gcds):
        result = GCF_PP_P(p1, p2)
        result_str = f"Ошибка {count}: НОД({p1}, {p2}) = {result}, ожидался {expected_gcd}"
        assert result == expected_gcd, result_str
        count += 1

    print("Все тесты пройдены успешно!")

if __name__ == "__main__":
    test_GCF_PP_P()
