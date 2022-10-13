'''
SLINDING-WINDOW(S, x, y)
let A be an empty array
n <- |S|
i <- 0
while i <= n-x do
    append S[i,...,i+x] to A
    i <- i + y
return A
'''


import sys


def sliding_window(s, x, y):
    A = []
    n = len(s)
    i = 0
    while i <= n - x:
        A.append(s[i:i + x])
        i += y
    return A


inp = sys.stdin.read().splitlines()
for e in sliding_window(inp[0], int(inp[1]), int(inp[2])):
    print(e)
