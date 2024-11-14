# test_polynomials.py
import pytest
from Types import pol, rat, ceil, nat_0
from ADD_PP_P import ADD_PP_P
from SUB_PP_P import SUB_PP_P
from MUL_PQ_P import MUL_PQ_P

@pytest.fixture
def setup_polynomials():
    """
    Фикстура для создания тестовых многочленов и рациональных чисел.
    """
    # Создание рациональных чисел:
    # 1/2, 3/4, -5/6, 0/1, 1/4, 1/1, 12/1, 25/2, 5/4
    rat_1_2 = rat(
        num=ceil(array=[1], n=1, sign=0),
        den=nat_0(array=[2], n=1)
    )
    rat_3_4 = rat(
        num=ceil(array=[3], n=1, sign=0),
        den=nat_0(array=[4], n=1)
    )
    rat_neg_5_6 = rat(
        num=ceil(array=[5], n=1, sign=1),
        den=nat_0(array=[6], n=1)
    )
    rat_0 = rat(
        num=ceil(array=[0], n=1, sign=0),
        den=nat_0(array=[1], n=1)
    )
    rat_1_4 = rat(
        num=ceil(array=[1], n=1, sign=0),
        den=nat_0(array=[4], n=1)
    )
    rat_1 = rat(
        num=ceil(array=[1], n=1, sign=0),
        den=nat_0(array=[1], n=1)
    )
    rat_neg_1_3 = rat(
        num=ceil(array=[1], n=1, sign=1),
        den=nat_0(array=[3], n=1)
    )
    rat_neg_half = rat(
        num=ceil(array=[1], n=1, sign=1),
        den=nat_0(array=[2], n=1)
    )
    rat_12 = rat(
        num=ceil(array=[1, 2], n=2, sign=0),  # 12 представлено как [1, 2]
        den=nat_0(array=[1], n=1)
    )
    rat_25_2 = rat(
        num=ceil(array=[2, 5], n=2, sign=0),  # 25 представлено как [2, 5]
        den=nat_0(array=[2], n=1)
    )
    rat_5_4 = rat(
        num=ceil(array=[5], n=1, sign=0),
        den=nat_0(array=[4], n=1)
    )

    # Создание многочленов:
    # P1(x) = 1/2 + 3/4x
    P1 = pol(
        coefficients=[rat_1_2, rat_3_4],
        m=1
    )

    # P2(x) = (-5/6) + 0x + 1/2x^2
    P2 = pol(
        coefficients=[
            rat_neg_5_6,
            rat_0,
            rat(
                num=ceil(array=[1], n=1, sign=0),
                den=nat_0(array=[2], n=1)
            )
        ],
        m=2
    )

    # P3(x) = 0 (пустой многочлен с m = -1)
    P3 = pol(
        coefficients=[],
        m=-1
    )

    # P4(x) = 1/2 + 1/4x
    P4 = pol(
        coefficients=[rat_1_2, rat_1_4],
        m=1
    )

    # P_neg1(x) = -1/2 - 3/4x
    P_neg1 = pol(
        coefficients=[
            rat(
                num=ceil(array=[1], n=1, sign=1),
                den=nat_0(array=[2], n=1)
            ),
            rat(
                num=ceil(array=[3], n=1, sign=1),
                den=nat_0(array=[4], n=1)
            )
        ],
        m=1
    )

    # P5(x) = 12 + 1/2x
    P5 = pol(
        coefficients=[rat_12, rat_1_2],
        m=1
    )

    return {
        "rat_1_2": rat_1_2,
        "rat_3_4": rat_3_4,
        "rat_neg_5_6": rat_neg_5_6,
        "rat_0": rat_0,
        "rat_1_4": rat_1_4,
        "rat_1": rat_1,
        "rat_neg_1_3": rat_neg_1_3,
        "rat_neg_half": rat_neg_half,
        "rat_12": rat_12,
        "rat_25_2": rat_25_2,
        "rat_5_4": rat_5_4,
        "P1": P1,
        "P2": P2,
        "P3": P3,
        "P4": P4,
        "P_neg1": P_neg1,
        "P5": P5
    }

