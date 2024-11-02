from Types import ceil, dig  # Импортируем необходимые классы
from ABS_Z_Z import ABS_Z_Z  # Импортируем функцию для вычисления абсолютной величины
from POZ_Z_D import POZ_Z_D  # Импортируем функцию для определения знака
from ADD_NN_N import ADD_NN_N  # Импортируем функцию для сложения натуральных чисел
from SUB_NN_N import SUB_NN_N  # Импортируем функцию для вычитания натуральных чисел
from MUL_ZM_Z import MUL_ZM_Z  # Импортируем функцию для изменения знака целого числа
from COM_NN_D import COM_NN_D
from TRANS_Z_N import TRANS_Z_N


def SUB_ZZ_Z(A: ceil, B: ceil) -> ceil:
    # Вычитает целое число B из целого числа A (A - B).

    sign_A = POZ_Z_D(A)
    sign_B = POZ_Z_D(B)

    # Инициализация значениями по умолчанию
    result_array = []
    result_sign = 0

    # Если одно из чисел равно нулю
    if sign_A == dig(0):
        return MUL_ZM_Z(B)  # -B
    elif sign_B == dig(0):
        return A  # A - 0 = A

    # Если A и B имеют одинаковый знак
    if sign_A == sign_B:
        # Вычисляем абсолютные значения
        abs_A = TRANS_Z_N(ABS_Z_Z(A))
        abs_B = TRANS_Z_N(ABS_Z_Z(B))

        if COM_NN_D(abs_A, abs_B) == 2:  # A > B
            result_array = SUB_NN_N(abs_A, abs_B).array
            result_sign = A.sign
        else:  # A <= B
            result_array = SUB_NN_N(abs_B, abs_A).array
            result_sign = 1 - A.sign

    # Если A и B имеют разные знаки
    elif sign_A == dig(2) and sign_B == dig(1):  # A положительное, B отрицательное
        positive_B = TRANS_Z_N(MUL_ZM_Z(B))  # Меняем знак B
        result_array = ADD_NN_N(TRANS_Z_N(A), positive_B).array
        result_sign = 0  # Результат положительный
    elif sign_A == dig(1) and sign_B == dig(2):  # A отрицательное, B положительное
        positive_A = TRANS_Z_N(MUL_ZM_Z(A))  # Меняем знак A
        result_array = ADD_NN_N(positive_A, TRANS_Z_N(B)).array
        result_sign = 1  # Результат отрицательный

    # Проверка на нулевой результат
    if result_array == [0]:
        result_sign = 0  # Устанавливаем положительный знак для нулевого результата

    return ceil(result_array, len(result_array), result_sign)
