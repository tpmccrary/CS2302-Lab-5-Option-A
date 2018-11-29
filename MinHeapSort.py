# **********************************************************************************************************************
# NAME: Timothy P. McCrary
# CLASS: CS 2302
# LAB 5 OPTION A
# INSTRUCTOR: Diego Aguirre
# TA: Manoj Pravaka Saha
# DATE: 11/25/2018
# PURPOSE: To understand and use a min heap.
# **********************************************************************************************************************


# Based off Zybook implementation.
def percolate_down(item_index, min_heap, list_size):
    child_index = 2 * item_index + 1
    value = min_heap[item_index]

    while child_index < list_size:
        # Find the max among the item and all the item's children
        max_value = value
        max_index = -1
        i = 0
        while i < 2 and i + child_index < list_size:
            if min_heap[i + child_index] > max_value:
                max_value = min_heap[i + child_index]
                max_index = i + child_index
            i = i + 1

        if max_value == value:
            return

        # Swap heap_list[node_index] and heap_list[max_index]
        temp = min_heap[item_index]
        min_heap[item_index] = min_heap[max_index]
        min_heap[max_index] = temp

        item_index = max_index
        child_index = 2 * item_index + 1


# Based off Zybook implementation.
def heap_sort(min_heap):
    i = len(min_heap) // 2 - 1
    while i >= 0:
        percolate_down(i, min_heap, len(min_heap))
        i = i - 1

    i = len(min_heap) - 1
    while i > 0:
        # Swap min_heap[0] and min_heap[i]
        temp = min_heap[0]
        min_heap[0] = min_heap[i]
        min_heap[i] = temp

        percolate_down(0, min_heap, i)
        i = i - 1
