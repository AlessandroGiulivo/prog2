'''
if all s[i] in s
if t is a permutation of s[1],...,s[i-1], s[i+1],...,s[n]
then s[i],t is a permutation of s

PERMUTATIONS(S)
let L be an empty list (of strings)
    if |S| = 1 then
        append s to L
    else
        for i = 1 to |S| do
            for all t in PERMUTATIONS(S[2],..,S[|S|]) do
                append S[i], t to L
    return L
'''


def permutations(s):
    L = []
    if len(s) == 1:
        L += [s]
    else:
        for i in range(len(s)):
            for t in permutations(s[:i] + s[i+1:]):
                L += [s[i] + t]
    return L


for t in permutations('ABC'):
    print(t)
