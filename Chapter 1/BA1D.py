#Find All Occurrences of a Pattern in a String 
def patternposition(text, pattern):
    a = ""
    for i in range(0, len(text) - len(pattern)+1):
        if (text[i:(len(pattern) + i)] == pattern):
            print(text[i])
            print("usa")
            a = a + str(i) + " "
            print (a)
            print(str(i))
    return a


if __name__ == "__main__":
   text="GATATATGCATATACTT"
   pattern="ATAT"
   res = patternposition(text, pattern)
   print(res)
