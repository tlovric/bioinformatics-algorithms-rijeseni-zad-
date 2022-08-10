#Find the Most Frequent Words with Mismatches in a String
def hamming_distance(p,q):
    if len(p)!=len(q):
        return -1
    br = 0
    for i in range(0, len(p)):
        if (p[i] != q[i]):
            br = br + 1
    return br


from itertools import product
def all_kmers(k):
    kmers = [''.join(c) for c in product('ACGT', repeat=k)]

    return kmers

def ListofFrequentwordswithmismatches(text, k, d1, D):
   lista = dict()
    kmers = all_kmers(k)

    for kmer in kmers:
        for i in range(len(text) - k + 1):
            if hamming_distance(text[i:i + k], kmer) <= d1:
                if kmer not in lista:
                    lista[kmer] = 1
                else:
                    lista[kmer] += 1
    return lista

if __name__ == "__main__":
    text = input("Unesi text: ")
    k = int(input("Unesi k: "))
    d1 = int(input("Unesi d1: "))
    res = ListofFrequentwordswithmismatches(text, k, d1, all_kmers(k))
    #Ispis najcescih kmer-a
    print(" ".join([k for k in res.keys() if res[k] == max(res.values())]))
