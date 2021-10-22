def rotLeft(a, d):
    a_prime = list(range(len(a)))
    #1 cycle backwards through indexs in a
    for i in range (len(a)-1, 0, -1):
        #2a If new index is < 0
        if i-d < 0:
            a_prime[i-d+len(a)] = a[i]
        else:
            a_prime[i-d] = a[i]
    return a_prime