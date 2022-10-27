inp = input("Enter Input : ")
check = False
if int(inp[0]) == int(inp[-1:]):
    print("Repdrome")
elif int(inp[0]) > int(inp[-1:]):
    for i in range(len(inp)-1):
        if int(inp[i]) < int(inp[i+1]):
            print("Nondrome")
            exit(0)
        elif int(inp[i]) == int(inp[i+1]):
            check = True
    if check:
        print("Nialpdrome")
    else:
        print("Katadrome")
elif int(inp[0]) < int(inp[-1:]):
    for i in range(len(inp)-1):
        if int(inp[i]) > int(inp[i+1]):
            print("Nondrome")
            exit(0)
        elif int(inp[i]) == int(inp[i+1]):
            check = True
    if check:
        print("Plaindrome")
    else:
        print("Metadrome")