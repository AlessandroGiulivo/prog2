'''
ABUNDANCE(S)
    let D be an empty dictionary (of strings to numbers)
    for string in S do
        let c_string be an empty string
        for character in reversed(string) do
            if character == A then
                append T to c_string
            else if character == T then
                append A to c_string
            else if character == C then
                append G to c_string
            else if character == G then
                append C to c_string
        if string in keys of D then
            D[string] += 1
        else if c_string in keys of D then
            D[c_string] += 1
        else 
            if string < c_string then        --- order alphabetically
                D[string] = 1
            else 
                D[c_string] = 1
    return each key and its value of the sorted D
'''

import sys


def abundance(S):
    D = {}
    for s in S:
        cs = ''
        for c in s[::-1]:
            if c == 'A':
                cs += 'T'
            elif c == 'T':
                cs += 'A'
            elif c == 'C':
                cs += 'G'
            elif c == 'G':
                cs += 'C'
        if s in D:
            D[s] += 1
        elif cs in D:
            D[cs] += 1
        else:
            if s < cs:
                D[s] = 1
            else:
                D[cs] = 1
    for k in sorted(D):
        print(k, D[k])


abundance(sys.stdin.read().splitlines())
