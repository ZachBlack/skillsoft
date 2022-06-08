"""
Skillsoft/Percipio Python Bootcamp
Course #15 Implementing Sorting Algorithms

Quick Sort
COMPLETED: 2/25/2022

This sort works for both num lists and string lists

Time Complexity:   O(nlog(n))
Space Complexity:  O(log(n)) -> worst case: O(N)
This sort is not stable and is not adaptive
"""

def partition(original_list, start_index, end_index):
    curr_index = start_index
    pivot = original_list[end_index]
    for i in range(start_index, end_index):
        if original_list[i] <= pivot:
            original_list[curr_index], original_list[i] = original_list[i], original_list[curr_index]
            curr_index+=1
    original_list[curr_index], original_list[end_index] = original_list[end_index], original_list[curr_index]

    return curr_index
    
def quick_sort(original_list, start_index, end_index):
    if start_index >= end_index:
        return
    
    part = partition(original_index, start_index, end_index)
    print('Element in the right place: {}'.format(original_list[part]))
    print(original_list)
    
    quick_sort(original_list, start_index, part-1)
    quick_sort(original_list, part+1, end_index)
