class nat_0(object):
    def __init__(self, array: list, n: int):
        assert n == len(array), "Длина списка должна быть равна n"
        assert all(0 <= i <= 9 for i in array), "Все элементы должны быть цифрами от 0 до 9"
        self.array = array
        self.n = n
    
    def __eq__(self, other):
        if isinstance(other, nat_0):
            return self.array == other.array and self.n == other.n
        return False

    def __repr__(self):
        return f"nat_0({self.array}, {self.n})"
    
    def copy(self):
        return nat_0(self.array, self.n)


class dig(object):
    def __init__(self, number: int):
        assert 0 <= number <= 9, "Число должно быть цифрой от 0 до 9"
        self.value = number  # Исправлено на `self.value`
    
    def __eq__(self, other):
        if isinstance(other, dig):
            return self.value == other.value
        return False

    def __repr__(self):
        return f"dig({self.value})"  # Исправлено на `self.value`
    
    def copy(self):
        return dig(self.value)


class ceil(object):
    def __init__(self, array: list, n: int, sign: int):
        assert n == len(array), "Длина списка должна быть равна n"
        assert all(0 <= i <= 9 for i in array), "Все элементы должны быть цифрами от 0 до 9"
        assert sign in [0, 1], "Знак должен быть либо 0, либо 1"
        self.array = array
        self.n = n
        self.sign = sign

    def __eq__(self, other):
        if isinstance(other, ceil):
            return self.array == other.array and self.n == other.n and self.sign == other.sign
        return False

    def __repr__(self):
        return f"ceil({self.array}, {self.n}, {self.sign})"
    
    def copy(self):
        return ceil(self.array, self.n, self.sign)
