# SUB_NN_N.py
# Модуль SUB_NN_N
# Вычитание из первого большего натурального числа второго меньшего или равного

# Автор: Самигулин Д.А. Группа - ПМИ-3381

from COM_NN_D import COM_NN_D   # Импортируем функцию сравнения натуральных чисел
from Types import nat_0, dig    # Импортируем классы nat_0 и dig

def SUB_NN_N(A: nat_0, B: nat_0) -> nat_0:
    """
    Вычитает натуральное число B из A (A >= B).

    :param A: уменьшаемое число (nat_0)
    :param B: вычитаемое число (nat_0)
    :return: разность A - B (nat_0)
    """
    comparison = COM_NN_D(A, B)           # Сравниваем числа A и B
    if comparison.value == 1:
        raise ValueError("Первое число должно быть больше или равно второму")

    A_digits = A.array.copy()             # Копируем массив цифр A
    B_digits = B.array.copy()             # Копируем массив цифр B

    max_len = A.n                         # Длина результата равна длине A
    B_digits = [0] * (max_len - B.n) + B_digits  # Выравниваем длину B

    result_digits = [0] * max_len         # Инициализируем массив для результата
    borrow = 0                            # Переменная для займа

    # Вычитаем цифры с конца
    for i in range(max_len - 1, -1, -1):
        diff = A_digits[i] - B_digits[i] - borrow  # Вычитаем цифры и заем
        if diff < 0:
            diff += 10                    # Если разность отрицательна, берем заем
            borrow = 1
        else:
            borrow = 0
        result_digits[i] = diff           # Записываем разность в результат

    # Удаляем ведущие нули
    while len(result_digits) > 1 and result_digits[0] == 0:
        del result_digits[0]

    result_len = len(result_digits)       # Обновляем длину результата

    return nat_0(result_digits, result_len)  # Возвращаем разность как объект nat_0
