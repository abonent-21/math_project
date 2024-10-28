# Автор: Марков М.М. Группа - ПМИ-3381

from Types import nat_0, dig
from MUL_Nk_N import MUL_Nk_N
from COM_NN_D import COM_NN_D
from SUB_NN_N import SUB_NN_N


def DIV_NN_Dk(A: nat_0, B: nat_0, k: int) -> dig:
    # Вычисление первой цифры деления большего натурального на меньшее,
    # домноженное на 10^k, где k - номер позиции этой цифры
    # (номер считается с нуля), результат - цифра

    if B.array == [0]:  # Проверка на деление на ноль
        raise ValueError("Делитель не может быть нулем")

    # Умножаем делитель B на 10^k
    scaled_B = MUL_Nk_N(B, k)

    # Ищем, сколько раз scaled_B помещается в A
    sub_count = 0

    # Пока A >= scaled_B, выполняем вычитание
    while COM_NN_D(A, scaled_B) != 1:
        A = SUB_NN_N(A, scaled_B)  # A = A - scaled_B
        sub_count += 1

    # Получаем первую цифру из sub_count
    first_digit = int(str(sub_count)[0]) if sub_count >= 10 else sub_count
    return dig(first_digit)
