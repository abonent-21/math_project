import pytest
from Types import rat, nat_0, ceil
from RED_Q_Q import RED_Q_Q
from INT_Q_B import INT_Q_B
from TRANS_Q_Z import TRANS_Q_Z
from TRANS_Z_Q import TRANS_Z_Q

# Вспомогательная функция для создания объектов rat
def make_rat(num_list, num_sign, den_list):
    num = nat_0(num_list, num_sign)  # числитель
    den = nat_0(den_list, 1)  # знаменатель
    return rat(num, den)

# Тесты для функции RED_Q_Q - сокращение рационального числа
def test_reduce_fraction_with_common_divisor():
    # Проверка на дробь, которая должна быть сокращена (например, 4/6 -> 2/3)
    val = make_rat([4], 1, [6])  # 4/6
    reduced_val = RED_Q_Q(val)
    assert reduced_val.num.array == [2]  # Ожидаемый числитель 2
    assert reduced_val.den.array == [3]  # Ожидаемый знаменатель 3

def test_reduce_already_simplified_fraction():
    # Проверка на дробь, которая уже сокращена (например, 5/7 -> 5/7)
    val = make_rat([5], 1, [7])  # 5/7
    reduced_val = RED_Q_Q(val)
    assert reduced_val.num.array == [5]  # Ожидаемый числитель 5
    assert reduced_val.den.array == [7]  # Ожидаемый знаменатель 7

def test_reduce_fraction_with_zero_numerator():
    # Проверка на дробь с числителем 0 (например, 0/5 -> 0/1)
    val = make_rat([0], 1, [5])  # 0/5
    reduced_val = RED_Q_Q(val)
    assert reduced_val.num.array == [0]  # Ожидаемый числитель 0
    assert reduced_val.den.array == [1]  # Ожидаемый знаменатель 1

def test_reduce_fraction_with_equal_numerator_and_denominator():
    # Проверка на дробь, где числитель и знаменатель равны (например, 3/3 -> 1/1)
    val = make_rat([3], 1, [3])  # 3/3
    reduced_val = RED_Q_Q(val)
    assert reduced_val.num.array == [1]  # Ожидаемый числитель 1
    assert reduced_val.den.array == [1]  # Ожидаемый знаменатель 1

# Тесты для функции INT_Q_B - проверка на целое число
def test_is_integer_true():
    # Проверка, является ли рациональное число целым, если знаменатель равен 1
    val = make_rat([5], 1, [1])  # 5/1
    assert INT_Q_B(val) is True

def test_is_integer_false():
    # Проверка, является ли рациональное число целым, если знаменатель не равен 1
    val = make_rat([5], 1, [3])  # 5/3
    assert INT_Q_B(val) is False

# Тесты для функции TRANS_Q_Z - преобразование рационального числа в целое
def test_transform_rational_to_integer_valid():
    # Преобразование рационального числа с знаменателем 1 в целое
    val = make_rat([7], 1, [1])  # 7/1
    result = TRANS_Q_Z(val)
    assert result.array == [7]  # Ожидаемый результат - массив с числом 7

def test_transform_rational_to_integer_invalid():
    # Преобразование рационального числа с знаменателем отличным от 1 вызывает ошибку
    val = make_rat([7], 1, [2])  # 7/2
    with pytest.raises(ValueError, match="Значение знаменателя должно ровняться единице"):
        TRANS_Q_Z(val)

# Тесты для функции TRANS_Z_Q - преобразование целого числа в рациональное
def test_transform_integer_to_rational():
    # Преобразование целого числа в рациональное, проверка числителя и знаменателя
    integer = ceil([7], 1, 0)  # Представление целого числа 7
    result = TRANS_Z_Q(integer)
    assert result.num.array == [7]  # Ожидаемый числитель 7
    assert result.den.array == [1]  # Ожидаемый знаменатель 1
