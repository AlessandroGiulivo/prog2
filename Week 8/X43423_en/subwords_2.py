'''
SUBWORDS-2(S)
S1, S2 = SUBWORDS-2(s, 1)
sort S2
return S2

SUBWORDS-2(S, i)
if i > |s| then 
    return {}, {}
else
    S1, S2 = SUBWORDS-2(s, i + 1)
    insert an empty string in S1
    let SS1 be an empty set (of strings)
    for all w in S1 do
        insert s[i] + w in SS1
        insert s[i] + w in S2
    return SS1, S2
'''


import sys


def subwords_2(s):
    s1, s2 = subwords(s, 0)
    s2 = sorted(s2)
    return s2
def subwords(s, i):
    if i >= len(s):
        return set(), set()
    else:
        s1, s2 = subwords(s, i + 1)
        s1.add("")
        ss1 = set()
        for w in s1:
            ss1.add(s[i] + w)
            s2.add(s[i] + w)
        return ss1, s2



for w in subwords_2(sys.stdin.read()[:-1]):
    print(w)
