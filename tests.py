# tests.py

import pytest
from Types import pol, rat, ceil, nat_0
from ADD_PP_P import ADD_PP_P
from SUB_PP_P import SUB_PP_P
from MUL_PQ_P import MUL_PQ_P

# Вспомогательные функции
def create_rat(numerator: int, denominator: int) -> rat:
    """
    Создаёт объект класса rat из числителя и знаменателя.
    :param numerator: Целое число (может быть отрицательным).
    :param denominator: Натуральное число (> 0).
    :return: Объект класса rat.
    """
    assert denominator != 0, "Знаменатель не может быть равен 0"
    if numerator < 0:
        sign = 1
        num_abs = -numerator
    else:
        sign = 0
        num_abs = numerator
    num_array = [int(digit) for digit in str(num_abs)] if num_abs != 0 else [0]
    num_n = len(num_array)
    num = ceil(array=num_array, n=num_n, sign=sign)
    den = nat_0(array=[denominator], n=len(str(denominator)))
    return rat(num=num, den=den)

def create_polynomial(coefficients: list, degree: int) -> pol:
    """
    Создаёт объект класса pol из списка коэффициентов и степени.
    Коэффициенты должны быть упорядочены от младшего к старшему члену.
    :param coefficients: Список объектов класса rat.
    :param degree: Степень многочлена.
    :return: Объект класса pol.
    """
    # Убедитесь, что список коэффициентов имеет длину degree + 1
    if len(coefficients) < degree + 1:
        # Дополняем коэффициентами 0/1, если необходимо
        for _ in range(degree + 1 - len(coefficients)):
            coefficients.append(create_rat(0, 1))
    elif len(coefficients) > degree + 1:
        # Обрезаем коэффициенты до степени degree + 1
        coefficients = coefficients[:degree + 1]
    return pol(coefficients=coefficients, m=degree)

# Тесты для малых многочленов (степени 0-5)
def test_operations_small_polynomials():
    # Создание многочленов
    # P1(x) = 3 + 2x + 1x^2 + 0x^3 + 5x^4 + 4x^5
    P1 = pol(coefficients=[
        create_rat(3, 1),   # x^0
        create_rat(2, 1),   # x^1
        create_rat(1, 1),   # x^2
        create_rat(0, 1),   # x^3
        create_rat(5, 1),   # x^4
        create_rat(4, 1)    # x^5
    ], m=5)

    # P2(x) = -1 + 1x + 2x^2 + 3x^3 + 0x^4 + 4x^5
    P2 = pol(coefficients=[
        create_rat(-1, 1),  # x^0
        create_rat(1, 1),   # x^1
        create_rat(2, 1),   # x^2
        create_rat(3, 1),   # x^3
        create_rat(0, 1),   # x^4
        create_rat(4, 1)    # x^5
    ], m=5)

    # Ожидаемые результаты сложения: 2 + 3x + 3x^2 + 3x^3 + 5x^4 + 8x^5
    expected_add = pol(coefficients=[
        create_rat(2, 1),    # x^0: 3 + (-1) = 2
        create_rat(3, 1),    # x^1: 2 + 1 = 3
        create_rat(3, 1),    # x^2: 1 + 2 = 3
        create_rat(3, 1),    # x^3: 0 + 3 = 3
        create_rat(5, 1),    # x^4: 5 + 0 = 5
        create_rat(8, 1)     # x^5: 4 + 4 = 8
    ], m=5)

    # Выполнение сложения
    result_add = ADD_PP_P(P1, P2)
    assert result_add == expected_add, f"Ожидалось P1 + P2: {expected_add}, получен: {result_add}"

    # Ожидаемые результаты вычитания: 4 +1x -1x^2 -3x^3 +5x^4 +0x^5
    expected_sub = pol(coefficients=[
        create_rat(4, 1),     # x^0: 3 - (-1) = 4
        create_rat(1, 1),     # x^1: 2 - 1 = 1
        create_rat(-1, 1),    # x^2: 1 - 2 = -1
        create_rat(-3, 1),    # x^3: 0 - 3 = -3
        create_rat(5, 1),     # x^4: 5 - 0 = 5
        create_rat(0, 1)      # x^5: 4 - 4 = 0
    ], m=5)

    # Выполнение вычитания
    result_sub = SUB_PP_P(P1, P2)
    assert result_sub == expected_sub, f"Ожидалось P1 - P2: {expected_sub}, получен: {result_sub}"

    # Умножение P1 * Q, где Q = 2/3
    Q = create_rat(2, 3)
    expected_mul = pol(coefficients=[
        create_rat(2, 1),     # x^0: 6/3 = 2/1
        create_rat(4, 3),     # x^1: 4/3
        create_rat(2, 3),     # x^2: 2/3
        create_rat(0, 1),     # x^3: 0/1
        create_rat(10, 3),    # x^4: 10/3
        create_rat(8, 3)      # x^5: 8/3
    ], m=5)

    # Выполнение умножения
    result_mul = MUL_PQ_P(P1, Q)
    assert result_mul == expected_mul, f"Ожидалось P1 * Q: {expected_mul}, получен: {result_mul}"

