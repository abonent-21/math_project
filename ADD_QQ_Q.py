# ADD_QQ_Q.py
# Сложение дробей
# Автор: Бескончин М.А. Группа - ПМИ-3381

from Types import rat, nat_0,ceil

from COM_NN_D import COM_NN_D
from ADD_ZZ_Z import ADD_ZZ_Z
from RED_Q_Q import RED_Q_Q
from LCM_NN_N import LCM_NN_N
from TRANS_Z_N import TRANS_Z_N
from MUL_ZZ_Z import MUL_ZZ_Z
from TRANS_N_Z import TRANS_N_Z
from DIV_NN_N import DIV_NN_N


def ADD_QQ_Q(summand_accepted: rat, addend_accepted: rat) -> rat:
    """
        Функция складывает две дроби (рациональных числа) и возвращает результат в несократимой форме.

        :param summand_accepted: Первое слагаемое (тип rat)
        :param addend_accepted: Второе слагаемое (тип rat)
        :return: Результат сложения двух дробей в несократимой форме (тип rat)
    """
    result = rat(num=ceil([0], 1,0), den=nat_0([1], 1))
    summand = summand_accepted.copy()
    addend = addend_accepted.copy()

    # Сравниваем знаменатели двух дробей
    if COM_NN_D(summand.den, addend.den).value == 0:
        """
        Если знаменатели равны, то можно напрямую сложить числители.
        """
        # Сложение числителей двух дробей
        summand.num = ADD_ZZ_Z(summand.num, addend.num)
        # Сокращение полученной дроби до несократимой формы и возврат результата
        return RED_Q_Q(summand)


    # Находим наименьшее общее кратное знаменателей
    result.den = LCM_NN_N(summand.den, addend.den)
    # Приводим числители к общему знаменателю и складываем их
    # Формула:
    # (a/b) + (c/d) = (a*(LCM/b) + c*(LCM/d)) / LCM
    result.num = ADD_ZZ_Z(
        MUL_ZZ_Z(
            TRANS_N_Z(DIV_NN_N(result.den, summand.den)),  # Преобразуем (LCM / b) из nat_0 в целое число
            summand.num  # Умножаем на числитель первой дроби
        ),
        MUL_ZZ_Z(
            TRANS_N_Z(DIV_NN_N(result.den, addend.den)),  # Преобразуем (LCM / d) из nat_0 в целое число
            addend.num  # Умножаем на числитель второй дроби
        )
    )
    # Сокращение полученной дроби до несократимой формы и возврат результата
    return RED_Q_Q(result)