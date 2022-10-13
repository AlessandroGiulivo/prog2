'''
WORDS-2(n, A)
sort A
if n = 0 then
    return a list containing an empty string
else
    L = WORDS-2(n - 1, A)
    let L1 be and empty list
    for all e in L do
        for all c in A do
            concatenate e, c and append to L1
    return L1
'''


import sys


def words_2(n, A):
    A.sort()
    if n == 0:
        return [""]
    else:
        L = words_2(n - 1, A)
        L1 = []
        for e in L:
            for c in A:
                L1.append(e + c)
        return L1


inp = sys.stdin.read().splitlines()
for w in words_2(int(inp[0]), inp[1].split()):
    print(w)