def test_addition_same_degree(setup_polynomials):
    """
    Тестирует сложение двух многочленов одинаковой степени.
    """
    P1 = setup_polynomials["P1"]
    P4 = setup_polynomials["P4"]

    # Ожидаемый результат P1 + P4 = (1/2 + 1/2) + (3/4 + 1/4)x = 1 + x
    P_expected = pol(
        coefficients=[
            rat(
                num=ceil(array=[1], n=1, sign=0),
                den=nat_0(array=[1], n=1)
            ),
            rat(
                num=ceil(array=[1], n=1, sign=0),
                den=nat_0(array=[1], n=1)
            )
        ],
        m=1
    )

    P_result = ADD_PP_P(P1, P4)
    assert P_result == P_expected, "Сложение многочленов с одинаковой степенью не прошло."

def test_addition_different_degree(setup_polynomials):
    """
    Тестирует сложение многочленов разной степени.
    """
    P1 = setup_polynomials["P1"]
    P2 = setup_polynomials["P2"]

    # Ожидаемый результат P1 + P2 = (1/2 - 5/6) + (3/4 + 0)x + (0 + 1/2)x^2 = (-1/3) + (3/4)x + (1/2)x^2
    P_expected = pol(
        coefficients=[
            setup_polynomials["rat_neg_1_3"],  # -1/3
            setup_polynomials["rat_3_4"],      # 3/4
            setup_polynomials["rat_1_2"]       # +1/2 (исправлено)
        ],
        m=2
    )

    P_result = ADD_PP_P(P1, P2)
    assert P_result == P_expected, "Сложение многочленов с разными степенями не прошло."

def test_subtraction_same_degree(setup_polynomials):
    """
    Тестирует вычитание двух многочленов одинаковой степени.
    """
    P1 = setup_polynomials["P1"]
    P4 = setup_polynomials["P4"]

    # Ожидаемый результат P1 - P4 = (1/2 - 1/2) + (3/4 - 1/4)x = 0 + (1/2)x
    P_expected = pol(
        coefficients=[
            setup_polynomials["rat_0"],        # 0
            rat(
                num=ceil(array=[1], n=1, sign=0),
                den=nat_0(array=[2], n=1)
            )                                    # +1/2
        ],
        m=1
    )

    P_result = SUB_PP_P(P1, P4)
    assert P_result == P_expected, "Вычитание многочленов с одинаковой степенью не прошло."

def test_subtraction_different_degree(setup_polynomials):
    """
    Тестирует вычитание многочленов разной степени.
    """
    P1 = setup_polynomials["P1"]
    P2 = setup_polynomials["P2"]

    # Ожидаемый результат P1 - P2 = (1/2 - (-5/6)) + (3/4 - 0)x + (0 - 1/2)x^2 = (4/3) + (3/4)x - 1/2x^2
    P_expected = pol(
        coefficients=[
            rat(
                num=ceil(array=[4], n=1, sign=0),
                den=nat_0(array=[3], n=1)
            ),                                    # +4/3
            setup_polynomials["rat_3_4"],        # +3/4
            setup_polynomials["rat_neg_half"]     # -1/2
        ],
        m=2
    )

    P_result = SUB_PP_P(P1, P2)
    assert P_result == P_expected, "Вычитание многочленов с разными степенями не прошло."

def test_multiplication_by_rational(setup_polynomials):
    """
    Тестирует умножение многочлена на положительное рациональное число.
    """
    P1 = setup_polynomials["P1"]
    Q = rat(
        num=ceil(array=[2], n=1, sign=0),
        den=nat_0(array=[3], n=1)
    )

    # Ожидаемый результат P1 * Q = (1/2 * 2/3) + (3/4 * 2/3)x = (1/3) + (1/2)x
    P_expected = pol(
        coefficients=[
            rat(
                num=ceil(array=[1], n=1, sign=0),
                den=nat_0(array=[3], n=1)
            ),                                    # 1/3
            rat(
                num=ceil(array=[1], n=1, sign=0),
                den=nat_0(array=[2], n=1)
            )                                     # 1/2
        ],
        m=1
    )

    P_result = MUL_PQ_P(P1, Q)
    assert P_result == P_expected, "Умножение многочлена на рациональное число не прошло."

