#Find All Approximate Occurrences of a Pattern in a String
def hamming_distance(p,q):
    if len(p)!= len(q):
        return -1
    br=0
    for i in range(0,len(p)):
        if(p[i]!=q[i]):
            br=br+1
    return br

def ApproximatePatternMatching(text,pattern,d):
    res=[]
    for i in range(0,len(text)-len(pattern)+1):
        if(hamming_distance(text[i:i+len(pattern)], pattern)<=d):
            res.append(i)
    return res





if __name__ == "__main__":

    text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
    pattern="ATTCTGGA"
    d=3

    res = ApproximatePatternMatching(text,pattern,d)
    print(res)
  

