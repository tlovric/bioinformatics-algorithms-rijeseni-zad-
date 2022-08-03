#Generate the Frequency Array of a String
from itertools import product

def allkmers(k):
    return [''.join(i) for i in product('ACGT',repeat= k)]

def Method(text,k):
    kmers=allkmers(k)
    niz=[0]*len(kmers) #ili 4^^k
    for i in range(0,len(kmers)):
        br=0
        for j in range(0,len(text)-k+1):
            if(text[j:j+k]==kmers[i]):
                br=br+1
            niz[i]=br
    a=""
    for i in range(0,len(niz)):
        a=a+str(niz[i])+" "
    return a

if __name__ == "__main__":
    text="ACGCGGCTCTGAAA"
    k = 2

    res = Method(text, k)
    print(res)
