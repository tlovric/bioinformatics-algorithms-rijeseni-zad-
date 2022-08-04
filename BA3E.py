#Construct the De Bruijn Graph of a Collection of k-mers
def DeBrujinGraphKmers(text):
    graph=dict()
    for pattern in text:
        a=pattern[:-1]
        if(a not in graph.keys()):
            graph[a]=[pattern[1:]]
        else:
            graph[a].append(pattern[1:])
    return graph

if __name__ == "__main__":
    x='''GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG'''
    inlines = x.split('\n')
    res = DeBrujinGraphKmers(inlines)
    for key in sorted(res):
        ispis = ''
        for i in range(len(res[key])):
            if (i == (len(res[key]) - 1)):
                ispis += res[key][i]
            else:
                ispis += res[key][i] + ","
        print(key + " -> " + ispis)

