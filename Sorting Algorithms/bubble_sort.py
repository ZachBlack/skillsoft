"""
Skillsoft/Percipio Python Bootcamp
Course #15 Implementing Sorting Algorithms

Bubble Sort
COMPLETED: 2/25/2022

This sort works for both num lists and string lists

Time Complexity:   O(n^2)
Space Complexity:  O(1)
"""

def bubble_sort(original_list):
    length = len(original_list)
    for i in range(length-1, 0, -1):
        for index in range(i):
            if original_list[index] > original_list[index+1]:
                original_list[index+1], original_list[index] = original_list[index], original_list[index+1]
        print('Unsorted until index: {}'.format(i-1))
        print(original_list)
