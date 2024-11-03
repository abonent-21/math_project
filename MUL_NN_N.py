# Автор: Марков М.М. Группа - ПМИ-3381

from Types import nat_0, dig
from MUL_ND_N import MUL_ND_N
from MUL_Nk_N import MUL_Nk_N
from ADD_NN_N import ADD_NN_N


def MUL_NN_N(A: nat_0, B: nat_0) -> nat_0:
    # Умножение натуральных чисел A и B

    # Если одно из чисел равно нулю, результат — [0]
    if A.array == [0] or B.array == [0]:
        return nat_0([0], 1)

    # Начинаем с результата, равного [0] (объект nat_0)
    result = nat_0([0], 1)

    # Перебираем цифры второго числа B с конца
    for i in range(B.n - 1, -1, -1):
        digit = dig(B.array[i])  # Получаем текущую цифру B[i]

        # Умножаем A на текущую цифру B[i]
        partial_product = MUL_ND_N(A, digit)  # Умножение A на B[i]

        # Сдвиг на нужное количество позиций, преобразуем сдвиг в nat_0
        shift = B.n - 1 - i
        partial_product = MUL_Nk_N(partial_product, shift)  # Сдвиг на shift позиций

        # Добавляем частичное произведение к общему результату
        result = ADD_NN_N(result, partial_product)

    return result


