# Автор: Марков М.М. Группа - ПМИ-3381

from Types import pol, rat, nat_0, ceil
from DEG_P_N import DEG_P_N
from LED_P_Q import LED_P_Q
from MUL_Pxk_P import MUL_Pxk_P


def test_deg_p_n():
    # Тестирование функции DEG_P_N

    # Базовый случай: многочлен нулевой степени
    assert DEG_P_N(pol([rat(ceil([1], 1, 0), nat_0([1], 1))], 0)) == nat_0([0], 1)  # Степень 0

    # Степень 1
    assert DEG_P_N(pol([rat(ceil([1], 1, 0), nat_0([1], 1)), rat(ceil([2], 1, 0), nat_0([1], 1))], 1)) == nat_0([1], 1)

    # Степень 1000 (большое число)
    large_coefficients = [rat(ceil([0], 1, 0), nat_0([1], 1))] * 1000 + [rat(ceil([1], 1, 0), nat_0([1], 1))]
    assert DEG_P_N(pol(large_coefficients, 1000)) == nat_0([1, 0, 0, 0], 4)  # Степень 1000

    print("Все тесты для DEG_P_N, включая пограничные, пройдены успешно!")


def test_led_p_q():
    # Тестирование функции LED_P_Q

    # Базовый случай: многочлен нулевой степени
    assert LED_P_Q(pol([rat(ceil([1], 1, 0), nat_0([1], 1))], 0)) == rat(ceil([1], 1, 0), nat_0([1], 1))

    # Многочлен со старшим коэффициентом не равным нулю
    assert LED_P_Q(pol([rat(ceil([3], 1, 0), nat_0([1], 1)), rat(ceil([4], 1, 0), nat_0([1], 1))], 1)) == rat(
        ceil([4], 1, 0), nat_0([1], 1))

    # Пограничный случай: большое количество нулей перед старшим коэффициентом
    large_coefficients = [rat(ceil([0], 1, 0), nat_0([1], 1))] * 1000 + [rat(ceil([5], 1, 0), nat_0([1], 1))]
    assert LED_P_Q(pol(large_coefficients, 1000)) == rat(ceil([5], 1, 0), nat_0([1], 1))

    print("Все тесты для LED_P_Q, включая пограничные и большие числа, пройдены успешно!")


def test_mul_pxk_p():
    # Тестирование функции MUL_Pxk_P

    # Базовый случай: умножение многочлена степени 1 на x^0 (не должно измениться)
    poly = pol([rat(ceil([1], 1, 0), nat_0([1], 1)), rat(ceil([2], 1, 0), nat_0([1], 1))], 1)  # P(x) = 1 + 2x
    result = MUL_Pxk_P(poly, nat_0([0], 1))  # Умножение на x^0
    assert result.m == 1
    assert result.coefficients == poly.coefficients

    # Умножение на x^2 (добавляем 2 нулевых коэффициента)
    result = MUL_Pxk_P(poly, nat_0([2], 1))  # Ожидаем P(x) * x^2 = 1x^2 + 2x^3
    assert result.m == 3
    assert result.coefficients == [
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # x^0
        rat(ceil([0], 1, 0), nat_0([1], 1)),  # x^1
        rat(ceil([1], 1, 0), nat_0([1], 1)),  # x^2 (исходный коэффициент при x^0)
        rat(ceil([2], 1, 0), nat_0([1], 1))  # x^3 (исходный коэффициент при x^1)
    ]

    # Умножение большого многочлена на x^1000 (проверка корректности для больших чисел)
    large_poly = pol([rat(ceil([1], 1, 0), nat_0([1], 1))], 0)
    large_k = nat_0([1, 0, 0, 0], 4)  # x^1000
    result = MUL_Pxk_P(large_poly, large_k)
    assert result.m == 1000
    assert result.coefficients == [rat(ceil([0], 1, 0), nat_0([1], 1))] * 1000 + [rat(ceil([1], 1, 0), nat_0([1], 1))]

    print("Все тесты для MUL_Pxk_P, включая пограничные и большие числа, пройдены успешно!")


if __name__ == "__main__":
    test_deg_p_n()
    test_led_p_q()
    test_mul_pxk_p()
