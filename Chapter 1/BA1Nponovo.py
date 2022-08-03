#Generate the d-Neighborhood of a String
from itertools import product

def hamming_distance(p, q):
    br = 0
    for i in range(0, len(p)):
        if (p[i] != q[i]):
            br = br + 1
    return br

def allkmers(k):
    return [''.join(i) for i in product('ACGT',repeat= k)]

def Neighbours(text,k):
    kmers=allkmers(len(text))
    lista=[]
    for kmer in kmers:
        if(hamming_distance(kmer,text)<=k):
            if(kmer not in lista):
                lista.append(kmer)
    for i in range(0,len(lista)):
        print (lista[i])
        
if __name__ == "__main__":
    text="ACG"
    k=1
    Neighbours(text,k)
