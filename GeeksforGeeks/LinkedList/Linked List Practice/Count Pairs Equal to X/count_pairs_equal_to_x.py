''' 
Probelm:
https://practice.geeksforgeeks.org/problems/count-pairs-whose-sum-is-equal-to-x/1/?page=1&category[]=Linked%20List&query=page1category[]Linked%20List

'''

#{ 
#Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    
        


 # } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countPair(self,h1,h2,n1,n2,x):
        '''
        h1:  head of linkedList 1
        h2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:   len of linkedList 1
        X:   given sum
        '''
        # Loop through Linked List 1
        ll1_current_node = h1
        ll2_current_node = h2
        pairs = 0
        i = 1
        j = 1
        while i<=n1:
            # Subtract loop value from x and set as remainder
            remainder = x - ll1_current_node
            if remainder > 0:
                # Loop through Linked List 2 and and count how man instances of remainder exist
                while j<=n2:
                    if ll2_current_node==remainder:
                        pairs+=1
                    ll2_current_node = ll2_current_node.next
                    j+=1
            ll1_current_node = ll1_current_node.next
            i+=1
        # Return number of pairs
        return pairs

#{ 
#Driver Code Starts.
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        
        n1=int(input())
        ll1 = LinkedList() # create a new linked list 'll1'.
        nodes_ll1 = list(map(int, input().strip().split()))
        for nodes in nodes_ll1:
            ll1.append(nodes)  # add to the end of the list
        
        n2=int(input())
        ll2=LinkedList()  #create a new linked list 'll1'.
        nodes_ll2 = list(map(int, input().strip().split()))
        for nodes in nodes_ll2:
            ll2.append(nodes)  # add to the end of the list
        
        X=int(input())
        
        
        print(Solution().countPair(ll1.head,ll2.head,n1,n2,X))


#} Driver Code Ends