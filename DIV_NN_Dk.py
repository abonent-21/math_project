# Автор: Марков М.М. Группа - ПМИ-3381

from Types import nat_0
from COM_NN_D import COM_NN_D
from SUB_NN_N import SUB_NN_N
from MUL_Nk_N import MUL_Nk_N


def DIV_NN_Dk(A: nat_0, B: nat_0) -> nat_0:
    # Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k,
    # где k - номер позиции этой цифры (номер считается с нуля), результат - натуральное

    if B.array == [0]:  # Проверка на деление на ноль
        raise ValueError("Деление на ноль невозможно")
    elif COM_NN_D(A, B).value == 1:
        raise ValueError("Нельзя поделить меньшее число на большее в натуральных числах")

    # Создаем временные объекты `nat_0` для частей чисел, используя срезы массива
    num_part = nat_0(A.array[:B.n + 1], len(A.array[:B.n + 1]))
    denom_part = nat_0(B.array[:B.n], B.n)

    # Инициализация счётчика для первой значащей цифры
    sub_count = 0

    # Циклическое вычитание для нахождения первой цифры результата деления
    while COM_NN_D(num_part, denom_part).value in (0, 2):  # пока num_part >= denom_part
        num_part = SUB_NN_N(num_part, denom_part)  # num_part -= denom_part
        sub_count += 1  # Увеличиваем счётчик при каждом вычитании

    first_digit = int(str(sub_count)[0])  # Первая цифра деления
    k = A.n - denom_part.n - 1 + len(str(sub_count)) - 1  # Позиция цифры деления большего на меньшее

    # Создаем nat_0 с первой цифрой
    result = nat_0([first_digit], 1)  # Создаем nat_0 с первой цифрой

    # Умножаем первую цифру на 10^k, если k > 0
    if k > 0:
        result = MUL_Nk_N(result, k)  # Умножаем на 10^k

    return result
