# # Автор: Козлов Г.Е. Группа - ПМИ-3381

from Types import rat, pol, ceil, nat_0
from MOD_PP_P import MOD_PP_P
from MUL_PP_P import MUL_PP_P

def GCF_PP_P(first_pol: pol, second_pol: pol) -> pol:
    """
    НОД многочленов
    """
    pass

p = pol([
    rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
    rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
], 1)
q = pol([
    rat(ceil([3], 1, 0), nat_0([1], 1)),  # 3 * x^0
], 0)

result = MUL_PP_P(p, q)

p1 = pol([
    rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
    rat(ceil([2], 1, 0), nat_0([1], 1)),  # 2 * x^1
    rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^2
], 2)
p2 = pol([
    rat(ceil([1], 1, 0), nat_0([1], 1)),  # 1 * x^0
    rat(ceil([1], 1, 0), nat_0([1], 1))   # 1 * x^1
], 1)

result = MOD_PP_P(p1, p2)