# Intervalles

class Range:
    def __init__(self, minimum, maximum):
        self.__min = 0
        self.__max = 0
        self.__init_range(minimum, maximum)

    def get_min(self):
        return self.__min
    def get_max(self):
        return self.__max

    def set_min(self, minimum):
        self.__min = minimum
    def set_max(self, maximum):
        self.__max = maximum

    def __init_range(self, minimum, maximum):
        if minimum == maximum:
            raise Exception( "Error: min and max are equal")

        min_max_list = [minimum, maximum]
        min_max_list.sort()
        self.set_min(min_max_list[0])
        self.set_max(min_max_list[1])

    def print_range(self):
        return f"[{self.get_min()};{self.get_max()}]"

    def get_range_elements_list(self):
        res = []
        for number in range(self.get_min(), self.get_max() + 1):
            res.append(number)
        return res

    def update_range(self, new_min, new_max):
        if new_min == new_max:
            raise Exception( "Error: min and max are equal")
        elif new_min > new_max:
            raise Exception( "Error: new min is greater than new max")

        self.set_min(new_min)
        self.set_max(new_max)
        self.__init_range(new_min, new_max)
        return "Range updated successfully"

    def __add__(self, other):
        new_min = self.get_min() + other.get_min()
        new_max = self.get_max() + other.get_max()
        return Range(new_min, new_max)

    def intersection(self, other):
        res = []
        other_range_elements = other.get_range_elements_list()
        for number in range(self.get_min(), self.get_max() + 1):
            if number in other_range_elements:
                res.append(number)
        if len(res) == 0:
            return None
        return res

    def union(self, other):
        if not self.intersection(other):
            return "Creating union is impossible."

        all_range_elements = self.get_range_elements_list() + other.get_range_elements_list()
        union_set = set(all_range_elements)
        return union_set

range1 = Range(5, 9)
range2 = Range(7, 15)
print("Range 1: ", range1.print_range()) # [5;9]
print("Range 1 elements: ", range1.get_range_elements_list()) # [5, 6, 7, 8, 9]
print("Range 2: ", range2.print_range()) # [7;15]
print("Range 2 elements: ", range2.get_range_elements_list()) # [7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Range 1 + range 2: ", range1.__add__(range2).print_range()) # [12;24]
print("Range 1 ∩ range 2: ",  range1.intersection(range2)) # [7, 8, 9]
print("Range 1 ⋃ range 2: ", range1.union(range2)) # {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

