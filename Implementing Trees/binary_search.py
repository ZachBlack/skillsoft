"""
Skillsoft/Percipio Python Bootcamp
Course #17 Implementing Trees

Binary Search

COMPLETED: 3/6/2022
"""

def binary_search(sorted_list, key):
    min_index = 0
    max_index = len(sorted_list)-1
    while min_index <= max_index:
        mid = (min_index + max_index)//2
        if sorted_list[mid] == key:
            return mid
        elif sorted_list[mid] < key:
            min_index = mid+1
        else:
            max_index = mid-1
    return -1    
