'''
This program will take a DNA string as input, and return the first ORF within the string

PSEUDOCODE

GENE_FINDING(s)
    Let stop codons be a list of strings
    Let orf be and empty string
    stop_codons <- ["TGA", "TAG", "TAA"]
    s <- s[s.find('ATG'):]
    for stop_codon in stop_codons do
        for i = 0 to i = |s| every 3 numbers do
            if s[i:i+3] = stop_codon then
                orf <- s[:i+3]
    return orf
'''

import sys


stop_codons = ["TGA", "TAG", "TAA"]
def gene_finding(s):
    orf = ""
    s = s[s.find('ATG'):]
    for stop in stop_codons:
        for i in range(0, len(s), 3):
            if s[i:i+3] == stop:
                orf = s[:i+3]
    return orf


print(gene_finding(sys.stdin.readline().strip()))
