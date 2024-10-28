# nat_0 = 0, 1, 2, 3, inf+
# ceil = -inf, -1, 0, 1, 2, inf+
# digit = 0 - 9

class nat_0:
    def __init__(self, array: list, n: int):
        assert n == len(array)
        assert all(0 <= i <= 9 for i in array)

        self.array = array
        self.n = n

class dig:
    def __init__(self, number: int):
        assert 0 <= number <= 9

        self.array = number

class ceil:
    def __init__(self, array: list, n: int, sign: int):
        assert n == len(array)
        assert all(0 <= i <= 9 for i in array)
        assert sign in [0, 1]
    
        self.array = array
        self.n = n
        self.sign = sign
        