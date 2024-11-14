from Types import ceil
from SUB_ZZ_Z import SUB_ZZ_Z


def test_sub_zz_z():
    # Тесты для положительных чисел
    assert SUB_ZZ_Z(ceil([5], 1, 0), ceil([3], 1, 0)) == ceil([2], 1, 0)  # 5 - 3 = 2
    assert SUB_ZZ_Z(ceil([9], 1, 0), ceil([4], 1, 0)) == ceil([5], 1, 0)  # 9 - 4 = 5

    # Тесты для отрицательных чисел
    assert SUB_ZZ_Z(ceil([7], 1, 1), ceil([2], 1, 1)) == ceil([5], 1, 1)  # -7 - (-2) = -5
    assert SUB_ZZ_Z(ceil([4], 1, 1), ceil([6], 1, 1)) == ceil([2], 1, 0)  # -4 - (-6) = 2
    assert SUB_ZZ_Z(ceil([4, 2, 6, 7, 2, 1], 6, 1), ceil([5, 7, 2, 1, 7], 5, 1)) \
           == ceil([3, 6, 9, 5, 0, 4], 6, 1)  # -426721 - (-57217) = -369504

    # Тесты для смешанных чисел (положительное - отрицательное и наоборот)
    assert SUB_ZZ_Z(ceil([3], 1, 0), ceil([2], 1, 1)) == ceil([5], 1, 0)  # 3 - (-2) = 5
    assert SUB_ZZ_Z(ceil([4], 1, 1), ceil([5], 1, 0)) == ceil([9], 1, 1)  # -4 - 5 = -9
    assert SUB_ZZ_Z(ceil([4, 2, 6, 7, 2, 1], 6, 1), ceil([5, 7, 2, 1, 7], 5, 0)) \
           == ceil([4, 8, 3, 9, 3, 8], 6, 1)  # -426721 - 57217 = -483938

    # Тесты для нуля
    assert SUB_ZZ_Z(ceil([0], 1, 0), ceil([3], 1, 0)) == ceil([3], 1, 1)  # 0 - 3 = -3
    assert SUB_ZZ_Z(ceil([7], 1, 0), ceil([0], 1, 0)) == ceil([7], 1, 0)  # 7 - 0 = 7
    assert SUB_ZZ_Z(ceil([0], 1, 0), ceil([0], 1, 0)) == ceil([0], 1, 0)  # 0 - 0 = 0

    # Тесты для одинаковых чисел (должен возвращать 0)
    assert SUB_ZZ_Z(ceil([3], 1, 0), ceil([3], 1, 0)) == ceil([0], 1, 0)  # 3 - 3 = 0
    assert SUB_ZZ_Z(ceil([5], 1, 1), ceil([5], 1, 1)) == ceil([0], 1, 0)  # -5 - (-5) = 0

    print("Все тесты для SUB_ZZ_Z пройдены успешно!")


if __name__ == "__main__":
    test_sub_zz_z()
