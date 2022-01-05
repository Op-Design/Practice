''' 
Probelm:
https://practice.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1

'''

# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
    current_node = head
    if k==1:
        if current_node.next:
            newhead = current_node.next
        else:
            newhead = null
        return newhead
            
    elif k==2:
        head.next = head.next.next
        newhead = head
        return newhead
            
    else:
        cycles = 1
        newhead = head
        while cycles < k:
            previous_node = current_node
            current_node = current_node.next
            next_node = current_node.next
            cycles += 1
        previous_node.next = next_node
        return newhead
        
    
        
    

#{ 
#  Driver Code Starts
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def printlist(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        k = int(input())
        newhead = delNode(list1.head, k)
        printlist(newhead)
# Contributed By: Harshit Sidhwa
# } Driver Code Ends