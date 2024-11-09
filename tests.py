# tests.py
# Тесты для модулей ADD_PP_P.py, SUB_PP_P.py и MUL_PQ_P.py с использованием pytest
# Автор: [Самигулин Денис] Группа - [ПМИ-3381]

import pytest

from Types import pol, rat, ceil, nat_0
from ADD_PP_P import ADD_PP_P
from SUB_PP_P import SUB_PP_P
from MUL_PQ_P import MUL_PQ_P

@pytest.fixture
def test_data():
    # Определяем рациональные числа для коэффициентов

    # Число 2/3
    rat_2_3 = rat(
        num=ceil([2], 1, 0),
        den=nat_0([3], 1)
    )

    # Число -1/4
    rat_neg_1_4 = rat(
        num=ceil([1], 1, 1),
        den=nat_0([4], 1)
    )

    # Число 5/1 (целое число 5)
    rat_5 = rat(
        num=ceil([5], 1, 0),
        den=nat_0([1], 1)
    )

    # Число 0
    rat_0 = rat(
        num=ceil([0], 1, 0),
        den=nat_0([1], 1)
    )

    # Многочлен P1: (2/3) * x^2 + (-1/4) * x + 5
    P1 = pol(
        coefficients=[
            rat_2_3,        # Коэффициент при x^2
            rat_neg_1_4,    # Коэффициент при x^1
            rat_5           # Коэффициент при x^0
        ],
        m=2  # Степень многочлена
    )

    # Многочлен P2: (-1/4) * x^3 + (2/3) * x + 0
    P2 = pol(
        coefficients=[
            rat_neg_1_4,    # Коэффициент при x^3
            rat_0,          # Коэффициент при x^2
            rat_2_3,        # Коэффициент при x^1
            rat_0           # Коэффициент при x^0
        ],
        m=3  # Степень многочлена
    )

    # Рациональное число для умножения: 3/2
    rat_3_2 = rat(
        num=ceil([3], 1, 0),
        den=nat_0([2], 1)
    )

    return {
        'rat_2_3': rat_2_3,
        'rat_neg_1_4': rat_neg_1_4,
        'rat_5': rat_5,
        'rat_0': rat_0,
        'P1': P1,
        'P2': P2,
        'rat_3_2': rat_3_2
    }

def test_add_pp_p(test_data):
    # Получаем данные из фикстуры
    rat_neg_1_4 = test_data['rat_neg_1_4']
    rat_2_3 = test_data['rat_2_3']
    rat_5 = test_data['rat_5']
    P1 = test_data['P1']
    P2 = test_data['P2']

    # Тестируем сложение P1 + P2
    result = ADD_PP_P(P1, P2)

    # Ожидаемый результат: (-1/4) * x^3 + (2/3) * x^2 + (5/12) * x + 5
    expected_coeffs = [
        rat_neg_1_4,    # Коэффициент при x^3
        rat_2_3,        # Коэффициент при x^2
        rat(
            num=ceil([5], 1, 0),
            den=nat_0([1, 2], 2)  # Число 12
        ),              # Коэффициент при x^1
        rat_5           # Коэффициент при x^0
    ]
    expected = pol(coefficients=expected_coeffs, m=3)
    assert result == expected

def test_sub_pp_p(test_data):
    # Получаем данные из фикстуры
    rat_2_3 = test_data['rat_2_3']
    rat_5 = test_data['rat_5']
    P1 = test_data['P1']
    P2 = test_data['P2']

    # Тестируем вычитание P1 - P2
    result = SUB_PP_P(P1, P2)

    # Ожидаемый результат: (1/4) * x^3 + (2/3) * x^2 + (-11/12) * x + 5
    expected_coeffs = [
        rat(
            num=ceil([1], 1, 0),
            den=nat_0([4], 1)
        ),              # Коэффициент при x^3
        rat_2_3,        # Коэффициент при x^2
        rat(
            num=ceil([1, 1], 2, 1),
            den=nat_0([1, 2], 2)
        ),  # Коэффициент при x^1
        rat_5           # Коэффициент при x^0
    ]
    expected = pol(coefficients=expected_coeffs, m=3)
    assert result == expected

def test_mul_pq_p(test_data):
    # Получаем данные из фикстуры
    P1 = test_data['P1']
    rat_3_2 = test_data['rat_3_2']

    # Тестируем умножение P1 на рациональное число 3/2
    result = MUL_PQ_P(P1, rat_3_2)

    # Ожидаемый результат: (1) * x^2 + (-3/8) * x + (15/2)
    expected_coeffs = [
        rat(
            num=ceil([1], 1, 0),
            den=nat_0([1], 1)
        ),              # Коэффициент при x^2
        rat(
            num=ceil([3], 1, 1),
            den=nat_0([8], 1)
        ),              # Коэффициент при x^1
        rat(
            num=ceil([1, 5], 2, 0),
            den=nat_0([2], 1)
        )               # Коэффициент при x^0
    ]
    expected = pol(coefficients=expected_coeffs, m=2)
    assert result == expected

if __name__ == '__main__':
    # Запускаем pytest при выполнении файла напрямую
    pytest.main()
