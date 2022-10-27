inp = input("Enter Input : ").split(" ")
for i in range(len(inp)-1):
    if int(inp[i]) > int(inp[i+1]):
        print("No")
        exit(0)
print("Yes")