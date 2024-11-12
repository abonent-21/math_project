# ADD_NN_N.py
# Модуль ADD_NN_N
# Сложение натуральных чисел

# Автор: Самигулин Д.А. Группа - ПМИ-3381

from Types import nat_0    # Импортируем класс nat_0
from COM_NN_D import COM_NN_D  # Импортируем функцию сравнения натуральных чисел

def ADD_NN_N(A: nat_0, B: nat_0) -> nat_0:
    """
    Суммирует два натуральных числа A и B.

    :param A: первое натуральное число (nat_0)
    :param B: второе натуральное число (nat_0)
    :return: сумма A + B (nat_0)
    """
    # Изначально предполагаем, что A длиннее или равно B
    longer = A
    shorter = B

    comparison = COM_NN_D(A, B)          # Сравниваем числа A и B
    if comparison.value == 1:
        longer, shorter = B, A            # Если A < B, то B - длиннее

    max_len = longer.n                   # Длина результата равна длине большего числа
    result_len = max_len                 # Инициализируем длину результата
    longer_digits = longer.array.copy()  # Копируем массив цифр длинного числа
    shorter_digits = shorter.array.copy()  # Копируем массив цифр короткого числа

    # Выравниваем длину короткого числа, добавляя ведущие нули
    shorter_digits = [0] * (max_len - shorter.n) + shorter_digits

    result = [0] * max_len               # Инициализируем массив для результата
    carry = 0                            # Переменная для переноса

    # Складываем цифры с конца
    for i in range(max_len - 1, -1, -1):
        total = longer_digits[i] + shorter_digits[i] + carry  # Суммируем цифры и перенос
        result[i] = total % 10         # Записываем цифру результата
        carry = total // 10            # Обновляем перенос

    if carry:
        result = [carry] + result        # Добавляем перенос в начало массива
        result_len += 1                  # Увеличиваем длину результата на 1

    return nat_0(result, result_len)     # Возвращаем сумму как объект nat_0
