from Types import pol, rat, ceil, nat_0
from MUL_QQ_Q import MUL_QQ_Q


def DER_P_P(polym: pol) -> pol:
    """
    Функция вычиляющая производную полинома
    """
    assert isinstance(polym, pol)
    # Коэффициенты производной
    derived_coeffs = []

    null_pol = pol([rat(ceil([0], 1, 0), nat_0([1], 1))], 0) # нулевой поленом

    if polym == null_pol: # если полином нулевой, но возвращаем, нулевой полином
        return null_pol
    # Перебираем коэффициенты исходного многочлена
    for i, coef in enumerate(polym.coefficients):
        if i > 0:  # Первая степень (i = 0) в производной исчезает
            mul_coef = rat(ceil([i], 1, 0), nat_0([1], 1))

            elem = MUL_QQ_Q(mul_coef, coef)
            derived_coeffs.append(elem)

    # Степень производной будет на 1 меньше, чем у исходного многочлена
    return pol(derived_coeffs, polym.m - 1)

