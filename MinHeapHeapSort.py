# **********************************************************************************************************************
# NAME: Timothy P. McCrary
# CLASS: CS 2302
# LAB 5 OPTION A
# INSTRUCTOR: Diego Aguirre
# TA: Manoj Pravaka Saha
# DATE: 11/25/2018
# PURPOSE: To understand and use a min heap.
# **********************************************************************************************************************


def main():
    input_list = file_to_list("Numbers.txt")
    # input_list = [4, 2, 7, 23, 9]

    print('List before converting to min heap:\n', input_list)

    min_heap = build_min_heap(input_list)
    print('After converting to min heap:\n', min_heap.heap_array)


class Heap:
    def __init__(self):
        self.heap_array = []

    def insert(self, k):
        self.heap_array.append(k)

        # TODO: Complete Implementation
        for i in range(len(self.heap_array) - 1, 0, -1):
            if k < self.heap_array[i - 1]:
                temp = self.heap_array[i - 1]
                self.heap_array[i - 1] = k
                self.heap_array[i] = temp

    def extract_min(self):
        if self.is_empty():
            return None

        min_elem = self.heap_array.pop(0)

        # TODO: Complete Implementation

        return min_elem

    def is_empty(self):
        return len(self.heap_array) == 0


def build_min_heap(input_list):
    min_heap = Heap()
    for item in input_list:
        min_heap.insert(item)

    return min_heap


def file_to_list(file_name):
    file = open(file_name)
    int_list = []
    for line in file:
        string_list = line.split(", ")
        for number in string_list:
            number = int(float(number))
            int_list.append(number)

    return int_list


if __name__ == '__main__':
    main()