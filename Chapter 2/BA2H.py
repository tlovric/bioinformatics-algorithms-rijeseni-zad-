#Implement DistanceBetweenPatternAndStrings
import math
def hamming_distance(p, q):
    if len(p) != len(q):
        return -1
    br = 0
    for i in range(0, len(p)):
        if (p[i] != q[i]):
            br = br + 1
    return br


def Distance(Pattern, Dna):
    k = len(Pattern)
    distance = 0

    for Text in Dna:
        hd = math.inf
        for i in range(0, len(Text) - k):
            kmer = Text[i:i + k]
            if hd > hamming_distance(Pattern, kmer):
                hd = hamming_distance(Pattern, kmer)
        distance += hd
    return distance

if __name__ == "__main__":
    x= '''AAA
TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT'''
    pattern = x.splitlines()[0]
    niz_dna = x.splitlines()[1].split(" ")
    print(Distance(pattern, niz_dna))