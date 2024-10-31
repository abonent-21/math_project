# Автор: Козлов Георгий. Группа - ПМИ-3381

from Types import nat_0, ceil  # Импортируем типы nat_0 (натуральное число) и ceil (целое число) из модуля Types

def TRANS_N_Z(number: nat_0) -> ceil:
    """
    Преобразование натурального в целое
    """
    # Создаем новый объект num_ceil типа ceil
    # Для этого копируем массив из number, передаем его длину и устанавливаем знак на 0 (положительный)
    num_ceil = ceil(array=number.array.copy(), n=number.n, sign=0)
    
    return num_ceil  # Возвращаем полученное целое число
