from Types import ceil
from MOD_ZZ_Z import MOD_ZZ_Z

def test_mod_zz_z():
    # Тестирование функции MOD_ZZ_Z

    # Тесты на положительных числах
    assert MOD_ZZ_Z(ceil([5], 1, 0), ceil([2], 1, 0)) == ceil([1], 1, 0)  # 5 % 2 = 1
    assert MOD_ZZ_Z(ceil([1, 0], 2, 0), ceil([3], 1, 0)) == ceil([1], 1, 0) # 10 % 3 = 1
    assert MOD_ZZ_Z(ceil([9], 1, 0), ceil([4], 1, 0)) == ceil([1], 1, 0)  # 9 % 4 = 1

    # Тесты деления 0
    assert MOD_ZZ_Z(ceil([0], 1, 0), ceil([5], 1, 0)) == ceil([0], 1, 0)  # 0 % 5 = 0
    assert MOD_ZZ_Z(ceil([0], 1, 0), ceil([5], 1, 1)) == ceil([0], 1, 0) # 0 % -5 = 0
    
    # Тесты на отрицательных числах
    assert MOD_ZZ_Z(ceil([5], 1, 1), ceil([2], 1, 0)) == ceil([1], 1, 0)  # -5 % 2 = 1
    assert MOD_ZZ_Z(ceil([1, 0, 0], 3, 1), ceil([3, 5], 2, 0)) == ceil([5], 1, 0)  # -100 % 35 = 5

    # Проверка на исключение при делении на ноль
    try:
        MOD_ZZ_Z(ceil([5], 1, 0), ceil([0], 1, 0))  # Ожидаем ValueError
    except ValueError as e:
        assert str(e) == "Делитель не может быть нулем"

    print("Все тесты для MOD_ZZ_Z пройдены успешно!")

if __name__ == "__main__":
    test_mod_zz_z()
