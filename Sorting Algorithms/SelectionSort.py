"""
Skillsoft/Percipio Python Bootcamp
Course #15 Implementing Sorting Algorithms
Selection Sort
COMPLETED: 2/25/2022
"""
def print_list(num_list):
    print(num_list)

def selection_sort(original_list):
    """
        This works for num_lists AND string_lists
        Time Complexity:    O(N^2)
        Space Complexity:   O(1)
    """
    length = len(original_list)
    for i in xrange(length):
        min_value_index = i
        for j in xrange(i+1, length):
            if original_list[min_value_index] > original_list[j]:
                min_value_index = j
        original_list[i], original_list[min_value_index] = original_list[min_value_index], original_list[i]
        print("Sorted until index: ", i)
        print_list(original_list)
    print("Sorted list:")
    print_list(original_list)