# Автор: Марков М.М. Группа - ПМИ-3381

from SUB_NN_N import SUB_NN_N
from MUL_ND_N import MUL_ND_N
from COM_NN_D import COM_NN_D
from Types import nat_0


def SUB_NDN_N(A: nat_0, B: nat_0, D: int) -> nat_0:
    # Вычитание из натурального числа другого натурального,
    # умноженного на цифру, результат - натуральное.

    # Умножаем B на D, результат - nat_0 (BD - это B*D)
    BD = MUL_ND_N(B, D)

    # Проверяем, что A >= B * D для неотрицательного результата
    if COM_NN_D(A, BD) == 1:
        raise ValueError("Результат вычитания будет отрицательным")

    # Вычитаем B * D из A
    result = SUB_NN_N(A, BD)
    return result
