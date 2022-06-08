"""
Skillsoft/Percipio Python Bootcamp
Course #15 Implementing Sorting Algorithms

Shell Sort
COMPLETED: 2/25/2022

This sort works for both num lists and string lists

Time Complexity:  ~O(n^(3/2))
Space Complexity:  O(1)
"""

# Think of this as a more efficient use of insertion sort
def shell_sort(original_list):
    length = len(original_list)
    gap = length//2
    while gap > 0:
        for i in range(gap, length):
            temp = original_list[i]
            j=i
            while j >= gap and original_list[j-gap] > temp:
                original_list[j] = original_list[j-gap]
                j-=gap
            original_list[j]=temp
            print('Gap: {}'.format(gap))
            print(original_list)
        gap = gap//2
