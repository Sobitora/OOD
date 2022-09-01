def length(txt):
    if txt == '':
        return 0
    else:
        print(f"{txt[0]}*",end="")
    if txt[1:] == '':
        return 1
    else:
        print(f"{txt[1]}~",end="")
        return 2+length(txt[2:])

print("\n",length(input("Enter Input : ")),sep="")