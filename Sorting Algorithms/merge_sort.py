"""
Skillsoft/Percipio Python Bootcamp
Course #15 Implementing Sorting Algorithms

Merge Sort
COMPLETED: 2/25/2022

This sort works for both num lists and string lists

Time Complexity:   O(nlog(n))
Space Complexity:  O(n)
This sort is stable, but is not adaptive
"""

def merge_sort(original_list):
    if len(original_list) <= 1:
        return
    
    mid = len(original_list)//2
    lefthalf = original_list[:mid]
    righthalf = original_list[mid:]
    
    merge_sort(lefthalf)
    print(lefthalf)
    
    merge_sort(righthalf)
    print(righthalf)
    
    i, j, k = 0, 0, 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            original_list[k] = lefthalf[i]
            i += 1
        else:
            original_list[k] = righthalf[j]
            j += 1
        k += 1
    
    while i < len(lefthalf):
        original_list[k] = lefthalf[i]
        i += 1
        k += 1
    while j < len(righthalf):
        original_list[k] = righthalf[j]
        j += 1
        k += 1
