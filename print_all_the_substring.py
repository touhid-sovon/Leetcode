# given a string ---print all the empty substring

def printSubstring(string:str) -> list[str]:
    substring = []
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            substring.append(string[i:j])
            #print(string[i:j])

    return substring


str1 = str(input(""))
print(printSubstring(str1))

