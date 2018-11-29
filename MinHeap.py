# **********************************************************************************************************************
# NAME: Timothy P. McCrary
# CLASS: CS 2302
# LAB 5 OPTION A
# INSTRUCTOR: Diego Aguirre
# TA: Manoj Pravaka Saha
# DATE: 11/25/2018
# PURPOSE: To understand and use a min heap.
# **********************************************************************************************************************


# Class for min heap.
class Heap:
    def __init__(self):
        self.heap_array = []

    # Based off Zybook implementation modified for a min heap.
    def percolate_up(self, item_index):
        while item_index > 0:
            # compute the parent node's index
            parent_index = (item_index - 1) // 2

            # check for a violation of the max heap property
            if self.heap_array[item_index] >= self.heap_array[parent_index]:
                # no violation, so percolate up is done.
                return
            else:
                # swap heap_array[node_index] and heap_array[parent_index]
                temp = self.heap_array[item_index]
                self.heap_array[item_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp

                # continue the loop from the parent node
                item_index = parent_index

    # Inserts item into min heap and sorts it.
    def insert(self, k):
        # Item placed at end of min heap list.
        self.heap_array.append(k)

        # This is where the item is sorted in the heap.
        self.percolate_up(len(self.heap_array) - 1)

    # Extracts first item from min heap.
    def extract_min(self):
        if self.is_empty():
            return None

        min_elem = self.heap_array.pop(0)

        return min_elem

    # Returns TRUE if min heap is empty.
    def is_empty(self):
        return len(self.heap_array) == 0


# Function that creates a min heap from a list.
def build_min_heap(input_list):
    min_heap = Heap()
    for item in input_list:
        min_heap.insert(item)

    return min_heap


# Function that stores data from a file into a list. File contents must be separated by commas.
def file_to_list(file_name):
    file = open(file_name)
    int_list = []
    empty_list = []

    for line in file:
        string_list = line.split(", ")
        for number in string_list:
            try:
                number = int(float(number))
                int_list.append(number)
            except ValueError:
                print('ERROR: File not formatted correctly.')
                return empty_list

    return int_list
