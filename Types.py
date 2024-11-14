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

    def __str__(self):
        return ''.join(str(i) for i in self.array)

    def copy(self):
        return nat_0(self.array.copy(), self.n)


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

    def __str__(self):
        return f"{self.value}"

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

    def __str__(self):
        return f"{['', '-'][self.sign]}{''.join([str(i) for i in self.array])}"

    def copy(self):
        return ceil(self.array.copy(), self.n, self.sign)


class rat(object):
    def __init__(self, num: ceil, den: nat_0):
        assert den.array != [0], "Знаменатель не может быть равен 0"
        self.num = num
        self.den = den

    def __eq__(self, other):
        if isinstance(other, rat):
            return self.num == other.num and self.den == other.den
        return False

    def __repr__(self):
        return f"rat({self.num}, {self.den})"

    def __str__(self):
        return f"{str(self.num)}/{str(self.den)}"

    def copy(self):
        return rat(self.num.copy(), self.den.copy())


class pol(object):
    def __init__(self, coefficients: list, m: int):
        if coefficients != [] or m != 0:
            assert m == len(coefficients) - 1, "Степень многочлена должна быть на 1 меньше длины массива коэффициентов"
            assert all(isinstance(coef, rat) for coef in coefficients), "Все элементы должны быть экземплярами класса rat"
        self.coefficients = coefficients
        self.m = m  # Явное указание степени многочлена

    def __eq__(self, other):
        if isinstance(other, pol):
            return self.coefficients == other.coefficients and self.m == other.m
        return False

    def __repr__(self):
        return f"pol({self.coefficients}, {self.m})"

    def __str__(self):
        result = ''
        pow = 0
        for i in self.coefficients[:-1]:
            if pow == 0:
                result += str(i.num) + ' + '
            elif i.den == nat_0([1], 1):
                result += str(i.num) + f' x^{pow} + '
            else:
                result += str(i) + f' x^{pow} + '
            pow += 1
        result += str(self.coefficients[-1]) + f' x^{pow}'
        return result

    def copy(self):
        return pol(self.coefficients.copy(), self.m)
