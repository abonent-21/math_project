# # Автор: Козлов Г.Е. Группа - ПМИ-3381

from Types import rat, pol, ceil, nat_0, dig
from MOD_PP_P import MOD_PP_P
from DEG_P_N import DEG_P_N
from COM_NN_D import COM_NN_D


def GCF_PP_P(first_pol: pol, second_pol: pol) -> pol:
    """
    НОД многочленов
    """
    assert isinstance(first_pol, pol), "first_pol не принадлежит классу полиномов"
    assert isinstance(second_pol, pol), "second_pol не принадлежит классу полиномов"

    f_pol = first_pol.copy()
    s_pol = second_pol.copy()

    null_pol = pol([rat(ceil([0], 1, 0), nat_0([1], 1))], 0) # нулевой поленом

    pw_f_pol: nat_0 = DEG_P_N(f_pol)
    pw_s_pol: nat_0 = DEG_P_N(s_pol)

    if (COM_NN_D(pw_f_pol, pw_s_pol) == dig(1)): # если первый полином меньше второго, то меняем их меcтами
        f_pol, s_pol = s_pol, f_pol
    
    while s_pol != null_pol:
        ost_pol = MOD_PP_P(f_pol, s_pol)
        f_pol = s_pol
        s_pol = ost_pol
    
    return f_pol