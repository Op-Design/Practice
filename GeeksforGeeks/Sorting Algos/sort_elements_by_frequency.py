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
# 1. Create a dictionary of each element in the array
# 2. Make the dictionary value equal to the amount of times it appears in the array
# 3. Create new array sorted according to frequemcy of elements - highest fruency elemtns come first.
#        If frequencies of two elements are same, then smaller number comes first.


def sort_elements_by_frequency(array):
    elements_and_frequency = {}
    for i in array:
        if i not in elements_and_frequency:
            # 1. Create a dictionary of each element in the array
            elements_and_frequency[i] = 1
            pass
        elif i in elements_and_frequency:
            # 2. Make the dictionary value equal to the amount of times it appears in the array
            elements_and_frequency[i] += 1
            pass
    print (elements_and_frequency)

    # 3. Create new array sorted according to frequemcy of elements - highest fruency elemtns come first.
    #    If frequencies of two elements are same, then smaller number comes first.
    sorted_keys_elements_and_frequency = sorted(elements_and_frequency)
    print(sorted_keys_elements_and_frequency)
    sorted_elements_and_frequency = []
    for i in sorted_keys_elements_and_frequency:
        for j in range(elements_and_frequency[i]):
            sorted_elements_and_frequency.append(i)
            pass

    print(sorted_elements_and_frequency)


# Example 1
example1_array = [5, 5, 4, 6, 4]
sort_elements_by_frequency(example1_array)
# Ans: 4 4 5 5 6

# Example 2
example2_array = [9, 9, 9, 2, 5]
sort_elements_by_frequency(example2_array)
# Ans: 9 9 9 2 5


# test_dict = [8, 8, 8, 12]
# sort_elements_by_frequency(test_dict)

