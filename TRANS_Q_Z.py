# Выполнил Кулаков Алексей 3381

# Импортируем модули
from Types import rat, ceil

# Функция для преобразования рационального числа в целое
def TRANS_Q_Z(val: rat) -> ceil:
    # Проверяем, что знаменатель числа равен 1; если нет, то вызываем ошибку
    if val.den.array != [1]:
        raise ValueError("Значение знаменателя должно ровняться единице")
    
    # Создаем копию числителя, чтобы избежать изменений исходного значения
    tmp = val.copy()
    
    # Возвращаем округленное значение числителя в виде целого числа
    return ceil(tmp.num.array, tmp.num.n, 0)