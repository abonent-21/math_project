# Выполнил Кулаков Алексей 3381

# Импортируем необходимые функции
from GCF_NN_N import GCF_NN_N  
from DIV_ZZ_Z import DIV_ZZ_Z  
from DIV_NN_N import DIV_NN_N  
from Types import rat, nat_0  

# Функция для сокращения рационального числа
def RED_Q_Q(val: rat) -> rat:
    # Вычисляем НОД абсолютного значения числителя и знаменателя
    natNum = nat_0(val.num.array.copy(), val.num.n)
    n = GCF_NN_N(natNum, val.den)
    
    # Делим числитель на НОД, чтобы сократить дробь
    val.num = DIV_ZZ_Z(val.num, n)
    
    # Делим знаменатель на НОД, чтобы сократить дробь
    val.den = DIV_NN_N(val.den, n)
    
    # Возвращаем сокращенное рациональное число
    return val
