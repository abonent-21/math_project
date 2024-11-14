# Автор: Сычев Н.С. Группа - ПМИ-3381

from Types import pol, rat
from ABS_Z_Z import ABS_Z_Z
from GCF_NN_N import GCF_NN_N
from LCM_NN_N import LCM_NN_N
from TRANS_N_Z import TRANS_N_Z
from DIV_NN_N import DIV_NN_N


def FAC_P_Q(p: pol) -> rat:
    """
    Функция для вычисления НОД (GCD) числителей и НОК (LCM) знаменателей многочлена с рациональными коэффициентами
    Эта функция нужна для упрощения полинома.
    Мы выносим полученное значение за скобки, получая удобный для решения полином.
    """
    
    # Получаем числители из коэффициентов (рациональные числа)
    # Переводим их в натуральные числа, так как НОД - натуральное число.
    numerators = [ABS_Z_Z(coeff.num) for coeff in p.coefficients] 
    
    # Получаем знаменатели из коэффициентов (натуральные числа).
    denominators = [coeff.den for coeff in p.coefficients] 
    
    # Определяем начальное значение для НОДа как первый числитель.
    gcd = numerators[0] 
    
    # Если коэффициентов больше одного, вычисляем НОД всех числителей.
    if p.m > 1: 
        for i in numerators[1:]:
            gcd = GCF_NN_N(gcd, i)
    
    # Проводим те же самые действия для НОКа.
    lcm = denominators[0]
    if p.m > 1: # если коэффицентов полинома больше 1, то на каждой итерации вычисляем НОК. 
        for i in denominators[1:]: 
            lcm = LCM_NN_N(lcm, i)
            
    # На выходе имеем дробь. Сделаем проверку на то, сократима она или нет.
    common_gcd = GCF_NN_N(gcd, lcm)  # Находим общий НОД для числителя и знаменателя
    gcd = DIV_NN_N(gcd, common_gcd) 
    lcm = DIV_NN_N(lcm, common_gcd) 
    
    gcd = TRANS_N_Z(gcd) # Перевод значения НОДа в целое, т.к. на выходе рац. число
    
    return rat(gcd, lcm) 