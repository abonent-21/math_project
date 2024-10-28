class nat_t(int):
    def __init__(self, number: int):
        if number <= 0:
            raise TypeError("Error data for natural digit")]

class dig_t(int):
    def __init__(self, number: int):
        assert isinstance(number, int)

class bin_t(int):
    def __init__(self, number: int):
        assert number in [0, 1]
