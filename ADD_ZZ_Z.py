# ADD_ZZ_Z.py

# Автор: Самигулин Д.А. Группа - ПМИ-3381

from Types import nat_0, ceil  # Импортируем необходимые классы
from ADD_NN_N import ADD_NN_N  # Импортируем функцию сложения натуральных чисел
from SUB_NN_N import SUB_NN_N  # Импортируем функцию вычитания натуральных чисел
from COM_NN_D import COM_NN_D  # Импортируем функцию сравнения натуральных чисел
from POZ_Z_D import POZ_Z_D    # Импортируем функцию определения знака целого числа
from ABS_Z_Z import ABS_Z_Z    # Импортируем функцию получения модуля целого числа

def ADD_ZZ_Z(A: ceil, B: ceil) -> ceil:
    """
    Суммирует два целых числа A и B.

    :param A: первое целое число (ceil)
    :param B: второе целое число (ceil)
    :return: сумма A + B (ceil)
    """
    # Получаем модули чисел A и B как целые числа со знаком 0
    abs_A = ABS_Z_Z(A)  # Модуль числа A (ceil со знаком 0)
    abs_B = ABS_Z_Z(B)  # Модуль числа B (ceil со знаком 0)

    # Определяем знаки чисел A и B с помощью POZ_Z_D
    sign_A = POZ_Z_D(A).value  # 2 - положительное, 0 - ноль, 1 - отрицательное
    sign_B = POZ_Z_D(B).value

    # Преобразуем значения функции POZ_Z_D в обозначения знака (0 или 1)
    # 2 (положительное) -> 0
    # 1 (отрицательное) -> 1
    # 0 (ноль) оставляем 0
    if sign_A == 2:
        sign_A = 0  # Положительное число
    elif sign_A == 1:
        sign_A = 1  # Отрицательное число

    if sign_B == 2:
        sign_B = 0
    elif sign_B == 1:
        sign_B = 1

    # Создаем объекты nat_0 из модулей чисел
    abs_A_nat = nat_0(abs_A.array.copy(), abs_A.n)
    abs_B_nat = nat_0(abs_B.array.copy(), abs_B.n)

    if sign_A == sign_B:
        # Если знаки совпадают, складываем модули и сохраняем знак
        sum_nat = ADD_NN_N(abs_A_nat, abs_B_nat)
        result = ceil(sum_nat.array, sum_nat.n, sign_A)
    else:
        # Если знаки разные, вычитаем меньший модуль из большего
        comp = COM_NN_D(abs_A_nat, abs_B_nat)
        if comp.value == 0:
            # Модули равны, результат ноль со знаком 0
            result = ceil([0], 1, 0)
        elif comp.value == 2:
            # Модуль A больше модуля B
            diff_nat = SUB_NN_N(abs_A_nat, abs_B_nat)
            result = ceil(diff_nat.array, diff_nat.n, sign_A)
        else:
            # Модуль B больше модуля A
            diff_nat = SUB_NN_N(abs_B_nat, abs_A_nat)
            result = ceil(diff_nat.array, diff_nat.n, sign_B)
    return result
