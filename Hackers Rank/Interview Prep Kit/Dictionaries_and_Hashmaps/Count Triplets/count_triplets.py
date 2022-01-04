import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # Create dictionary of the amount times each number appears
    # arr_kv.sort()
    triplets = 0
    arr_kv = dict(sorted(Counter(arr).items(), key = lambda arr: arr[0]))
    # Find max, make sure no numbers larger than max/2r ir looped through
    loop_limit = int(max(arr_kv.keys())/(r))
    # For each number/key under this limit see if key*r and key*2r exist
    print(loop_limit)
    for key in arr_kv:
        if key < loop_limit:
            # If key*r and key*2r exist add 1 to triplets
            if arr_kv[key*r] >= 1 and arr_kv[key*r**2]>=1:
                # If more than one instance key*r and key*2r exist, add addition instances to triplets
                print (max(arr_kv[key], arr_kv[key*r], arr_kv[key*r**2]))
                triplets += max(arr_kv[key], arr_kv[key*r], arr_kv[key*r**2])
                
            
    print(arr_kv)
    print (triplets)
    return triplets


# 4/13 Test cases passed


# def countTriplets(arr, r):
#     # Create dictionary of the amount times each number appears
#     # arr_kv.sort()
#     triplets = 0
#     arr_kv = dict(sorted(Counter(arr).items(), key = lambda arr: arr[0]))
#     # Find max, make sure no numbers larger than max/2r ir looped through
#     loop_limit = int(max(arr_kv.keys())/(r))
#     # For each number/key under this limit see if key*r and key*2r exist
#     print(loop_limit)
#     for key in arr_kv:
#         if key < loop_limit:
#             # If key*r and key*2r exist add 1 to triplets
#             try:
#                 if arr_kv[key*r] >= 1 and arr_kv[key*r**2]>=1:
#                     # If more than one instance key*r and key*2r exist, add addition instances to triplets
#                     print (max(arr_kv[key], arr_kv[key*r], arr_kv[key*r**2]))
#                     triplets += max(arr_kv[key], arr_kv[key*r], arr_kv[key*r**2])
#             except:
#                 pass
                    
            
#     print(arr_kv)
#     print (triplets)
#     return triplets

# This gets 8/13 but is not my real solution