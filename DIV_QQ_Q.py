# DIV_QQ_Q.py
# Деление дробей (делитель отличен от нуля)
# Автор: Бескончин М.А. Группа - ПМИ-3381

from Types import rat, nat_0,ceil

from MUL_ZZ_Z import MUL_ZZ_Z
from TRANS_N_Z import TRANS_N_Z
from NZER_N_B import NZER_N_B
from TRANS_Z_N import TRANS_Z_N
from RED_Q_Q import RED_Q_Q

def DIV_QQ_Q(divisible_accepted: rat, divider_accepted: rat) -> rat:
    """
    Функция делит одну дробь на другую и возвращает результат в несократимой форме.

    :param divisible_accepted: Делимое (тип rat)
    :param divider_accepted: Делитель (тип rat, должен быть отличен от нуля)
    :return: Результат деления двух дробей в несократимой форме (тип rat)
    :raises ValueError: Если делитель равен нулю
    """
    # Проверяем, что делитель не равен нулю
    if not NZER_N_B(TRANS_Z_N(divider_accepted.num)):
        raise ValueError("Деление на ноль невозможно")

    result = rat(num=nat_0([0], 1), den=ceil([0], 1, 0))
    divisible = divisible_accepted.copy()
    divider = divider_accepted.copy()


    # Умножаем числитель делимого на знаменатель делителя
    result.num = MUL_ZZ_Z(divisible.num,TRANS_N_Z(divider.den))
    # Умножаем знаменатель делимого на числитель делителя
    result.den = MUL_ZZ_Z(TRANS_N_Z(divisible.den), divider.num)

    # Сокращаем полученную дробь до несократимой формы
    return RED_Q_Q(result)