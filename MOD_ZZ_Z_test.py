# test_MOD_ZZ_Z.py
from Types import ceil
from MOD_ZZ_Z import MOD_ZZ_Z

def test_mod_zz_z():
    # Тестирование функции MOD_ZZ_Z

    # Тесты на положительных числах
    assert MOD_ZZ_Z(ceil([5], 1), ceil([2], 1)) == ceil([1], 1)  # 5 % 2 = 1
    assert MOD_ZZ_Z(ceil([10], 1), ceil([3], 1)) == ceil([1], 1) # 10 % 3 = 1
    assert MOD_ZZ_Z(ceil([9], 1), ceil([4], 1)) == ceil([1], 1)  # 9 % 4 = 1

    # Тесты на нулевом делимом
    assert MOD_ZZ_Z(ceil([0], 1), ceil([5], 1)) == ceil([0], 1)  # 0 % 5 = 0
    assert MOD_ZZ_Z(ceil([0], 1), ceil([-5], 1)) == ceil([0], 1) # 0 % -5 = 0

    # Тесты на отрицательных числах
    assert MOD_ZZ_Z(ceil([-5], 1), ceil([2], 1)) == ceil([1], 1)  # -5 % 2 = 1
    assert MOD_ZZ_Z(ceil([5], 1), ceil([-2], 1)) == ceil([1], 1)  # 5 % -2 = -1

    # Проверка на исключение при делении на ноль
    try:
        MOD_ZZ_Z(ceil([5], 1), ceil([0], 1))  # Ожидаем ValueError
    except ValueError as e:
        assert str(e) == "Делитель не может быть нулем"

    print("Все тесты для MOD_ZZ_Z пройдены успешно!")

if __name__ == "__main__":
    test_mod_zz_z()
