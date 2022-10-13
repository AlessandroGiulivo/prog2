'''
PERMUTATIONS(S)
let L be an empty set (of strings)
    if |S| = 1 then
        append s to L
    else
        for i = 1 to |S| do
            for all t in PERMUTATIONS(S[2],..,S[|S|]) do
                append S[i], t to L
    let A be an empty list (of strings)
    for all w in L do
        append w to A
    sort A
    return A
'''


import sys


def permutations_2(s):
    l = set()
    if len(s) == 1:
        l.add(s)
    else:
        for i in range(len(s)):
            for t in permutations_2(s[:i] + s[i+1:]):
                l.add(s[i] + t)
    A = list()
    for w in l:
        A.append(w)
    A = sorted(A)
    return A


for w in permutations_2(sys.stdin.read()[:-1]):
    print(w)


    

