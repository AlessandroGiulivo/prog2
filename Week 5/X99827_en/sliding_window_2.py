'''
let A be an empty array
SLINDING-WINDOW(S, x, y)
n <- |S|
if n < x then
    do nothing
else if n = x then
    append S to A
else
    append S[0,...,x] to A
    S <- S[y,...,n]
    SLIDING-WINDOW(S, x, y) 
return A
'''


import sys

A = []
def sliding_window_2(s, x, y):
    n = len(s)
    if n < x:
        None
    elif n == x:
        A.append(s)
    else:
        A.append(s[:x])
        s = s[y:]
        sliding_window_2(s, x, y)
    return A


inp = sys.stdin.read().splitlines()
for e in sliding_window_2(inp[0], int(inp[1]), int(inp[2])):
    print(e)
