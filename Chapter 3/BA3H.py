#Reconstruct a String from its k-mer Composition
def StringReconstruction(patterns, k):
    suffix = []
    prefix = []
    D = dict()
    for kmer in patterns:
        suffix.append(kmer[1:])
        prefix.append(kmer[:-1])
        D[kmer[:-1]] = kmer[k - 1:k]

    # pocetni kmer
    for p in prefix:
        if p not in suffix:
            start = p
            break

    pocetak_teksta = start + D[start]

    # zavrsni kmer
    for s in suffix:
        if s not in prefix:
            end = s
            break

    text = pocetak_teksta
    while True:
        ostatak_teksta = text[len(text) - k + 1:len(text)]
        if ostatak_teksta == end:
            break
        else:
            text += D[ostatak_teksta]
    return text

if __name__ == "__main__":
    x= '''4
CTTA
ACCA
TACC
GGCT
GCTT
TTAC'''
    inlines =x.split("\n")
    k = int(inlines[0])
    patterns = [line.strip() for line in inlines[1:]]
    print(StringReconstruction(patterns, k))