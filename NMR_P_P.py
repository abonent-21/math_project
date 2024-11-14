# Автор: Козлов Г.Е. Группа - ПМИ-3381
from Types import pol, rat, ceil, nat_0
from DIV_QQ_Q import DIV_QQ_Q # деление дробей
from DIV_PP_P import DIV_PP_P # деление полиномов
from MOD_PP_P import MOD_PP_P # отсаток от деления полиномов
from MUL_PP_P import MUL_PP_P # умножение полиномов

def find_devisors(r: rat) -> list:
    """
    Функция по нахождению делителей свободного коэфициента
    """
    moderator: ceil = int(''.join([str(i) for i in r.num.array])) # числитель
    denominator: nat_0 = int(''.join([str(i) for i in r.den.array])) # знаменатель

    devisors_moderator = [] # список делителей числителя

    numbers = [int(j) for j in str(moderator)] # числитель
    devisors_moderator.append(rat(ceil(numbers, len(numbers), 0), nat_0([1], 1))) # знаменатель с + как делитель
    devisors_moderator.append(rat(ceil(numbers, len(numbers), 1), nat_0([1], 1))) # знаменатель с - как делитель
    for i in range(1, int(abs(moderator)**0.5 + 1) + 1): # все делители числителя
        if moderator % i == 0:
            numbers = [int(j) for j in str(i)]
            devisors_moderator.append(rat(ceil(numbers, len(numbers), 0), nat_0([1], 1)))
            devisors_moderator.append(rat(ceil(numbers, len(numbers), 1), nat_0([1], 1)))
    
    devisors_denominator = [] # список делителей знаменателя

    numbers = [int(j) for j in str(denominator)] # знаменатель
    devisors_denominator.append(rat(ceil([1], 1, 0), nat_0(numbers, len(numbers)))) # числитель с + как делитель
    devisors_denominator.append(rat(ceil([1], 1, 1), nat_0(numbers, len(numbers)))) # числитель с - как делитель
    for i in range(1, int(abs(denominator)**0.5 + 1) + 1): # все делители знаменателя
        if denominator % i == 0:
            numbers = [int(j) for j in str(i)]
            devisors_denominator.append(rat(ceil([1], 1, 0), nat_0(numbers, len(numbers))))
            devisors_denominator.append(rat(ceil([1], 1, 1), nat_0(numbers, len(numbers))))

    devisors = []

    for i in devisors_moderator:
        for j in devisors_denominator:
            rat_num = rat(ceil(i.num.array, i.num.n, i.num.sign), nat_0(j.den.array, j.den.n))
            if rat_num not in devisors:
                devisors.append(rat_num)
    
    devisors += devisors_moderator + devisors_denominator

    return devisors



def NMR_P_P(polym: pol) -> pol:
    """
    Функция преобразования многочлена. Пример (x-5)^3 * (x - 3)^2 --> (x-5)(x-3)
    """
    assert isinstance(polym, pol)

    polynom = polym.copy()

    # Первоначальное преобразование. Пример: 7x^2 + x - 6 ---> x^2 + (1/7)x - 6/7 
    new_coefs = []
    for elem in polynom.coefficients:
        new_coefs.append(DIV_QQ_Q(elem, polynom.coefficients[-1])) # делим каждый элемент многочлена на старший коэфициент

    polynom = pol(new_coefs, len(new_coefs) - 1)
    null_pol = pol([rat(ceil([0], 1, 0), nat_0([1], 1))], 0) # нулевой поленом
    union_pol = pol([rat(ceil([1], 1, 0), nat_0([1], 1))], 0) # единичный полином

    polynoms = []

    free_coef = polynom.coefficients[0] # свободный коэфициент
    devisors = find_devisors(free_coef) # делители свободного коэфициента
    idx_div = 0 # индекс делителя в списке делителей
    while idx_div != len(devisors) and polynom != union_pol:
        devisor_polym = pol([
                            devisors[idx_div],  # потенцияальное решение уравнения
                            rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
                            ], 1)
        if MOD_PP_P(polynom, devisor_polym) == null_pol:
            polynom = DIV_PP_P(polynom, devisor_polym)
            if devisor_polym not in polynoms:
                polynoms.append(devisor_polym)
        else:
            idx_div += 1
    if polynoms:
        new_polym = polynoms[0]
        for i in range(1, len(polynoms)):
            new_polym = MUL_PP_P(new_polym, polynoms[i]) # собираем все в единый полином
        return new_polym
    return None