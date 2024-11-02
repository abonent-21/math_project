# Автор: Марков М.М. Группа - ПМИ-3381

from Types import nat_0, dig


def MUL_ND_N(A: nat_0, digit: dig) -> nat_0:
    # Умножение натурального числа A на цифру digit, результат - натуральное число типа nat_0.

    # Если умножаем на 0, возвращаем число [0] длиной 1
    if digit.value == 0:
        return nat_0([0], 1)

    # Создаем объект nat_0 с длиной A.n + 1, чтобы учесть возможный перенос
    result = nat_0([0] * (A.n + 1), A.n + 1)
    carry = 0  # Перенос

    # Перебираем цифры числа A с конца
    for i in range(A.n - 1, -1, -1):
        product = A.array[i] * digit.value + carry  # Произведение текущей цифры на digit и добавляем перенос
        result.array[i + 1] = product % 10  # Текущая цифра результата
        carry = product // 10  # Обновляем перенос

    # Если остался перенос, записываем его в старшую позицию
    result.array[0] = carry

    # Убираем ведущий ноль, если он не понадобился
    if result.array[0] == 0:
        result = nat_0(result.array[1:], result.n - 1)

    return result  # Возвращаем объект nat_0 с результатом
