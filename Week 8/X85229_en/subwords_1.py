'''
SUBWORDS-1(S)
let T be an empty set (of strings)
for i = 1 to |S| do                      --- for (int i = 0; i < s.length(); i++)
    for j = i to |S| do                  --- for (int j = i; i < s.length(); i++)
        insert s[i,...,j] in S           --- s[i:j+1]                              ---s.substr(i, j - i + 1)
let L be an empty list (of strings)
for all w in S do
    append w to L
sort L
return L
'''


import sys


def subwords_1(s):
    T = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            T.add(s[i:j+1])
    L = list()
    for w in T:
        L.append(w)
    L = sorted(L)
    return L


for w in subwords_1(sys.stdin.read()[:-1]):
    print(w)

