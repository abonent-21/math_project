# Автор: Марков М.М. Группа - ПМИ-3381

from Types import nat_0, dig
from DIV_NN_Dk import DIV_NN_Dk


def test_div_nn_dk():
    # Тестирование функции DIV_NN_Dk

    # Малые числа
    assert DIV_NN_Dk(nat_0([4], 1), nat_0([2], 1)) == nat_0([2], 1)  # 4 // 2 = 2
    assert DIV_NN_Dk(nat_0([9], 1), nat_0([3], 1)) == nat_0([3], 1)  # 9 // 3 = 3
    assert DIV_NN_Dk(nat_0([5], 1), nat_0([1], 1)) == nat_0([5], 1)  # 5 // 1 = 5

    # Средние числа
    assert DIV_NN_Dk(nat_0([1, 2], 2), nat_0([3], 1)) == nat_0([4], 1)  # 12 // 3 = 4 -> 4, k = 0
    assert DIV_NN_Dk(nat_0([1, 5, 0], 3), nat_0([5], 1)) == nat_0([3, 0], 2)  # 150 // 5 = 30 -> 3, k = 1

    # Большие числа
    assert DIV_NN_Dk(nat_0([1, 0, 0, 0, 0], 5), nat_0([2], 1)) == nat_0([5, 0, 0, 0],
                                                                        4)  # 100000 // 2 = 50000 -> 50000, k = 4
    assert DIV_NN_Dk(nat_0([9, 9, 9, 9], 4), nat_0([1, 0, 0], 3)) == nat_0([9, 0], 2)  # 9999 // 100 = 99 -> 90, k = 1

    # Пограничные значения
    assert DIV_NN_Dk(nat_0([1], 1), nat_0([1], 1)) == nat_0([1], 1)  # 1 // 1 = 1

    # Проверка деления на 0
    try:
        DIV_NN_Dk(nat_0([3], 1), nat_0([0], 1))  # Ошибка: деление на ноль
    except ValueError as e:
        assert str(e) == "Деление на ноль невозможно"

    print("Все тесты для DIV_NN_Dk пройдены успешно!")
