#Find a Median String 
def HammingDistance(p, q):
    """Computes the hamming distance between strings p and q"""
    if len(p) != len(q):
        return -1
    br=0
    for i in range(0,len(p)):
        if(p[i]!=q[i]):
            br=br+1
    return br

def Kmers(text,k):
  kmers=[]
  for i in range(len(text)-k+1):
    kmer=text[i:i+k]
    if (kmer not in kmers):
      kmers.append(kmer)
  return kmers

def d_text(pattern,text,k):
  min=k
  for pattern_ in Kmers(text,k):
    hd=HammingDistance(pattern,pattern_)
    if(hd<min):
      min=hd
  return min

def d_dna(pattern,dna,k):
  suma=0
  for i in range(len(dna)):
    suma+=d_text(pattern,dna[i],k)
  return suma

from itertools import product

def AllKmers(k):
  kmers=[''.join(c) for c in product('ACGT', repeat=k)]
  return kmers

def MedianString(k,dna):
  d=float('inf')
  median="a"

  for kmer in AllKmers(k):
    dna_d=d_dna(kmer,dna,k)
    if (dna_d<d):
      d=dna_d
      median=kmer
  return median

if __name__ == "__main__":
    text="AAATTGACGCAT GACGACCACGTT CGTCAGCGCCTG GCTGAGCACCGG AGTACGGGACAG"
    text = text.split()
    k = 3
    res = MedianString(text, k)
    print(res)
