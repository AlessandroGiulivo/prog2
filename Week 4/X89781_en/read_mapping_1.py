'''
READ-MAPPING-1(S)
    let D be an empty dictionary (of strings and integers)
    for i = 0 to i = |S| - 1 do
        D[S[i,...,|s|]] = i
    sort D
    let A be an empty array (of integers)
    i <- 0
    for x in D do
        i <- i + 1
        A[i] <- D[x]
    return A
'''


import sys


def read_mapping_1(s):
    D = {}
    for i in range(len(s)):
        D[s[i:len(s)]] = i + 1
    SD = sorted(D)
    A = []
    for x in SD:
        A.append(D[x])
    for e in A:
        print(e)


read_mapping_1(sys.stdin.readline().strip())
