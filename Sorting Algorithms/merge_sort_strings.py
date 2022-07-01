"""

Merge Sort algorithm from skillsoft adapted to sort strings

Time Complexity:   O(nlog(n))
Space Complexity:  O(n)
This sort is stable, but is not adaptive
"""

def merge_sort(word):
    if len(word) <= 1:
        return word

    mid = len(word)//2
    lefthalf = word[:mid]
    righthalf = word[mid:]

    sorted_left = merge_sort(lefthalf)
    sorted_right = merge_sort(righthalf)

    i,j = 0,0
    sorted_string = []
    while (i < len(sorted_left)) and (j < len(sorted_right)):
        if sorted_left[i] < sorted_right[j]:
            sorted_string.append(sorted_left[i])
            i+=1
        else:
            sorted_string.append(sorted_right[j])
            j+=1

    while (i < len(sorted_left)):
        sorted_string.append(sorted_left[i])
        i+=1

    while (j < len(sorted_right)):
        sorted_string.append(sorted_right[j])
        j+=1

    return "".join(sorted_string)
