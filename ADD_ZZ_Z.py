# ADD_ZZ_Z.py
# Модуль ADD_ZZ_Z
# Сложение целых чисел

# Автор: Самигулин Д.А. Группа - ПМИ-3381

from Types import nat_0, ceil  # Импортируем необходимые классы
from ADD_NN_N import ADD_NN_N  # Импортируем функцию сложения натуральных чисел
from SUB_NN_N import SUB_NN_N  # Импортируем функцию вычитания натуральных чисел
from COM_NN_D import COM_NN_D  # Импортируем функцию сравнения натуральных чисел

def ADD_ZZ_Z(A: ceil, B: ceil) -> ceil:
    """
    Суммирует два целых числа A и B.

    :param A: первое целое число (ceil)
    :param B: второе целое число (ceil)
    :return: сумма A + B (ceil)
    """
    # Если знаки чисел совпадают, складываем модули и сохраняем знак
    if A.sign == B.sign:
        sum_nat = ADD_NN_N(nat_0(A.array, A.n), nat_0(B.array, B.n))  # Складываем модули
        return ceil(sum_nat.array, sum_nat.n, A.sign)  # Знак сохраняется

    else:
        # Если знаки разные, вычитаем меньшее по модулю число из большего
        comp = COM_NN_D(nat_0(A.array, A.n), nat_0(B.array, B.n))

        if comp.value == 0:
            # Если модули равны, результат ноль со знаком 0
            return ceil([0], 1, 0)

        elif comp.value == 2:
            # Модуль A больше модуля B
            diff_nat = SUB_NN_N(nat_0(A.array, A.n), nat_0(B.array, B.n))
            return ceil(diff_nat.array, diff_nat.n, A.sign)  # Знак числа A

        else:
            # Модуль B больше модуля A
            diff_nat = SUB_NN_N(nat_0(B.array, B.n), nat_0(A.array, A.n))
            return ceil(diff_nat.array, diff_nat.n, B.sign)  # Знак числа B
