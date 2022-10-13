'''
WORD-COMPOSITION(S, K)
let D be an empty dictionary (of strings and integers)
n <- |S|
i <- 1
while i <= n - K do
    if S[i,...,i + K] is not in D then
        D[S[i,...,i + K]] <- 0
        i <- i + 1
    else
        D[S[i,...,i + K]] <- D[S[i,...,i + K]] + 1
        i <- i + 1
let A be a list of keys of D
sort A
let R be an empy dictionary (of strings and integers)
for element in A do
    R[element] <- D[element]
return R
'''


import sys


def word_composition(s, k):
    D = {}
    n = len(s)
    i = 0
    while i <= n - k:
        if s[i:i + k] in D:
            D[s[i:i + k]] += 1
            i += 1
        else:
            D[s[i:i + k]] = 1
            i += 1
    A = sorted(D)
    R = {}
    for e in A:
        R[e] = D[e]
    return R


inp = sys.stdin.read().splitlines()

result = word_composition(inp[0], int(inp[1]))
for key in result:
    print(key, result[key])
