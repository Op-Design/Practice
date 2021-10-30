from collections import Counter

def countTriplets(arr, r):
    # Create dictionary of the amount times each number appears
    # arr_kv.sort()
    arr_kv = dict(sorted(Counter(arr).items(), key = lambda arr: arr[0]))
    # Find max, make sure no numbers larger than max/2r ir looped through
    loop_limit = int(max(arr_kv.keys())/(r))
    # For each number/key under this limit see if key*r and key*2r exist
    for key in arr_kv:
        if key < loop_limit:
            # If key*r and key*2r exist add 1 to triplets
            if key* == 1 and ==1    
                # If more than one instance key*r and key*2r exist, add addition instances to triplets
            
    print(arr_kv)
    print(loop_limit)