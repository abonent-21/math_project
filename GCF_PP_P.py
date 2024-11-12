# # Автор: Козлов Г.Е. Группа - ПМИ-3381

from Types import rat, pol, ceil, nat_0
from MOD_PP_P import MOD_PP_P

def GCF_PP_P(first_pol: pol, second_pol: pol) -> pol:
    """
    НОД многочленов
    """
    pass

polynomial_1 = pol([rat(ceil([1], 1, 1), nat_0([1], 1)), 
                    rat(ceil([2], 1, 0), nat_0([1], 1)),
                    rat(ceil([3], 1, 0), nat_0([1], 1)),
                    rat(ceil([4], 1, 0), nat_0([1], 1))], 3)
 
polynomial_2 = pol([rat(ceil([1], 1, 1), nat_0([1], 1)), 
                    rat(ceil([1], 1, 0), nat_0([1], 1)),
                    rat(ceil([1], 1, 0), nat_0([1], 1))], 2)

res = MOD_PP_P(polynomial_1, polynomial_2)
print(res)