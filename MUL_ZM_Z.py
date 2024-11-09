# Автор: Козлов Георгий. Группа - ПМИ-3381
from Types import ceil  # Импортируем класс ceil из модуля Types

def MUL_ZM_Z(number: ceil) -> ceil:
    """
    Функция для умножения целого числа на (-1).
    
    Параметры:
    - number: объект класса ceil, представляющий целое число с возможным знаком.
    
    Возвращает:
    - Объект класса ceil с изменённым знаком числа.
    """
    num = number.copy()  # Создаем копию переданного числа
    if num.array == [0]:  # Если число равно 0
        return num  # Возвращаем 0 без изменений
    num.sign = (num.sign + 1) % 2  # Меняем знак числа (0 на 1 и наоборот)
    return num  # Возвращаем объект с изменённым знаком

    