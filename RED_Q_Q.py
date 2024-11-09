# Выполнил Кулаков Алексей 3381

# Импортируем необходимые функции
from ABS_Z_N import ABS_Z_N  
from GCF_NN_N import GCF_NN_N  
from DIV_ZZ_Z import DIV_ZZ_Z  
from DIV_NN_N import DIV_NN_N  
from Types import rat  

# Функция для сокращения рационального числа
def RED_Q_Q(val: rat) -> rat:
    # Вычисляем НОД абсолютного значения числителя и знаменателя
    n = GCF_NN_N(ABS_Z_N(val.num), val.den)
    
    # Делим числитель на НОД, чтобы сократить дробь
    val.num = DIV_ZZ_Z(val.num, n)
    
    # Делим знаменатель на НОД, чтобы сократить дробь
    val.den = DIV_NN_N(val.den, n)
    
    # Возвращаем сокращенное рациональное число
    return val
