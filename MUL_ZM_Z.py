from Types import ceil


def MUL_ZM_Z(number: ceil) -> ceil:
    """
    Умножение целого на (-1)
    """

    num = number.copy()
    if num.array == [0]:
        return num
    num.sign = (num.sign + 1) % 2
    return num


    