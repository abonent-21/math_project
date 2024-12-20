# Автор: Марков М.М. Группа - ПМИ-3381

from Types import nat_0, dig
from MUL_ND_N import MUL_ND_N


def test_mul_nd():
    # Тестирование функции MUL_ND_N
    # Малые числа
    assert MUL_ND_N(nat_0([1], 1), dig(5)) == nat_0([5], 1)  # 1 * 5 = 5
    assert MUL_ND_N(nat_0([0], 1), dig(9)) == nat_0([0], 1)  # 0 * 9 = 0

    # Средние числа
    assert MUL_ND_N(nat_0([1, 2], 2), dig(3)) == nat_0([3, 6], 2)  # 12 * 3 = 36
    assert MUL_ND_N(nat_0([4], 1), dig(2)) == nat_0([8], 1)  # 4 * 2 = 8
    assert MUL_ND_N(nat_0([5, 5], 2), dig(2)) == nat_0([1, 1, 0], 3)  # 55 * 2 = 110
    assert MUL_ND_N(nat_0([2, 3, 4], 3), dig(4)) == nat_0([9, 3, 6], 3)  # 234 * 4 = 936
    assert MUL_ND_N(nat_0([5, 2, 3], 3), dig(0)) == nat_0([0], 1)  # 523 * 0 = 0

    # Большие числа
    assert MUL_ND_N(nat_0([9, 9], 2), dig(2)) == nat_0([1, 9, 8], 3)  # 99 * 2 = 198
    assert MUL_ND_N(nat_0([1, 5, 7], 3), dig(4)) == nat_0([6, 2, 8], 3)  # 157 * 4 = 628
    assert MUL_ND_N(nat_0([9, 8, 7, 6], 4), dig(3)) == nat_0([2, 9, 6, 2, 8], 5)  # 9876 * 3 = 29628
    assert MUL_ND_N(nat_0([7, 4, 2, 5, 8, 2, 1, 7, 4, 3, 4, 7], 12), dig(5)) == \
           nat_0([3, 7, 1, 2, 9, 1, 0, 8, 7, 1, 7, 3, 5], 13)  # 742582174347 * 5 = 3712910871735
    assert MUL_ND_N(nat_0([1] * 50, 50), dig(2)) == nat_0([2] * 50, 50)  # 111...1 * 2 = 222...2 (50 цифр)

    # Пограничные значения
    assert MUL_ND_N(nat_0([1], 1), dig(0)) == nat_0([0], 1)  # 1 * 0 = 0

    print("Все тесты для MUL_ND_N пройдены успешно!")


if __name__ == "__main__":
    test_mul_nd()