# Тесты для средних многочленов (степени 6-15)
# Тесты для средних многочленов (степени 6-15)
def test_operations_medium_polynomials():
    # Создание многочленов
    # P7(x) = 1 + 2x + 3x^2 + ... + 16x^15
    P7 = pol(coefficients=[
        create_rat(1, 1),   # x^0
        create_rat(2, 1),   # x^1
        create_rat(3, 1),   # x^2
        create_rat(4, 1),   # x^3
        create_rat(5, 1),   # x^4
        create_rat(6, 1),   # x^5
        create_rat(7, 1),   # x^6
        create_rat(8, 1),   # x^7
        create_rat(9, 1),   # x^8
        create_rat(10, 1),  # x^9
        create_rat(11, 1),  # x^10
        create_rat(12, 1),  # x^11
        create_rat(13, 1),  # x^12
        create_rat(14, 1),  # x^13
        create_rat(15, 1),  # x^14
        create_rat(16, 1)   # x^15
    ], m=15)

    # P8(x) = -1 +1x -1x^2 +1x^3 -1x^4 +1x^5 -1x^6 +1x^7 -1x^8 +1x^9 -1x^10 +1x^11 -1x^12 +1x^13 -1x^14 +1x^15
    P8 = pol(coefficients=[
        create_rat(-1, 1),  # x^0
        create_rat(1, 1),   # x^1
        create_rat(-1, 1),  # x^2
        create_rat(1, 1),   # x^3
        create_rat(-1, 1),  # x^4
        create_rat(1, 1),   # x^5
        create_rat(-1, 1),  # x^6
        create_rat(1, 1),   # x^7
        create_rat(-1, 1),  # x^8
        create_rat(1, 1),   # x^9
        create_rat(-1, 1),  # x^10
        create_rat(1, 1),   # x^11
        create_rat(-1, 1),  # x^12
        create_rat(1, 1),   # x^13
        create_rat(-1, 1),  # x^14
        create_rat(1, 1)    # x^15
    ], m=15)

    # Ожидаемые результаты сложения P7 + P8:
    # [0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17]
    expected_add = pol(coefficients=[
        create_rat(0, 1),    # x^0: 1 + (-1) = 0
        create_rat(3, 1),    # x^1: 2 + 1 = 3
        create_rat(2, 1),    # x^2: 3 + (-1) = 2
        create_rat(5, 1),    # x^3: 4 + 1 = 5
        create_rat(4, 1),    # x^4: 5 + (-1) = 4
        create_rat(7, 1),    # x^5: 6 + 1 = 7
        create_rat(6, 1),    # x^6: 7 + (-1) = 6
        create_rat(9, 1),    # x^7: 8 + 1 = 9
        create_rat(8, 1),    # x^8: 9 + (-1) = 8
        create_rat(11, 1),   # x^9: 10 + 1 = 11
        create_rat(10, 1),   # x^10: 11 + (-1) = 10
        create_rat(13, 1),   # x^11: 12 + 1 = 13
        create_rat(12, 1),   # x^12: 13 + (-1) = 12
        create_rat(15, 1),   # x^13: 14 + 1 = 15
        create_rat(14, 1),   # x^14: 15 + (-1) = 14
        create_rat(17, 1)    # x^15: 16 + 1 = 17
    ], m=15)

    # Выполнение сложения
    result_add = ADD_PP_P(P7, P8)
    assert result_add == expected_add, f"Ожидалось P7 + P8: {expected_add}, получен: {result_add}"

    # Ожидаемые результаты вычитания P7 - P8:
    # [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]
    expected_sub = pol(coefficients=[
        create_rat(2, 1),    # x^0: 1 - (-1) = 2
        create_rat(1, 1),    # x^1: 2 - 1 = 1
        create_rat(4, 1),    # x^2: 3 - (-1) = 4
        create_rat(3, 1),    # x^3: 4 - 1 = 3
        create_rat(6, 1),    # x^4: 5 - (-1) = 6
        create_rat(5, 1),    # x^5: 6 - 1 = 5
        create_rat(8, 1),    # x^6: 7 - (-1) = 8
        create_rat(7, 1),    # x^7: 8 - 1 = 7
        create_rat(10, 1),   # x^8: 9 - (-1) = 10
        create_rat(9, 1),    # x^9: 10 - 1 = 9
        create_rat(12, 1),   # x^10: 11 - (-1) = 12
        create_rat(11, 1),   # x^11: 12 - 1 = 11
        create_rat(14, 1),   # x^12: 13 - (-1) = 14
        create_rat(13, 1),   # x^13: 14 - 1 = 13
        create_rat(16, 1),   # x^14: 15 - (-1) = 16
        create_rat(15, 1)    # x^15: 16 - 1 = 15
    ], m=15)

    # Выполнение вычитания
    result_sub = SUB_PP_P(P7, P8)
    assert result_sub == expected_sub, f"Ожидалось P7 - P8: {expected_sub}, получен: {result_sub}"

    # Умножение P7 * Q, где Q = 3/4
    Q = create_rat(3, 4)
    # Ожидаемые коэффициенты после умножения: (P7.coefficients[i] * 3) / 4
    expected_mul = pol(coefficients=[
        create_rat(3, 4),    # x^0: 1 * 3 /4 = 3/4
        create_rat(6, 4),    # x^1: 2 * 3 /4 = 6/4 = 3/2
        create_rat(9, 4),    # x^2: 3 * 3 /4 = 9/4
        create_rat(12, 4),   # x^3: 4 * 3 /4 = 12/4 = 3/1
        create_rat(15, 4),   # x^4: 5 * 3 /4 = 15/4
        create_rat(18, 4),   # x^5: 6 * 3 /4 = 18/4 = 9/2
        create_rat(21, 4),   # x^6: 7 * 3 /4 = 21/4
        create_rat(24, 4),   # x^7: 8 * 3 /4 = 24/4 = 6/1
        create_rat(27, 4),   # x^8: 9 * 3 /4 = 27/4
        create_rat(30, 4),   # x^9: 10 * 3 /4 = 30/4 = 15/2
        create_rat(33, 4),   # x^10: 11 * 3 /4 = 33/4
        create_rat(36, 4),   # x^11: 12 * 3 /4 = 36/4 = 9/1
        create_rat(39, 4),   # x^12: 13 * 3 /4 = 39/4
        create_rat(42, 4),   # x^13: 14 * 3 /4 = 42/4 = 21/2
        create_rat(45, 4),   # x^14: 15 * 3 /4 = 45/4
        create_rat(48, 4)    # x^15: 16 * 3 /4 = 48/4 = 12/1
    ], m=15)

    # Упрощение дробей в expected_mul
    # Если классы rat и pol уже упрощают дроби, тогда ожидаемые коэффициенты должны быть упрощены
    # Однако, если нет, то ожидаемые коэффициенты должны соответствовать фактическим результатам операций
    # Предполагаем, что операции упрощают, поэтому приведём expected_mul к упрощённому виду

    expected_mul_simplified = pol(coefficients=[
        create_rat(3, 4),    # x^0: 3/4
        create_rat(3, 2),    # x^1: 6/4 = 3/2
        create_rat(9, 4),    # x^2: 9/4
        create_rat(3, 1),    # x^3: 12/4 = 3/1
        create_rat(15, 4),   # x^4: 15/4
        create_rat(9, 2),    # x^5: 18/4 = 9/2
        create_rat(21, 4),   # x^6: 21/4
        create_rat(6, 1),    # x^7: 24/4 = 6/1
        create_rat(27, 4),   # x^8: 27/4
        create_rat(15, 2),   # x^9: 30/4 = 15/2
        create_rat(33, 4),   # x^10: 33/4
        create_rat(9, 1),    # x^11: 36/4 = 9/1
        create_rat(39, 4),   # x^12: 39/4
        create_rat(21, 2),   # x^13: 42/4 = 21/2
        create_rat(45, 4),   # x^14: 45/4
        create_rat(12, 1)     # x^15: 48/4 = 12/1
    ], m=15)

    # Выполнение умножения
    result_mul = MUL_PQ_P(P7, Q)
    assert result_mul == expected_mul_simplified, f"Ожидалось P7 * Q: {expected_mul_simplified}, получен: {result_mul}"

