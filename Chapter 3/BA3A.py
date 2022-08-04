#Generate the k-mer Composition of a String
def kComposition(text,k):
    lista=[]
    for i in range(len(text)-k+1):
        lista.append(text[i:i+k])
    return sorted(lista)

if __name__ == "__main__":
    x='''5
CAATCCAAC'''
    inlines=x.split('\n')
    k=int(inlines[0])
    text=inlines[1]
    res=kComposition(text,k)
    print("\n".join(res))
