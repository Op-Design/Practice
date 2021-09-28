#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Jump two unless next number will be a thundercloud. If so jump one. (remember you can always win)
    current_cloud = 0
    minimum_jumps = 0
    while current_cloud < len(c)-1:
        if current_cloud+2<len(c)-1 and c[current_cloud+2] == 1:
            minimum_jumps+=1
            current_cloud+=1
        else:
            minimum_jumps+=1
            current_cloud+=2
    return minimum_jumps

    # Write your code here


c = [0,0,1,0,0,1,0]
jumpingOnClouds(c)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     c = list(map(int, input().rstrip().split()))

#     result = jumpingOnClouds(c)

#     fptr.write(str(result) + '\n')

#     fptr.close()
