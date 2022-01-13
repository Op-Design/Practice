import linked_list_creation as llc

# 1
# 6
# 1 2 3 4 5 6
# 3
# 11 12 13
# 15

array1 = [1, 2, 3, 4, 5, 6]
array2 = [11, 12, 13]
# print (array)

LinkedList1 = llc.LinkedList()

for value in array1:
    LinkedList1.append(value)

LinkedList1.printlist(LinkedList1.head)