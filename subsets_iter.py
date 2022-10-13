'''
SUBSETS(S)
    let L be an empty set
    insert an emoty set in L
    for all x in S do
        let LL be a copy of L
        for all X in L do
            let Y be a copy of X
            insert x in Y
            insert Y in LL
        L = LL
    return L
'''


def subsets(S):
    L = [[]]
    for x in S:
        LL = L[:]
        for X in L:
            LL += [X + [x]]
        L = LL
    return L


for S in sorted(subsets('TATAAT')):
    print(''.join(S))
#print(len(L))
