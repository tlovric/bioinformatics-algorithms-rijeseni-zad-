#Construct the Overlap Graph of a Collection of k-mers
def prefix(pattern):
    return pattern[:-1]
def sufix(pattern):
    return pattern[1:]
def overlapGraph(text):
    graph=dict() #{}
    for row in text:
        for row1 in text:
            if(sufix(row)==prefix(row1)):
                if(row not in graph.keys()):
                    graph[row]=[row1]
                else:
                    graph[row].append(row1)
    return graph

if __name__ == "__main__":
    x='''ATGCG
GCATG
CATGC
AGGCA
GGCAT'''
    inlines=x.split('\n')
    res=overlapGraph(inlines)
    for key in sorted(res):
        for value in res[key]:
            print(key+" -> "+value)
