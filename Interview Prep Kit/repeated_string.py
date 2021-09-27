#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    # Repeat string
    elements = len(s)
    rep = math.ceil(n/elements)
    rep_string = rep*s
    rep_string = rep_string[:n]
    # Count occurencies of a
    a_occur = rep_string.count('a')
    print (a_occur)
    return a_occur

repeatedString("aba",10)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     n = int(input().strip())

#     result = repeatedString(s, n)

#     fptr.write(str(result) + '\n')

#     fptr.close()