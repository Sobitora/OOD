inp = input("Enter Input : ").split(" ")
for i in range(len(inp)-1):
    for j in range(i+1,len(inp)):
        if int(inp[i]) < 0 or int(inp[j]) < 0:
            continue
        elif int(inp[i]) > int(inp[j]) :
            temp = inp[i]
            inp[i] = inp[j]
            inp[j] = temp
print(" ".join(inp))