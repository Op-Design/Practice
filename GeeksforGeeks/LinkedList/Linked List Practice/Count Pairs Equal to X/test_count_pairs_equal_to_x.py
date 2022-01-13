import linked_list_creation as llc
from count_pairs_equal_to_x import Solution

# 1
# 6
# 1 2 3 4 5 6
# 3
# 11 12 13
# 15

array1 = [1, 2, 3, 4, 5, 6]
array2 = [11, 12, 13]
# print (len(array1))

LinkedList1 = llc.LinkedList()
for value in array1:
    LinkedList1.append(value)

LinkedList2 = llc.LinkedList()
for value in array2:
    LinkedList2.append(value)

pairs = Solution().countPair(LinkedList1.head,LinkedList2.head,len(array1),len(array2),15)
print(pairs)




# 1
# 6
# 1 2 3 4 5 6
# 3
# 11 12 13
# 15

array1 = [7, 5, 1, 3]
array2 = [3, 5, 2, 8]
# print (len(array1))

LinkedList1 = llc.LinkedList()
for value in array1:
    LinkedList1.append(value)

LinkedList2 = llc.LinkedList()
for value in array2:
    LinkedList2.append(value)

pairs = Solution().countPair(LinkedList1.head,LinkedList2.head,len(array1),len(array2),10)
print(pairs)