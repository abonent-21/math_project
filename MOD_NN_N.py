# MOD_NN_N.py
# Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля)
# Автор: Бескончин М.А. Группа - ПМИ-3381


from Types import nat_0
import COM_NN_D
import DIV_NN_N
import SUN_NDN_N
import MUL_NN_N

def MOD_NN_N(A: nat_0, B: nat_0) -> nat_0:
    # Проверка на деление на ноль
    if B.array == [0]:
        raise ValueError("Делитель не может быть нулем")

    # Проверка, чтобы A было больше или равно B
    if COM_NN_D(A, B) == 1:
        raise ValueError("2 число больше 1")

    num1 = A.copy()  # Создание копии числа A
    num2 = B.copy()  # Создание копии числа B

    integer = DIV_NN_N(num1, num2)
    result = SUN_NDN_N(num1, MUL_NN_N(integer, num2), 1)

    return result
