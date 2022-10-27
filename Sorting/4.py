inp = input("Enter Input : ").split(" ")
strinput = []
for i in inp:
    for j in i:
        if j.isalpha():
            strinput.append(j)
            break
for i in range(len(strinput)-1):
    for j in range(i+1,len(strinput)):
        if strinput[i] > strinput[j] :
            tempint,tempstr = inp[i],strinput[i]
            inp[i],strinput[i] = inp[j],strinput[j]
            inp[j],strinput[j] = tempint,tempstr
print(" ".join(inp))
