#Reconstruct a String from its Genome Path
def GenomePath(text):
    a=text[0]
    for pattern in text[1:]:
        a=a+pattern[-1]
    return a
if __name__ == "__main__":
    x='''ACCGA
CCGAA
CGAAG
GAAGC
AAGCT'''
    inlines=x.split('\n')
    res=GenomePath(inlines)
    print(res)
