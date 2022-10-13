import sys

stop_codons = ["TGA", "TAG", "TAA"]
def genes_finding(s):
    while len(s) >= 0:
        ns = s[s.find('ATG'):]
        for j in range(0, len(ns), 3):
            if ns[j:j+3] == "TGA" or ns[j:j+3] == "TAG" or ns[j:j+3] == "TAA":
                orf = ns[:j+3]
                print(orf)
                s = ns[3:]
                break

genes_finding(sys.stdin.readline().strip())
