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
    d = dict()
    for i in D:
        br = 0
        for j in range(0, len(text) - k+1):
            if (hamming_distance(i, text[j:j + k]) <= d1):
                br = br + 1
        d[i] = br
    return d

if __name__ == "__main__":
    text = input("Unesi text: ")
    k = int(input("Unesi k: "))
    d1 = int(input("Unesi d1: "))
    res = ListofFrequentwordswithmismatches(text, k, d1, all_kmers(k))
    #Ispis najcescih kmer-a
    print(" ".join([k for k in res.keys() if res[k] == max(res.values())]))
