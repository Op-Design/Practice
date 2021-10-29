# Solution
# Got stuck on my solution

# from collections import Counter

# def isValid(s):
#     d = Counter(Counter(s).values())
#     if len(d)==1:
#         return "YES"
#     if len(d)>2:
#         return "NO"
#     if 1 in d.values() and (d[min(d.keys())]==1 or (max(d.keys()) - min(d.keys())==1)):
#         return "YES"
#     else:
#         return "NO"

# s = "aaabbbcccd"

# print (isValid(s))