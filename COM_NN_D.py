# COM_NN_D.py
# Модуль COM_NN_D
# Сравнение натуральных чисел:
# 2 - если первое больше второго,
# 0 - если равно,
# 1 - если первое меньше второго.

# Автор: Самигулин Д.А. Группа - ПМИ-3381

from Types import nat_0, dig  # Импортируем классы nat_0 и dig

def COM_NN_D(A: nat_0, B: nat_0) -> dig:
    """
    Сравнивает два натуральных числа A и B.

    :param A: первое натуральное число (nat_0)
    :param B: второе натуральное число (nat_0)
    :return: результат сравнения (dig)
    """
    if A.n > B.n:
        return dig(2)                    # Если длина A больше, то A > B
    elif A.n < B.n:
        return dig(1)                    # Если длина A меньше, то A < B
    else:
        for i in range(A.n):
            a_digit = A.array[i]         # Текущая цифра из A
            b_digit = B.array[i]         # Текущая цифра из B
            if a_digit > b_digit:
                return dig(2)            # Если цифра A больше, то A > B
            elif a_digit < b_digit:
                return dig(1)            # Если цифра A меньше, то A < B
        return dig(0)                    # Если все цифры равны, то A == B
