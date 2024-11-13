# Автор: Козлов Г.Е. Группа - ПМИ-3381
from Types import pol, rat, ceil, nat_0
from DIV_QQ_Q import DIV_QQ_Q # деление дробей
from DIV_PP_P import DIV_PP_P


def find_devisors(r: rat) -> list:
    moderator: ceil = int(''.join([str(i) for i in r.num.array]))
    denominator: nat_0 = int(''.join([str(i) for i in r.den.array]))

    devisors = []

    numbers = [int(j) for j in str(moderator)]
    devisors.append(rat(ceil(numbers, len(numbers), 0), nat_0([1], 1)))
    devisors.append(rat(ceil(numbers, len(numbers), 1), nat_0([1], 1)))
    for i in range(2, int(abs(moderator)**0.5 + 1) + 1):
        if moderator % i == 0:
            numbers = [int(j) for j in str(i)]
            devisors.append(rat(ceil(numbers, len(numbers), 0), nat_0([1], 1)))
            devisors.append(rat(ceil(numbers, len(numbers), 1), nat_0([1], 1)))
    

    numbers = [int(j) for j in str(denominator)]
    devisors.append(rat(ceil([1], 1, 0), nat_0(numbers, len(numbers))))
    devisors.append(rat(ceil([1], 1, 1), nat_0(numbers, len(numbers))))
    for i in range(2, int(abs(denominator)**0.5 + 1) + 1):
        if denominator % i == 0:
            numbers = [int(j) for j in str(i)]
            devisors.append(rat(ceil([1], 1, 0), nat_0(numbers, len(numbers))))
            devisors.append(rat(ceil([1], 1, 1), nat_0(numbers, len(numbers))))

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
        new_coefs.append(DIV_QQ_Q(elem, polynom.coefficients[0])) # делим каждый элемент многочлена на старший коэфициент

    polynom = pol(new_coefs, len(new_coefs) - 1)
    null_pol = pol([rat(ceil([0], 1, 0), nat_0([1], 1))], 0) # нулевой поленом

    polynoms = []
    
    while True:
        free_coef = polynom.coefficients[-1] # свободный коэфициент
        devisors = find_devisors(free_coef)
        


p5 = pol([
        rat(ceil([6], 1, 0), nat_0([7], 1)),  # 6/7 * x^0
        rat(ceil([1], 1, 0), nat_0([7], 1)),  # 1/7 * x^1
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
    ], 2)

p2 = pol([
        rat(ceil([6], 1, 1), nat_0([7], 1)),  # -6/7 * x^0
        rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
    ], 1)

print(find_devisors(rat(ceil([6], 1, 1), nat_0([7], 1))))