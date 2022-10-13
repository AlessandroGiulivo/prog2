'''
WORD-COMPOSITION(s, k)
    n = |s|
    let D be an empty dictionary (of strings and integers)
    for i = 1 to n - k + 1 do
        w = s[i,...,i+k-1]
        if w in D then
            D[w] = D[w] + 1
        else
            D[w] = 1
    sort D
    let L be and empty list (of pairs of string and integer)
    for all w in D do
        append (w, D[w]) to L
    return L
    
// return [(w, D[w]) for w in sorted(D)]
'''

import sys


def word_composition(s, k):
    n = len(s)
    D = {}
    for i in range(n - k + 1):
        w = s[i:i + k]
        if w in D:
            D[w] += 1
        else:
            D[w] = 1
    A = sorted(D)
    L = []
    for w in A:
        L.append([w, D[w]])
    return L

inp = sys.stdin.read().splitlines()

result = word_composition(inp[0], int(inp[1]))
for e in result:
    print(e[0], e[1])
