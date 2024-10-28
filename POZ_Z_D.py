from Types import ceil, dig


def POZ_Z_D(number: ceil) -> dig:
    """
    Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
    """
    num = number.copy() 
    if num.array == [0]:
        return dig(0)
    elif num.sign == 1:
        return dig(1)
    elif num.sign == 0:
        return dig(2)

    
