#Find a Position in a Genome Minimizing the Skew
def Minimize(text):
    lista=[0]
    for i in range(0,len(text)):
        if(text[i]=="G"):
            lista.append(lista[-1]+1)
        elif(text[i]=="C"):
            lista.append(lista[-1]-1)
        else:
            lista.append(lista[-1])
    minimum=min(lista)
    for i in range(0,len(lista)):
        if (lista[i]==minimum):
            print (i)


if __name__ == '__main__':
    text = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"
    res = Minimize(text)
   


