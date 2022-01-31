import pytest
from sort_elements_by_frequency import sort_elements_by_frequency


# class TestClass:
# Try this out later.
# Notes:
    # Example #4 is failing


def test_sort_elements_by_frequency1():
    example1_array = [5, 5, 4, 6, 4]
    assert sort_elements_by_frequency(example1_array) == [4, 4, 5, 5, 6]
    # Example 1
    # example1_array = [5, 5, 4, 6, 4]
    # Ans: 4 4 5 5 6

def test_sort_elements_by_frequency2():
    example2_array = [9, 9, 9, 2, 5]
    assert sort_elements_by_frequency(example2_array) == [9, 9, 9, 2, 5]
    # Example 2
    # example2_array = [9, 9, 9, 2, 5]
    # Ans: 9 9 9 2 5

def test_sort_elements_by_frequency3():
    example3_array = [2, 5, 2, 8, 5, 6, 8, 8]
    assert sort_elements_by_frequency(example3_array) == [8, 8, 8, 2, 2, 5, 5, 6]
    # Example 3
    # example3_array = [2, 5, 2, 8, 5, 6, 8, 8]
    # Ans: 8, 8, 8, 2, 2, 5, 5, 6

def test_sort_elements_by_frequency4():
    example4_array = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    assert sort_elements_by_frequency(example4_array) == [8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999]
    # Example 4
    # example4_array = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    # Ans: 8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999

def test_sort_elements_by_frequency5():
    example5_array = [8, 9, 1, 2, 3, 1]
    assert sort_elements_by_frequency(example5_array) == [1, 1, 2, 3, 8, 9]
    # Example 5
    # example5_array = [8, 9, 1, 2, 3, 1]
    # Ans: 1, 1, 2, 3, 8, 9