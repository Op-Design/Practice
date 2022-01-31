import pytest
from matching_pair import Solution

def __test__matching_pair1():
    example1_input = 1
    assert Solution(example1_input) == 2

def __test__matching_pair2():
    example2_input = 2
    assert Solution(example2_input) == 3

def __test__matching_pair3():
    example3_input = 3
    assert Solution(example3_input) == 4

def __test__matching_pair4():
    example4_input = 4
    assert Solution(example4_input) == 5