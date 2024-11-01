# Пример тестового файла для DIV_ZZ_Z.py
from Types import ceil
from MUL_ZZ_Z import DIV_ZZ_Z

def test_div_zz_z():
    # Тестирование функции DIV_ZZ_Z

    # Тесты на положительных числах
    assert DIV_ZZ_Z(ceil([4], 1), ceil([2], 1)) == ceil([2], 1)  # 4 / 2 = 2
    assert DIV_ZZ_Z(ceil([10], 1), ceil([5], 1)) == ceil([2], 1)  # 10 / 5 = 2
    assert DIV_ZZ_Z(ceil([9], 1), ceil([3], 1)) == ceil([3], 1)   # 9 / 3 = 3

    # Тесты на деление с нулем
    assert DIV_ZZ_Z(ceil([0], 1), ceil([5], 1)) == ceil([0], 1)   # 0 / 5 = 0
    assert DIV_ZZ_Z(ceil([0], 1), ceil([-5], 1)) == ceil([0], 1)  # 0 / -5 = 0

    # Тесты на отрицательных числах
    assert DIV_ZZ_Z(ceil([-4], 1), ceil([2], 1)) == ceil([-2], 1) # -4 / 2 = -2
    assert DIV_ZZ_Z(ceil([4], 1), ceil([-2], 1)) == ceil([-2], 1) # 4 / -2 = -2
    assert DIV_ZZ_Z(ceil([-10], 1), ceil([-5], 1)) == ceil([2], 1) # -10 / -5 = 2

    # Тесты на смешанных знаках
    assert DIV_ZZ_Z(ceil([-9], 1), ceil([3], 1)) == ceil([-3], 1)  # -9 / 3 = -3
    assert DIV_ZZ_Z(ceil([9], 1), ceil([-3], 1)) == ceil([-3], 1)  # 9 / -3 = -3

    # Проверка на деление на 1 и -1
    assert DIV_ZZ_Z(ceil([10], 1), ceil([1], 1)) == ceil([10], 1)   # 10 / 1 = 10
    assert DIV_ZZ_Z(ceil([-10], 1), ceil([-1], 1)) == ceil([10], 1) # -10 / -1 = 10
    assert DIV_ZZ_Z(ceil([10], 1), ceil([-1], 1)) == ceil([-10], 1) # 10 / -1 = -10

    # Проверка на деление на себя
    assert DIV_ZZ_Z(ceil([5], 1), ceil([5], 1)) == ceil([1], 1)   # 5 / 5 = 1
    assert DIV_ZZ_Z(ceil([-5], 1), ceil([-5], 1)) == ceil([1], 1) # -5 / -5 = 1

    # Проверка на исключение при делении на ноль
    try:
        DIV_ZZ_Z(ceil([5], 1), ceil([0], 1))  # Ожидаем ValueError
    except ValueError as e:
        assert str(e) == "Делитель не может быть нулем"

    print("Все тесты для DIV_ZZ_Z пройдены успешно!")

if __name__ == "__main__":
    test_div_zz_z()
