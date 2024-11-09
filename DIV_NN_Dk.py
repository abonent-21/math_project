# Автор: Марков М.М. Группа - ПМИ-3381

from Types import nat_0, dig
from MUL_Nk_N import MUL_Nk_N
from COM_NN_D import COM_NN_D
from SUB_NN_N import SUB_NN_N


def DIV_NN_Dk(A: nat_0, B: nat_0) -> nat_0:
    # Вычисление первой цифры деления большего натурального на меньшее,
    # домноженное на 10^k, где k - номер позиции этой цифры
    # (номер считается с нуля), результат - натуральное   223 / 2 = 111.5 -> 100

    if B.array == [0]:  # Проверка на деление на ноль
        raise ValueError("Деление на ноль невозможно")

    # Инициализация переменных
    sub_count = 0  # Счетчик, сколько раз B помещается в A

    # Временная переменная для вычитания
    tmp = A.copy()

    # Пока A >= B, выполняем вычитание
    while COM_NN_D(tmp, B).value in (0, 2):
        tmp = SUB_NN_N(tmp, B)  # tmp = tmp - B
        sub_count += 1

    # Получаем первую цифру из sub_count
    first_digit = int(str(sub_count)[0])  # Первая цифра деления
    k = len(str(sub_count)) - 1  # Позиция цифры деления большего на меньшее

    # Создаем nat_0 с первой цифрой
    result = nat_0([first_digit], 1)  # Создаем nat_0 с первой цифрой

    # Умножаем первую цифру на 10^k, если k > 0
    if k > 0:
        result = MUL_Nk_N(result, k)  # Умножаем на 10^k

    return result
