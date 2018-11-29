# **********************************************************************************************************************
# NAME: Timothy P. McCrary
# CLASS: CS 2302
# LAB 5 OPTION A
# INSTRUCTOR: Diego Aguirre
# TA: Manoj Pravaka Saha
# DATE: 11/25/2018
# PURPOSE: To understand and use a min heap.
# **********************************************************************************************************************

import time
import MinHeap
from MinHeapSort import heap_sort


def main():
    # __________TEST 1__________________________________________________________________________________________________
    print('\n__________TEST 1__________: Uses file with 1,000 numbers.')
    # Creates list from file. This is the test we will be using.
    input_list = MinHeap.file_to_list("Numbers.txt")
    print('List before converting to min heap:\n', input_list)

    start_time = time.time()

    # Builds min heap from list then prints list.
    min_heap = MinHeap.build_min_heap(input_list)
    print('After converting to min heap:\n', min_heap.heap_array)

    # Sorts min heap using heap sort then prints list once sorted.
    heap_sort(min_heap.heap_array)
    print('After using heap sort:\n', min_heap.heap_array)

    print("\nRunning time after building min heap then sorting it = %s seconds" % (time.time() - start_time))

    # __________TEST 2__________________________________________________________________________________________________
    print('\n__________TEST 2__________: Uses empty file.')
    # Creates list from file. This is the test we will be using.
    input_list = MinHeap.file_to_list("Empty.txt")
    print('List before converting to min heap:\n', input_list)

    start_time = time.time()

    # Builds min heap from list then prints list.
    min_heap = MinHeap.build_min_heap(input_list)
    print('After converting to min heap:\n', min_heap.heap_array)

    # Sorts min heap using heap sort then prints list once sorted.
    heap_sort(min_heap.heap_array)
    print('After using heap sort:\n', min_heap.heap_array)

    print("\nRunning time after building min heap then sorting it = %s seconds" % (time.time() - start_time))

    # __________TEST 3__________________________________________________________________________________________________
    print('\n__________TEST 3__________: Uses file not formatted.')
    # Creates list from file. This is the test we will be using.
    input_list = MinHeap.file_to_list("Not Formatted.txt")
    print('List before converting to min heap:\n', input_list)

    start_time = time.time()

    # Builds min heap from list then prints list.
    min_heap = MinHeap.build_min_heap(input_list)
    print('After converting to min heap:\n', min_heap.heap_array)

    # Sorts min heap using heap sort then prints list once sorted.
    heap_sort(min_heap.heap_array)
    print('After using heap sort:\n', min_heap.heap_array)

    print("\nRunning time after building min heap then sorting it = %s seconds" % (time.time() - start_time))


if __name__ == '__main__':
    main()