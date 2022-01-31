import pytest
from matching_pair import find

"""
Notes:
    - Solved but test not working
"""

find(1)
print("10")


def test__matching_pair1():
    example1_input = 1
    assert find(example1_input) == 2

def test__matching_pair2():
    example2_input = 2
    assert find(example2_input) == 3

def test__matching_pair3():
    example3_input = 3
    assert find(example3_input) == 4

def test__matching_pair4():
    example4_input = 4
    assert find(example4_input) == 5