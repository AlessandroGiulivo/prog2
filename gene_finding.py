#This program will take a DNA string as input, and return the first ORF within the string

#PSEUDOCODE

#GENE_FINDING(s)
#    stop_codons <- ["TGA", "TAG", "TAA"]
#    s <- s[s.find('ATG'):]
#    for stop_codon in stop_codons do
#        for i in range|s, 3| do
#            if s[i:i+3] = stop_codon then
#                orf <- s[:i+3]
#    return orf

import sys

stop_codons = ["TGA", "TAG", "TAA"]
def gene_finding(s):
    s = s[s.find('ATG'):]
    for stop in stop_codons:
        for j in range(0, len(s), 3):
            if s[j:j+3] == stop:
                s = s[:j+3]
    return s

print(gene_finding(sys.stdin.readline().strip()))
