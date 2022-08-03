#Find Patterns Forming Clumps in a String 
def kmer(text, i, k):
    return text[i: (i + k)]


def kmersfrequency(text, k):
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] = D[tmp] + 1
        except KeyError:
            D[tmp] = 1
    return D


def clump_find(text, k, L, t):
    lista = []
    for i in range(0, (len(text) - L)+ 1):
        D = kmersfrequency(text[i:i + L], k)
        for i in D:
            if (D[i] == t):
                lista.append(i)
    return lista


if __name__ == "__main__":
    k=5
    L=75
    t=4
    text="CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"

    res = clump_find(text, k, L, t)
    print(set(res)) #da se ne ponavlja