# Тесты для больших многочленов (степени 16-30)
def test_operations_large_polynomials():
    # Создание многочленов
    # P9(x) = 1 + 2x + 3x^2 + ... + 31x^30
    P9_coefficients = [
        create_rat(i, 1) for i in range(1, 32)  # x^0 до x^30
    ]
    P9 = pol(coefficients=P9_coefficients, m=30)

    # P10(x) = -1 + 2x -3x^2 +4x^3 -5x^4 +6x^5 -7x^6 +8x^7 -9x^8 +10x^9 -11x^10 +12x^11 -13x^12 +14x^13 -15x^14 +16x^15 -17x^16 +18x^17 -19x^18 +20x^19 -21x^20 +22x^21 -23x^22 +24x^23 -25x^24 +26x^25 -27x^26 +28x^27 -29x^28 +30x^29 -31x^30
    P10_coefficients = [
        create_rat(-1, 1),  # x^0
        create_rat(2, 1),   # x^1
        create_rat(-3, 1),  # x^2
        create_rat(4, 1),   # x^3
        create_rat(-5, 1),  # x^4
        create_rat(6, 1),   # x^5
        create_rat(-7, 1),  # x^6
        create_rat(8, 1),   # x^7
        create_rat(-9, 1),  # x^8
        create_rat(10, 1),  # x^9
        create_rat(-11, 1), # x^10
        create_rat(12, 1),  # x^11
        create_rat(-13, 1), # x^12
        create_rat(14, 1),  # x^13
        create_rat(-15, 1), # x^14
        create_rat(16, 1),  # x^15
        create_rat(-17, 1), # x^16
        create_rat(18, 1),  # x^17
        create_rat(-19, 1), # x^18
        create_rat(20, 1),  # x^19
        create_rat(-21, 1), # x^20
        create_rat(22, 1),  # x^21
        create_rat(-23, 1), # x^22
        create_rat(24, 1),  # x^23
        create_rat(-25, 1), # x^24
        create_rat(26, 1),  # x^25
        create_rat(-27, 1), # x^26
        create_rat(28, 1),  # x^27
        create_rat(-29, 1), # x^28
        create_rat(30, 1),  # x^29
        create_rat(-31, 1)  # x^30
    ]
    P10 = pol(coefficients=P10_coefficients, m=30)

    # Ожидаемые результаты сложения P9 + P10:
    # [0,4,0,8,0,12,0,16,0,20,0,24,0,28,0,32,0,36,0,40,0,44,0,48,0,52,0,56,0,60,0]
    expected_add = pol(coefficients=[
        create_rat(0, 1),    # x^0:1 + (-1) =0
        create_rat(4, 1),    # x^1:2 +2 =4
        create_rat(0, 1),    # x^2:3 + (-3) =0
        create_rat(8, 1),    # x^3:4 +4 =8
        create_rat(0, 1),    # x^4:5 + (-5) =0
        create_rat(12, 1),   # x^5:6 +6 =12
        create_rat(0, 1),    # x^6:7 + (-7) =0
        create_rat(16, 1),   # x^7:8 +8 =16
        create_rat(0, 1),    # x^8:9 + (-9) =0
        create_rat(20, 1),   # x^9:10 +10 =20
        create_rat(0, 1),    # x^10:11 + (-11) =0
        create_rat(24, 1),   # x^11:12 +12 =24
        create_rat(0, 1),    # x^12:13 + (-13) =0
        create_rat(28, 1),   # x^13:14 +14 =28
        create_rat(0, 1),    # x^14:15 + (-15) =0
        create_rat(32, 1),   # x^15:16 +16 =32
        create_rat(0, 1),    # x^16:17 + (-17) =0
        create_rat(36, 1),   # x^17:18 +18 =36
        create_rat(0, 1),    # x^18:19 + (-19) =0
        create_rat(40, 1),   # x^19:20 +20 =40
        create_rat(0, 1),    # x^20:21 + (-21) =0
        create_rat(44, 1),   # x^21:22 +22 =44
        create_rat(0, 1),    # x^22:23 + (-23) =0
        create_rat(48, 1),   # x^23:24 +24 =48
        create_rat(0, 1),    # x^24:25 + (-25) =0
        create_rat(52, 1),   # x^25:26 +26 =52
        create_rat(0, 1),    # x^26:27 + (-27) =0
        create_rat(56, 1),   # x^27:28 +28 =56
        create_rat(0, 1),    # x^28:29 + (-29) =0
        create_rat(60, 1),   # x^29:30 +30 =60
        create_rat(0, 1)     # x^30:31 + (-31) =0
    ], m=30)

    # Выполнение сложения
    result_add = ADD_PP_P(P9, P10)
    assert result_add == expected_add, f"Ожидалось P9 + P10: {expected_add}, получен: {result_add}"

    # Ожидаемые результаты вычитания P9 - P10:
    # [2,0,6,0,10,0,14,0,18,0,22,0,26,0,30,0,34,0,38,0,42,0,46,0,50,0,54,0,58,0,62]
    expected_sub = pol(coefficients=[
        create_rat(2, 1),    # x^0:1 - (-1) =2
        create_rat(0, 1),    # x^1:2 -2 =0
        create_rat(6, 1),    # x^2:3 - (-3) =6
        create_rat(0, 1),    # x^3:4 -4 =0
        create_rat(10, 1),   # x^4:5 - (-5) =10
        create_rat(0, 1),    # x^5:6 -6 =0
        create_rat(14, 1),   # x^6:7 - (-7) =14
        create_rat(0, 1),    # x^7:8 -8 =0
        create_rat(18, 1),   # x^8:9 - (-9) =18
        create_rat(0, 1),    # x^9:10 -10 =0
        create_rat(22, 1),   # x^10:11 - (-11) =22
        create_rat(0, 1),    # x^11:12 -12 =0
        create_rat(26, 1),   # x^12:13 - (-13) =26
        create_rat(0, 1),    # x^13:14 -14 =0
        create_rat(30, 1),   # x^14:15 - (-15) =30
        create_rat(0, 1),    # x^15:16 -16 =0
        create_rat(34, 1),   # x^16:17 - (-17) =34
        create_rat(0, 1),    # x^17:18 -18 =0
        create_rat(38, 1),   # x^18:19 - (-19) =38
        create_rat(0, 1),    # x^19:20 -20 =0
        create_rat(42, 1),   # x^20:21 - (-21) =42
        create_rat(0, 1),    # x^21:22 -22 =0
        create_rat(46, 1),   # x^22:23 - (-23) =46
        create_rat(0, 1),    # x^23:24 -24 =0
        create_rat(50, 1),   # x^24:25 - (-25) =50
        create_rat(0, 1),    # x^25:26 -26 =0
        create_rat(54, 1),   # x^26:27 - (-27) =54
        create_rat(0, 1),    # x^27:28 -28 =0
        create_rat(58, 1),   # x^28:29 - (-29) =58
        create_rat(0, 1),    # x^29:30 -30 =0
        create_rat(62, 1)     # x^30:31 - (-31) =62
    ], m=30)

    # Выполнение вычитания
    result_sub = SUB_PP_P(P9, P10)
    assert result_sub == expected_sub, f"Ожидалось P9 - P10: {expected_sub}, получен: {result_sub}"

    # Умножение P9 * Q, где Q = -1/3
    Q = create_rat(-1, 3)
    # Ожидаемые коэффициенты после умножения: (P9.coefficients[i] * -1) /3
    # Необходимо упростить дроби
    expected_mul = pol(coefficients=[
        create_rat(-1, 3),    # x^0:1 * (-1)/3 = -1/3
        create_rat(-2, 3),    # x^1:2 * (-1)/3 = -2/3
        create_rat(-1, 1),    # x^2:3 * (-1)/3 = -1/1
        create_rat(-4, 3),    # x^3:4 * (-1)/3 = -4/3
        create_rat(-5, 3),    # x^4:5 * (-1)/3 = -5/3
        create_rat(-2, 1),    # x^5:6 * (-1)/3 = -2/1
        create_rat(-7, 3),    # x^6:7 * (-1)/3 = -7/3
        create_rat(-8, 3),    # x^7:8 * (-1)/3 = -8/3
        create_rat(-3, 1),    # x^8:9 * (-1)/3 = -3/1
        create_rat(-10, 3),   # x^9:10 * (-1)/3 = -10/3
        create_rat(-11, 3),   # x^10:11 * (-1)/3 = -11/3
        create_rat(-4, 1),    # x^11:12 * (-1)/3 = -4/1
        create_rat(-13, 3),   # x^12:13 * (-1)/3 = -13/3
        create_rat(-14, 3),   # x^13:14 * (-1)/3 = -14/3
        create_rat(-5, 1),    # x^14:15 * (-1)/3 = -5/1
        create_rat(-16, 3),   # x^15:16 * (-1)/3 = -16/3
        create_rat(-17, 3),   # x^16:17 * (-1)/3 = -17/3
        create_rat(-6, 1),    # x^17:18 * (-1)/3 = -6/1
        create_rat(-19, 3),   # x^18:19 * (-1)/3 = -19/3
        create_rat(-20, 3),   # x^19:20 * (-1)/3 = -20/3
        create_rat(-7, 1),    # x^20:21 * (-1)/3 = -7/1
        create_rat(-22, 3),   # x^21:22 * (-1)/3 = -22/3
        create_rat(-23, 3),   # x^22:23 * (-1)/3 = -23/3
        create_rat(-8, 1),    # x^23:24 * (-1)/3 = -8/1
        create_rat(-25, 3),   # x^24:25 * (-1)/3 = -25/3
        create_rat(-26, 3),   # x^25:26 * (-1)/3 = -26/3
        create_rat(-9, 1),    # x^26:27 * (-1)/3 = -9/1
        create_rat(-28, 3),   # x^27:28 * (-1)/3 = -28/3
        create_rat(-29, 3),   # x^28:29 * (-1)/3 = -29/3
        create_rat(-10, 1),   # x^29:30 * (-1)/3 = -10/1
        create_rat(-31, 3)    # x^30:31 * (-1)/3 = -31/3
    ], m=30)

    # Выполнение умножения
    result_mul = MUL_PQ_P(P9, Q)
    assert result_mul == expected_mul, f"Ожидалось P9 * Q: {expected_mul}, получен: {result_mul}"

# Дополнительные тесты для класса rat
def test_rat_equality():
    # Проверка равенства двух одинаковых дробей
    a = create_rat(6, 3)  # rat(6,3)
    b = create_rat(6, 3)  # rat(6,3)
    assert a == b, f"rat(6,3) должно быть равно rat(6,3), получено: {a} и {b}"

def test_rat_zero():
    # Проверка равенства двух нулевых дробей
    a = create_rat(0, 1)  # rat(0,1)
    b = create_rat(0, 1)  # rat(0,1)
    assert a == b, f"rat(0,1) должно быть равно rat(0,1), получено: {a} и {b}"

def test_rat_negative():
    # Проверка равенства двух отрицательных дробей
    a = create_rat(-6, 3)  # rat(-6,3)
    b = create_rat(-6, 3)  # rat(-6,3)
    assert a == b, f"rat(-6,3) должно быть равно rat(-6,3), получено: {a} и {b}"

if __name__ == '__main__':
    # Запускаем pytest при выполнении файла напрямую
    pytest.main()
