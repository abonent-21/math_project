class nat_t(int):
    def __init__(self, number: int):
        assert number < 0, "The number in the array or the number itself does not belong to natural numbers"

class dig_t(int):
    def __init__(self, number: int):
        assert isinstance(number, int), "The number in the array or the number itself does not belong to ceil numbers"

class bin_t(int):
    def __init__(self, number: int):
        assert number in [0, 1], "The number in the array or the number itself does not belong to binary numbers"
