# Автор: Козлов Георгий. Группа - ПМИ-3381
from Types import ceil, nat_0

def TRANS_Z_N(number: ceil) -> nat_0:
    """
    Преобразование целого неотрицательного в натуральное
    """
    if number.sign == 1:
        raise AssertionError
    num_nat = nat_0(array=number.array.copy(), n=number.n)
    return num_nat
