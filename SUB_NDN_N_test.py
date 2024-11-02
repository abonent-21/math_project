# Автор: Марков М.М. Группа - ПМИ-3381

from Types import nat_0, dig
from SUB_NDN_N import SUB_NDN_N


def test_sub_ndn_n():
    # Тестирование функции SUB_NDN_N

    # Малые значения
    assert SUB_NDN_N(nat_0([2], 1), nat_0([1], 1), dig(1)) == nat_0([1], 1)  # 2 - (1 * 1) = 1
    assert SUB_NDN_N(nat_0([3], 1), nat_0([1], 1), dig(2)) == nat_0([1], 1)  # 3 - (1 * 2) = 1
    assert SUB_NDN_N(nat_0([5], 1), nat_0([2], 1), dig(2)) == nat_0([1], 1)  # 5 - (2 * 2) = 1

    # Средние значения
    assert SUB_NDN_N(nat_0([5, 5], 2), nat_0([1, 2], 2), dig(3)) == nat_0([1, 9], 2)  # 55 - (12 * 3) = 19
    assert SUB_NDN_N(nat_0([9, 9, 9], 3), nat_0([3, 3, 3], 3), dig(2)) == nat_0([3, 3, 3], 3)  # 999 - (333 * 2) = 333
    assert SUB_NDN_N(nat_0([7, 2, 4], 3), nat_0([2, 3], 2), dig(2)) == nat_0([6, 7, 8], 3)  # 724 - (23 * 2) = 678

    # Большие значения
    assert SUB_NDN_N(nat_0([1, 0, 0, 0], 4), nat_0([5, 0], 2), dig(3)) == nat_0([8, 5, 0], 3)  # 1000 - (50 * 3) = 850
    assert SUB_NDN_N(nat_0([9, 9, 9, 9], 4), nat_0([3, 3], 2), dig(3)) == nat_0([9, 9, 0, 0], 4)  # 9999 - (33 * 3) = 9900

    # Пограничные значения
    assert SUB_NDN_N(nat_0([1], 1), nat_0([1], 1), dig(0)) == nat_0([1], 1)  # 1 - (1 * 0) = 1
    assert SUB_NDN_N(nat_0([5, 0], 2), nat_0([5, 0], 2), dig(1)) == nat_0([0], 1)  # 50 - (50 * 1) = 0

    # Проверка на отрицательный результат
    try:
        SUB_NDN_N(nat_0([2], 1), nat_0([3], 1), dig(1))  # Ожидаем ValueError
    except ValueError as e:
        assert str(e) == "Результат вычитания будет отрицательным"

    print("Все тесты для SUB_NDN_N пройдены успешно!")


if __name__ == "__main__":
    test_sub_ndn_n()
