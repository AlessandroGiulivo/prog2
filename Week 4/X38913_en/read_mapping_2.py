'''
READ-MAPPING-2(S)
    let D be an empty dictionary (of strings and integers)
    for i = 0 to i = |S| - 1 do
        D[S[i,...,|s|]] = i                  --- key = suffix, value = index
    let A be an empty array (of integers)
    i <- 0
    for key in D do
        i <- i + 1
        A[i] <- D[key]                       --- add dictionary keys to A
    for i = 1 to |A| -1 do
        for j = |A| - 1 down to i + 1        --- sorting A using
            if A[j] < A[j - 1] then          --- bubble sort
                exchange A[j] with A[j - 1]
    for suffix in A do
        return D[suffix]
'''


import sys


def read_mapping_2(s):
    D = {}
    for i in range(len(s)):
        D[s[i:len(s)]] = i + 1
    A = []
    for key in D.keys():
        A.append(key)
    for i in range(len(A)):
        for j in reversed(range(i, len(A))):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    for e in A:
        print(D[e])


read_mapping_2(sys.stdin.readline().strip())
