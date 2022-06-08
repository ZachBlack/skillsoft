"""
Skillsoft/Percipio Python Bootcamp
Course #15 Implementing Sorting Algorithms

Insertion Sort
COMPLETED: 2/25/2022

This sort works for both num lists and string lists

Time Complexity:   O(n^2)
Space Complexity:  O(1)
"""

def insertion_sort(original_list):
    length = len(original_list)
    for i in range(0, length-1):
        for j in range(i+1, 0, -1):
            if original_list[j] < original_list[j-1]:
                original_list[j], original_list[j-1] = original_list[j-1], original_list[j]
        print('Sorted until index: {}'.format(i))
        print(original_list)
