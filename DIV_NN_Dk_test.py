# Автор: Марков М.М. Группа - ПМИ-3381

from Types import nat_0, dig
from DIV_NN_Dk import DIV_NN_Dk


def test_div_nn_dk():
    # Тестирование функции DIV_NN_Dk

    # Малые числа
    assert DIV_NN_Dk(nat_0([5], 1), nat_0([2], 1), 0) == dig(2)  # 5 // 2 = 2
    assert DIV_NN_Dk(nat_0([8], 1), nat_0([4], 1), 0) == dig(2)  # 8 // 4 = 2
    assert DIV_NN_Dk(nat_0([7], 1), nat_0([3], 1), 0) == dig(2)  # 7 // 3 = 2

    # Средние числа
    assert DIV_NN_Dk(nat_0([9, 0], 2), nat_0([3], 1), 1) == dig(3)  # 90 // (3 * 10) = 3
    assert DIV_NN_Dk(nat_0([1, 5, 6], 3), nat_0([7], 1), 1) == dig(2) # 156 // (7 * 10) = 2
    assert DIV_NN_Dk(nat_0([5, 4, 3], 3), nat_0([5], 1), 1) == dig(1)  # 543 // (5 * 10) = 1

    # Большие числа
    assert DIV_NN_Dk(nat_0([9, 9, 9], 3), nat_0([3, 3], 2), 1) == dig(3)  # 999 // (33 * 10) = 3
    assert DIV_NN_Dk(nat_0([7, 0, 0, 0], 4), nat_0([2, 5, 0], 3), 1) == dig(2)  # 7000 // (250 * 10) = 2
    assert DIV_NN_Dk(nat_0([5, 2, 5, 3, 1, 7, 8, 5, 7, 3, 2], 11), nat_0([7, 5, 1], 3),
                     3) == dig(6)  # 52531785732 // (751 * 10^3) = 6

    # Пограничные значения
    assert DIV_NN_Dk(nat_0([1], 1), nat_0([1], 1), 0) == dig(1)  # 1 // 1 = 1

    # Проверка деления на 0
    try:
        DIV_NN_Dk(nat_0([3], 1), nat_0([0], 1), 0)  # Ошибка: деление на ноль
    except ValueError as e:
        assert str(e) == "Делитель не может быть нулем"

    print("Все тесты для DIV_NN_Dk пройдены успешно!")


if __name__ == "__main__":
    test_div_nn_dk()
