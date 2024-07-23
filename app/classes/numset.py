class NumSet:
    def __init__(self, max):
        self.__available_nums = self.__initialize_nums(max)
        self.__assigned_nums = []

    def __str__(self):
        return str(self.__available_nums)

    def __initialize_nums(self, max):
        return set(range(1, max + 1))

    def assign_num(self, num):
        self.__available_nums.remove(num)
        self.__assigned_nums.append(num)

    def get_available_nums(self):
        return self.__available_nums
