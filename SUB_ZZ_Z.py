# Автор: Марков М.М. Группа - ПМИ-3381

from Types import ceil
from ABS_Z_Z import ABS_Z_Z
from POZ_Z_D import POZ_Z_D
from ADD_NN_N import ADD_NN_N
from SUB_NN_N import SUB_NN_N
from MUL_ZM_Z import MUL_ZM_Z
from COM_NN_D import COM_NN_D
from TRANS_Z_N import TRANS_Z_N


def SUB_ZZ_Z(A: ceil, B: ceil) -> ceil:
    # Вычитает целое число B из целого числа A (A - B).

    sign_A = POZ_Z_D(A)
    sign_B = POZ_Z_D(B)

    # Вычисляем абсолютные значения A и B
    abs_A = TRANS_Z_N(ABS_Z_Z(A))
    abs_B = TRANS_Z_N(ABS_Z_Z(B))

    # Если A и B имеют одинаковый знак
    if sign_A == sign_B:
        if COM_NN_D(abs_A, abs_B).value == 2:  # A > B
            result_array = SUB_NN_N(abs_A, abs_B).array
            result_sign = A.sign  # Оставляем знак A
        else:  # A <= B
            result_array = SUB_NN_N(abs_B, abs_A).array
            result_sign = 1 - A.sign  # Знак противоположный A

    # Если A и B имеют разные знаки
    else:
        if sign_A.value == 2:  # A положительное
            # A + |B| (так как B отрицательное)
            result_array = ADD_NN_N(TRANS_Z_N(A), TRANS_Z_N(MUL_ZM_Z(B))).array
            result_sign = 0  # Результат положительный
        else:  # A отрицательное, B положительное
            # |A| + B
            result_array = ADD_NN_N(TRANS_Z_N(MUL_ZM_Z(A)), TRANS_Z_N(B)).array
            result_sign = 1  # Результат отрицательный

    # Проверка на нулевой результат
    if result_array == [0]:
        result_sign = 0  # Нулевой результат всегда положительный

    return ceil(result_array, len(result_array), result_sign)
