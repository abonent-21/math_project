# SUB_QQ_Q.py
# Вычитание дробей
# Автор: Бескончин М.А. Группа - ПМИ-3381

from Types import rat, nat_0,ceil

from COM_NN_D import COM_NN_D
from SUB_ZZ_Z import SUB_ZZ_Z
from RED_Q_Q import RED_Q_Q
from LCM_NN_N import LCM_NN_N
from TRANS_Z_N import TRANS_Z_N
from MUL_ZZ_Z import MUL_ZZ_Z
from TRANS_N_Z import TRANS_N_Z
from DIV_NN_N import DIV_NN_N



def SUB_QQ_Q(minuend_accepted: rat, subtrahend_accepted: rat) -> rat:
    """
    Функция вычитает одну дробь из другой и возвращает результат в несократимой форме.

    :param minuend_accepted: Минуенд (откуда вычитаем), тип rat
    :param subtrahend_accepted: Субтрахенд (что вычитаем), тип rat
    :return: Результат вычитания двух дробей в несократимой форме, тип rat
    """

    result = rat(num=ceil([0], 1,0), den=nat_0([1], 1))
    minuend = minuend_accepted.copy()
    subtrahend = subtrahend_accepted.copy()

    # Сравниваем знаменатели двух дробей
    if COM_NN_D(minuend.den, subtrahend.den).value == 0:
        """
        Если знаменатели равны, то можно напрямую вычесть числители.
        """
        # Вычитание числителей двух дробей
        minuend.num = SUB_ZZ_Z(minuend.num, subtrahend.num)
        # Сокращение полученной дроби до несократимой формы и возврат результата
        return RED_Q_Q(minuend)
    # Находим наименьшее общее кратное знаменателей
    result.den = LCM_NN_N(TRANS_Z_N(minuend.den), TRANS_Z_N(subtrahend.den))

    # Приводим числители к общему знаменателю и вычитаем их
    # Формула:
    # (a/b) - (c/d) = (a*(LCM/b) - c*(LCM/d)) / LCM
    result.num = SUB_ZZ_Z(
        MUL_ZZ_Z(
            TRANS_N_Z(DIV_NN_N(result.den, minuend.den)),  # Преобразуем (LCM / b) из nat_0 в целое число
            minuend.num  # Умножаем на числитель первой дроби
        ),
        MUL_ZZ_Z(
            TRANS_N_Z(DIV_NN_N(result.den, subtrahend.den)),  # Преобразуем (LCM / d) из nat_0 в целое число
            subtrahend.num  # Умножаем на числитель второй дроби
        )
    )

    # Сокращаем полученную дробь до несократимой формы и возвращаем результат
    return RED_Q_Q(result)