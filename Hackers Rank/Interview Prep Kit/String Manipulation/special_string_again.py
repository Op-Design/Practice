from collections import Counter

# def substrCount(n, s):
#     special_strings = 0
#     # 1. Index through s
#     for i in range(len(s)):
#         # 2a. If i+2 < len(s)-1
#         r = i+3
#         if i+3 <= len(s)-1:
#             # 3. Create subset of [i:i+2]
#             # subset_set = [i, i+3]
#             subset = s[i:i+3]
#             # 4. If len(Counter(subset).values()) < 3
#             if len(Counter(subset).values()) < 3:
#                 # 5. Add special_strings =+ 0
#                 # print (subset)
#                 special_strings += 1
#         # 2b If i+2 > len(s)-1
#         if i+3 > len(s)-1:
#             # 2. Create subset of [i:-1]
#             # subset_set = [i, len(s)-1]
#             subset = s[i:len(s)]
#             # 4. If len(counter(subset).values()) < 2
#             if len(Counter(subset).values()) < 2 and not len(subset) == 1:
#                 # 5. Add special_strings =+ 0
#                 # print (subset)
#                 special_strings += 1
#     # Return "special_strings" + n
#     return print (special_strings + n)

def subsrCount()




s = "mnonopoo"
substrCount(len(s),s)
print ("Expected 12")
s = "asasd"
substrCount(len(s),s)
print ("Expected 7")
s = "abcbaba"
substrCount(len(s),s)
print ("Expected 10")
s = "aaaa"
substrCount(len(s),s)
print ("Expected 10")