import string
def makeAnagram(a, b):
    #1 Create dictionaries with keys a-z
    alpha_range_a = dict.fromkeys(string.ascii_lowercase,0)
    alpha_range_b = dict.fromkeys(string.ascii_lowercase,0)
    alpha_range_ab_diff = dict.fromkeys(string.ascii_lowercase,0)
    #2 Quantify how often each letter/key appears in set a
    for i in range(len(a)):
        alpha_range_a[a[i]]+=1
    #3 Quantify how often each letter/key appears in set b
    for i in range(len(b)):
        alpha_range_b[b[i]]+=1
    #4 Compare these two sets. The difference if how many deletes are needed
    for key in alpha_range_ab_diff.keys():
        alpha_range_ab_diff[key] = abs(alpha_range_a[key] - alpha_range_b[key])
    return sum (alpha_range_ab_diff.values())