import time


def minimumSwaps (arr):
    # print(arr)
    min_swaps = 0
    for i in range(len(arr)):
        if not i+1 == arr[i]:
            pos = arr.index(i+1, i)
            arr[i] , arr[pos] = arr[pos] , arr[i]
            min_swaps+=1
    # print (arr)
    return min_swaps

# start_time = time.time()
# arr = [7, 1, 3, 2, 4, 5, 6]
# print(minimumSwaps (arr))
# print ("Should be - 5")
# print("--- %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# arr = [4, 3, 1, 2]
# print(minimumSwaps (arr))
# print ("Should be - 3")
# print("--- %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# arr = [2, 3, 4, 1, 5]
# print(minimumSwaps (arr))
# print ("Should be - 3")
# print("--- %s seconds ---" % (time.time() - start_time))

# start_time = time.time()
# arr = [1, 3, 5, 2, 4, 6, 7]
# print(minimumSwaps (arr))
# print ("Should be - 3")
# print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
arr = []
arr = list (open ("minimum_swap_2_testcase.txt"))
arr = arr[0].split()
arr = list(map(int,arr))
# arr_sort = arr.copy()
# arr_sort.sort()
# print (arr_sort[-5:])
# print (arr [0:40])
print(minimumSwaps (arr))
print ("Should be - 3")
print("--- %s seconds ---" % (time.time() - start_time))
