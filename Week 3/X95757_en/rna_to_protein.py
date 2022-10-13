
'''
RNA-TO-PROTEIN(S)
    let D be an empty dictionary (of strings to characters)
    D[AAA] <- K
    ,,,
    D[UUU] <- F
    let t be an empty string
    n <- |s|
    i <- 1
    while i + 2 <= n and s[i,...,i + 2] != AUG do
        i <- i + 1
    if i + 2 <= n then
        i <- i + 3 --- skip the start codon
        while i + 2 <= n and s[i,...,i + 2] not in {UAA, UAG, UGA} do
            append D[s[i,...,i + 2]] to t
            i <- i + 3
        if i + 2 <= n then
            return t
        else
            return an empty string --- no stop codon found
    else
        return an empty string --- no start codon found
'''

import sys


def protein(s):
    D = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
         "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
         "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
         "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
         "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
         "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
         "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
         "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
         "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
         "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
         "UAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
         "UAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
         "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
         "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
         "UGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
         "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}
    t = ''
    n = len(s)
    i = 1
    while (i + 3) <= n and s[i:i + 3] != "AUG":
        i = i + 1
    if i + 3 <= n:
        i = i + 3
        while i + 3 <= n and s[i:i + 3] not in ["UAA", "UAG", "UGA"]:
            t = t + D[s[i:i + 3]]
            i = i + 3
        if i + 3 <= n:
            return t
        else:
            return ""
    else:
        return ""


print(protein(sys.stdin.readline().strip()))

'''
Run with:
python3 rna_to_protein.py < sample.inp
MVVIIPSRTV

or
python3 rna_to_protein.py < sample.inp | diff - sample.cor
'''
