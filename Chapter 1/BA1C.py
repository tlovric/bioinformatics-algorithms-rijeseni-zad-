#Find the Reverse Complement of a String
def reversecomplement(text):
    a=""
    for i in range(0,len(text)):
        if(text[i] == "A"):
            a=a+"T"
        if (text[i] == "T"):
            a=a+"A"
        if (text[i] == "G"):
            a=a+"C"
        if (text[i] == "C"):
            a=a+"G"
    return a[::-1]


if __name__ == "__main__":
    text = "AAAACCCGGT"
    res = reversecomplement(text)
    print(res)
