#Construct the De Bruijn Graph of a String
def DeBruijnGraph(text,k):
    graph=dict()
    for i in range(0,len(text)-k+1):
        a=text[i:i+k-1]
        if(a not in graph.keys()):
            graph[a]=[text[i+1:i+k]]
        else:
            graph[a].append(text[i+1:i+k]) #ako nije u stupcu prvom nadodaj ga, a ako je onda samo dodaj tu njegovu vrijednost u listu, to je else
    return graph

if __name__ == "__main__":
    x='''4
AAGATTCTCTAC'''
    inlines = x.split('\n')
    k = int(inlines[0])
    text = inlines[1]
    res = DeBruijnGraph(text,k)
    for key in sorted(res):
        ispis = ''
        for i in range(len(res[key])):
            if (i == (len(res[key]) - 1)):
                ispis += res[key][i]
            else:
                ispis += res[key][i] + ","
        print(key + " -> " + ispis)

