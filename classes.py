class NumSet:
    def __init__(self, max):
        self.available_nums = set(range(1, max + 1))
        self.assigned_nums = []

    def assign_num(self, num):
        self.available_nums.remove(num)
        self.assigned_nums.append(num)

    def get_available_nums(self):
        return self.available_nums

    def __str__(self):
        return str(self.available_nums)
