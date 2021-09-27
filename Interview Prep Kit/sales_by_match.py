#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # 1. Identify all possible colors
    colors = {}
    for n in ar:
        if not n in colors:
            # pass
            colors [n] = None
    # 2. Quantify instances
    for key in colors.keys():
        colors[key] = ar.count(key)
    # 3. Quantify pairs
    colors_pairs = colors.copy()
    for key in colors_pairs.keys():
        colors_pairs[key] = colors_pairs[key]//2
    quantity = sum(colors_pairs.values())
    # 4. Return Quantity
    return quantity
    
    
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()


ar2 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
sockMerchant(len(ar2), ar2)