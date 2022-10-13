'''
WORDS-2(n, abc)
sort abc
if n = 0 then
    return a list containing an empty string
else
    L = WORDS-2(n - 1, abc)
    let L1 be and empty list
    for e in L do
        for c in abc do
            string <- c + e
            append string to L1
    return L1
'''


import sys


def words_2(n, abc):
    abc.sort()
    if n == 0:
        return [""]
    else:
        L = words_2(n-1, abc)
        L1 = []
        for e in L:
            for c in abc:
                string = c + e
                L1.append(string)
        return L1

L = ['']
inp = sys.stdin.read().splitlines()
res = words_2(int(inp[0]), inp[1].split())
for w in res:
    print(w)
