'''
PERMUTATIONS(S)
    let S be an empty stack (of characters)
    for i = 1 to |S| do
        push s[i] onto S
    let L be an empty set (of strings)
    insert an empty string in L
    while S is not empty do
        pop from S the top element x
        let L' be an empty set (of strings)
        for all w in L do
            for i = 1 to |w| + 1 do
                insert w[1,...,i - 1] + x + w[i,...,|w|] in L'
        L = L'
    sort L
    return L
'''


import sys


def permutations(s):
    t = list()
    for i in range(len(s)):
        t.append(s[i])
    l = set()
    l.add("")
    while len(t) > 0:
        x = t.pop()
        l1 = set()
        for w in l:
            for i in range(len(w) + 2):
                l1.add(w[:i] + x + w[i:])
        l = l1
    A = list()
    for w in l:
        A.append(w)
    A = sorted(A)
    return A


for w in permutations(sys.stdin.read()[:-1]):
    print(w)


    

