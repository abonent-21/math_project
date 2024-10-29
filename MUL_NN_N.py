# Автор: Марков М.М. Группа - ПМИ-3381

from Types import nat_0
from MUL_ND_N import MUL_ND_N
from MUL_Nk_N import MUL_Nk_N
from ADD_NN_N import ADD_NN_N


def MUL_NN_N(A: nat_0, B: nat_0) -> nat_0:
    # Если одно из чисел равно нулю, результат — [0]
    if A.array == [0] or B.array == [0]:
        return nat_0([0], 1)

    # Начинаем с результата, равного [0] (объект nat_0)
    result = nat_0([0], 1)

    # Перебираем цифры второго числа B с конца, умножая на первое число A
    for i in range(B.n - 1, -1, -1):
        # Умножаем A на текущую цифру B[i] и сдвигаем результат на (B.n - 1 - i) позиций
        partial_product = MUL_ND_N(A, B.array[i])  # Умножение A на B[i]
        partial_product = MUL_Nk_N(partial_product, nat_0([B.n - 1 - i], 1))  # Сдвиг на нужное количество позиций

        # Добавляем частичное произведение к общему результату
        result = ADD_NN_N(result, partial_product)

    return result
