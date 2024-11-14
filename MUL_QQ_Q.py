# MUL_QQ_Q.py
# Умножение дробей
# Автор: Бескончин М.А. Группа - ПМИ-3381

from Types import rat, nat_0,ceil

from MUL_ZZ_Z import MUL_ZZ_Z
from TRANS_N_Z import TRANS_N_Z
from RED_Q_Q import RED_Q_Q


def MUL_QQ_Q(multiplier_one_accepted: rat, multiplier_two_accepted: rat) -> rat:
    """
        Функция умножает две дроби (рациональных числа) и возвращает результат в несократимой форме.

        :param multiplier_one_accepted: Первое множитель (тип rat)
        :param multiplier_two_accepted: Второе множитель (тип rat)
        :return: Результат умножения двух дробей в несократимой форме (тип rat)
    """

    result = rat(num=ceil([0], 1,0), den=nat_0([1], 1))
    multiplier_one = multiplier_one_accepted.copy()
    multiplier_two = multiplier_two_accepted.copy()

    # Умножаем числители двух дробей
    result.num = MUL_ZZ_Z(multiplier_one.num,multiplier_two.num)
    # Умножаем знаменатели двух дробей
    result.den = MUL_ZZ_Z(TRANS_N_Z(multiplier_one.den), TRANS_N_Z(multiplier_two.den))
    # Сокращаем полученную дробь до несократимой формы
    return RED_Q_Q(result)