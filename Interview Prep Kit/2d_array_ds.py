#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    rows = len(arr)
    columns = len(arr [0])
    arr_list=[]
    # convert matrix into vector
    for i in range(rows):
        for j in range (columns):
            arr_list.append(arr[i][j])
    # cycle through ever center of the hour glass
    hourglass_sums = []
    for i in range(7,len(arr_list)-7):
        # cycle through each hour glass using the mathematical equation relating the center of an hour glass to other element in hour glass
        top_lef = arr_list[i-7]
        top_mid = arr_list[i-6]
        top_rig = arr_list[i-5]
        center = arr_list[i]
        bottom_lef = arr_list[i+5]
        bottom_mid = arr_list[i+6]
        bottom_rig = arr_list[i+7]
        top_sum = top_lef+top_mid+top_rig
        bottom_sum = bottom_lef+bottom_mid+bottom_rig
        hourglass_sum = top_sum+bottom_sum+center
        # Store sum
        hourglass_sums.append(hourglass_sum)
    # return hour glass with largest value
    print (max(hourglass_sums))
    return (max(hourglass_sums))

    

arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]
arr = [
    [3, 7, -3, 0, 1, 8],
    [1, -4, -7, -8, -6, 5],
    [-8, 1, 3, 3, 5, 7],
    [-2, 4, 3, 1, 2, 7],
    [2, 4, -5, 1, 8, 4],
    [5, -7, 6, 5, 2, 8],
]
hourglassSum(arr)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr = []

#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = hourglassSum(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()