# nat_0 = 0, 1, 2, 3, inf+
# ceil = -inf, -1, 0, 1, 2, inf+
# digit = 0 - 9

class nat_0:
    def __init__(self, array: list, n: int):
        assert n == len(array)
        assert all(0 <= i <= 9 for i in array)

        self.array = array
        self.n = n
    
    def __eq__(self, other):
        # Проверяем, что другой объект - это тоже nat_0 и имеет те же значения атрибутов
        if isinstance(other, nat_0):
            return self.array == other.array and self.n == other.n
        return False

    def __repr__(self):
        return f"nat_0({self.array}, {self.n})"



class dig:
    def __init__(self, number: int):
        assert 0 <= number <= 9

        self.array = number
    
    def __eq__(self, other):
        # Проверяем, что другой объект - это тоже dig и имеет то же значение
        if isinstance(other, dig):
            return self.value == other.value
        return False

    def __repr__(self):
        # Удобное представление для вывода информации об объекте
        return f"dig({self.value})"

class ceil:
    def __init__(self, array: list, n: int, sign: int):
        assert n == len(array)
        assert all(0 <= i <= 9 for i in array)
        assert sign in [0, 1]
    
        self.array = array
        self.n = n
        self.sign = sign

    def __eq__(self, other):
        # Проверяем, что другой объект - это тоже ceil и имеет те же значения атрибутов
        if isinstance(other, ceil):
            return self.array == other.array and self.n == other.n and self.sign == other.sign
        return False

    def __repr__(self):
        # Удобное представление для вывода информации об объекте
        return f"ceil({self.array}, {self.n}, {self.sign})"