def test_multiplication_by_negative_rational(setup_polynomials):
    """
    Тестирует умножение многочлена на отрицательное рациональное число.
    """
    P1 = setup_polynomials["P1"]
    Q = rat(
        num=ceil(array=[2], n=1, sign=1),
        den=nat_0(array=[3], n=1)
    )

    # Ожидаемый результат P1 * Q = (1/2 * -2/3) + (3/4 * -2/3)x = (-1/3) + (-1/2)x
    P_expected = pol(
        coefficients=[
            rat(
                num=ceil(array=[1], n=1, sign=1),
                den=nat_0(array=[3], n=1)
            ),                                    # -1/3
            rat(
                num=ceil(array=[1], n=1, sign=1),
                den=nat_0(array=[2], n=1)
            )                                     # -1/2
        ],
        m=1
    )

    P_result = MUL_PQ_P(P1, Q)
    assert P_result == P_expected, "Умножение многочлена на отрицательное рациональное число не прошло."

def test_addition_with_coefficient_12(setup_polynomials):
    """
    Тестирует сложение многочлена с коэффициентом 12 с другим многочленом.
    """
    P5 = setup_polynomials["P5"]
    P1 = setup_polynomials["P1"]

    # Ожидаемый результат P5 + P1 = (12 + 1/2) + (1/2 + 3/4)x = 25/2 + 5/4x
    P_expected = pol(
        coefficients=[
            rat(
                num=ceil(array=[2, 5], n=2, sign=0),  # 25 представлено как [2, 5]
                den=nat_0(array=[2], n=1)
            ),  # 25/2
            rat(
                num=ceil(array=[5], n=1, sign=0),
                den=nat_0(array=[4], n=1)
            )  # 5/4
        ],
        m=1
    )

    P_result = ADD_PP_P(P5, P1)
    assert P_result == P_expected, "Сложение многочленов с коэффициентом 12 не прошло."

def test_zero_polynomial(setup_polynomials):
    """
    Тестирует свойства нулевого многочлена.
    """
    P3 = setup_polynomials["P3"]

    # Проверяем, что P3 имеет m = -1 и пустые коэффициенты
    assert P3.m == -1, "Степень нулевого многочлена должна быть -1."
    assert P3.coefficients == [], "Коэффициенты нулевого многочлена должны быть пустыми."

# Дополнительные тесты для проверки новых коэффициентов

def test_multiplication_with_coefficient_12(setup_polynomials):
    """
    Тестирует умножение многочлена с коэффициентом 12 на рациональное число.
    """
    P5 = setup_polynomials["P5"]
    Q = rat(
        num=ceil(array=[2], n=1, sign=0),
        den=nat_0(array=[1], n=1)
    )

    # Ожидаемый результат P5 * Q = (12 * 2) + (1/2 * 2)x = 24 + 1x
    P_expected = pol(
        coefficients=[
            rat(
                num=ceil(array=[2, 4], n=2, sign=0),  # 24 представлено как [2, 4]
                den=nat_0(array=[1], n=1)
            ),  # 24/1
            rat(
                num=ceil(array=[1], n=1, sign=0),
                den=nat_0(array=[1], n=1)
            )   # 1/1
        ],
        m=1
    )

    P_result = MUL_PQ_P(P5, Q)
    assert P_result == P_expected, "Умножение многочлена с коэффициентом 12 не прошло."

def test_addition_with_zero_polynomial(setup_polynomials):
    """
    Тестирует сложение многочлена с коэффициентом 12 и нулевого многочлена.
    """
    P5 = setup_polynomials["P5"]
    P3 = setup_polynomials["P3"]

    # Ожидаемый результат: P5 + P3 = P5
    P_expected = setup_polynomials["P5"]

    P_result = ADD_PP_P(P5, P3)
    assert P_result == P_expected, "Сложение многочлена с коэффициентом 12 и нулевого многочлена не прошло."

if __name__ == "__main__":
    pytest.main()
