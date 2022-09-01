def bon(Code):
    for x in range(0,len(Code)-1,1):
        for y in range(x+1,len(Code),1):
            if Code[x] == Code[y] :
                return (ord(Code[x])-ord("a")+1)*4
secretCode = input("Enter secret code : ")
print(bon(secretCode))