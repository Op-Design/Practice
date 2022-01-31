"""
Practice Problem: https://practice.geeksforgeeks.org/problems/matching-pair5320/1/?page=1&query=page1
"""

class Solution:
    def find (self, N):
        numbers_picked_for_matching_pair = N+1
        return numbers_picked_for_matching_pair

#{ 
#  Driver Code Starts

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.find(N))
# } Driver Code Ends