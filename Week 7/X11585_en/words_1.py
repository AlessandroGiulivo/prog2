'''
WORDS-1(n, abc)
sort abc
let L be a list containing an empty string
s <- 0
while s < n do
    let L1 be and empty list
    for e in L do
        for c in abc do
            string <- c + e
            append string to L1
    s <- s + 1
    L <- L1
return L
'''


import sys


def words_1(n, abc):
    abc.sort()
    L = ['']
    s = 0
    while s < n:
        L1 = []
        for e in L:
            for c in abc:
                string = c + e
                L1.append(string)
        s += 1
        L = L1
    return L


inp = sys.stdin.read().splitlines()
res = words_1(int(inp[0]), inp[1].split())
for w in res:
    print(w)
