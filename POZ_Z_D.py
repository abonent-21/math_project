# Автор: Козлов Георгий. Группа - ПМИ-3381
from Types import ceil, dig  # Импортируем классы ceil и dig из модуля Types

def POZ_Z_D(number: ceil) -> dig:
    """
    Функция для определения положительности числа.
    
    Параметры:
    - number: объект класса ceil, представляющий целое число с возможным знаком.
    
    Возвращает:
    - Объект класса dig:
      - 2, если число положительное,
      - 0, если число равно нулю,
      - 1, если число отрицательное.
    """
    num = number.copy()  # Создаем копию переданного числа
    if num.array == [0]:  # Проверяем, равно ли число 0
        return dig(0)  # Возвращаем 0 как объект класса dig
    elif num.sign == 1:  # Проверяем, является ли число отрицательным
        return dig(1)  # Возвращаем 1 как объект класса dig
    elif num.sign == 0:  # Если число положительное
        return dig(2)  # Возвращаем 2 как объект класса dig

    
