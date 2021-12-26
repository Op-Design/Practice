# Practice Problem: https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/1
# Supporting Tutorial: https://www.geeksforgeeks.org/sort-elements-by-frequency/

# Given an array of integers, sort the array according to frequency of elements.
# That is elements that have higher frequency come first.
# If frequencies of two elements are same, then smaller number comes first.

# Input:  arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
# Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}

# Input: arr[] = {2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8}
# Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999}


# My approach:
# 1. Sort array (This allows for array to be order before sorting by frequency)
# 2. Create a dictionary of each element in the array
# 3. Make the dictionary value equal to the amount of times it appears in the array
# 4. Create new array sorted according to frequemcy of elements - highest fruency elemtns come first.
#        If frequencies of two elements are same, then smaller number comes first.


def sort_elements_by_frequency(array):
    # 1. Sort array (This allows for array to be order before sorting by frequency)
    array.sort()
    elements_and_frequency = {}

    for i in array:
        if i not in elements_and_frequency:
            # 2. Create a dictionary of each element in the array
            elements_and_frequency[i] = 1
        elif i in elements_and_frequency:
            # 3. Make the dictionary value equal to the amount of times it appears in the array
            elements_and_frequency[i] += 1
    print (elements_and_frequency.items())

    # 4. Create new array sorted according to frequemcy of elements - highest fruency elemtns come first.
    #    If frequencies of two elements are same, then smaller number comes first.
    sorted_keys_elements_and_frequency = sorted(elements_and_frequency.items(), key = lambda x:x[1], reverse=True)
    print(sorted_keys_elements_and_frequency)
    sorted_elements_and_frequency = []
    for i in sorted_keys_elements_and_frequency:
        for j in range(i[1]):
            sorted_elements_and_frequency.append(i[0])

    print(sorted_elements_and_frequency)
    return sorted_elements_and_frequency


    # 1. Sort array (This allows for array to be order before sorting by frequency)
    array.sort()
    elements_and_frequency = {}

    for i in array:
        if i not in elements_and_frequency:
            # 2. Create a dictionary of each element in the array
            elements_and_frequency[i] = 1
        elif i in elements_and_frequency:
            # 3. Make the dictionary value equal to the amount of times it appears in the array
            elements_and_frequency[i] += 1

    # 4. Create new array sorted according to frequemcy of elements - highest fruency elemtns come first.
    #    If frequencies of two elements are same, then smaller number comes first.
    sorted_keys_elements_and_frequency = sorted(elements_and_frequency.items(), key = lambda x:x[1], reverse=True)
    sorted_elements_and_frequency = []
    for i in sorted_keys_elements_and_frequency:
        for j in range(i[1]):
            sorted_elements_and_frequency.append(i[0])

    return sorted_elements_and_frequency

# Example 1
# example1_array = [5, 5, 4, 6, 4]
# sort_elements_by_frequency(example1_array)
# Ans: 4 4 5 5 6

# Example 2
# example2_array = [9, 9, 9, 2, 5]
# sort_elements_by_frequency(example2_array)
# Ans: 9 9 9 2 5

# Example 3
# example3_array = [2, 5, 2, 8, 5, 6, 8, 8]
# sort_elements_by_frequency(example3_array)
# Ans: 8, 8, 8, 2, 2, 5, 5, 6

# Example 4
# example4_array = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
# sort_elements_by_frequency(example4_array)
# Ans: 8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999

# Example 5
example5_array = [8, 9, 1, 2, 3, 1]
sort_elements_by_frequency(example5_array)
# Ans: 1, 1, 2, 3, 8, 9


# test_dict = [8, 8, 8, 12]
# sort_elements_by_frequency(test_dict)

