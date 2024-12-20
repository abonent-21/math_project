# Автор: Козлов Георгий. Группа - ПМИ-3381

from Types import ceil  # Импортируем класс ceil из модуля Types

def ABS_Z_Z(number: ceil) -> ceil:
    """
    Функция для вычисления абсолютной величины числа.
    Параметры:
    - number: объект класса ceil, представляющий целое число с возможным знаком.
    
    Возвращает:
    - Объект класса ceil с положительным значением (абсолютная величина).
    """
    num = number.copy()  # Создаем копию переданного числа
    num.sign = 0  # Устанавливаем знак на положительный
    return num  # Возвращаем объект с положительным значением
