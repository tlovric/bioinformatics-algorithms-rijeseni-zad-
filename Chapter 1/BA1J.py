#Find Frequent Words with Mismatches and Reverse Complements
def hamming_distance(text1, text2):
    br = 0
    for i in range(0, len(text1)):
        if (text1[i] != text2[i]):
            br = br + 1
    return br

def reversecomplement(text):
    a=""
    for i in range(0,len(text)):
        if(text[i] == "A"):
            a=a+"T"
        if (text[i] == "T"):
            a=a+"A"
        if (text[i] == "G"):
            a=a+"C"
        if (text[i] == "C"):
            a=a+"G"

    return a[::-1]


def Frequency_with_mismatches(text, k, d1, D):
    lista = dict()
    kmers = all_kmers(k)

    for kmer in kmers:
        for i in range(len(text) - k + 1):
            if hamming_distance(text[i:i + k], kmer) <= d1:
                if kmer not in lista:
                    lista[kmer] = 1
                else:
                    lista[kmer] += 1
            if hamming_distance(text[i:i + k], reversecomplement(kmer)) <= d1:
                if kmer not in lista:
                    lista[kmer] = 1
                else:
                    lista[kmer] += 1
    return lista

from itertools import product
def all_kmers(k):
    kmers = [''.join(c) for c in product('ACGT', repeat=k)]
    return kmers


if __name__ == "__main__":
    text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    d1 = 1
    res1 = Frequency_with_mismatches(text, k, d1,all_kmers(k))
    res2=[k for k in res1.keys() if res1[k] == max(res1.values())]
    print(" ".join(res2))



