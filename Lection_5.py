def cntpairwithdiffgtk(sortednums, k):
    cntpairs = 0
    b = 0
    for a in range(len(sortednums)):
        while b < len(sortednums) and sortednums[b] - sortednums[a] <= k:
            b += 1
        cntpairs += len(sortednums) - b
    return cntpairs


l = [1, 2, 5, 7, 8, 10]
k = 4
print(cntpairwithdiffgtk(l, k))