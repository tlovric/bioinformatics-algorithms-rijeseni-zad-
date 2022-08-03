#Implement MotifEnumeration
from itertools import product
def hamming_distance(p, q):
    """Computes the hamming distance between strings p and q"""
    if len(p) != len(q):
        return -1
    br = 0
    for i in range(0, len(p)):
        if (p[i] != q[i]):
            br = br + 1
    return br


def allkmers(k):
    return [''.join(i) for i in product('ACGT', repeat=k)]


def Neighbours(pattern, d):
    rez = {""}
    if (d == 0):
        return {pattern}
    kmers = allkmers(len(pattern))
    rez = {k for k in kmers if hamming_distance(k, pattern) <= d}
    return rez


def Mismatch(x, text, d, k):
    for a in text:
        br = 0
        for i in range(0, len(a) - k + 1):
            if (hamming_distance(a[i:i + k], x) <= d):
                br = 1

        if (br == 0):
            return False
    return True #mora zadovoljit sve a da bi bia true


def MotifEnumeration(text, k, d):
    rez = set()
    L = set()
    text = text.split(" ")
    for a in text:
        for i in range(0, len(a) - k):
            pattern = a[i:i + k]
            neighbor_pattern = Neighbours(pattern, d)
            L = L.union(neighbor_pattern)
    for x in L:
        if (Mismatch(x, text, d, k) == True):
            rez.add(x)

    return rez

if __name__ == "__main__":
    text = "ATTTGGC TGCCTTA CGGTATC GAAAATT"
    k =3
    d = 1

    res = MotifEnumeration(text, k, d)
    print(" ".join(res))

