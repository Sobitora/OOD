print("*** Fun with Drawing ***")
number = input("Enter input : ")
number = int(number)
for i in range(1,number+1,1):
    for j in range(number-i,0,-1):
        print(".",end="")
    for j in range((2*i)-1):
        if j == 0 or j == (2*i)-2:
            print("*",end="")
        else:
            print("+",end="")
    for j in range(((number-i)*2)-1,0,-1):
        print(".",end="")
    for j in range((2*i)-1):
        if j == 0 or j == (2*i)-2 :
            if i != number :
                print("*",end="")
            elif j != 0 :
                print("*",end="")
        else:
            print("+",end="")
    for j in range(number-i,0,-1):
        print(".",end="")
    print("")
for i in range(1,(number*2)-1,1):
    for j in range(i):
        print(".",end="")
    for j in range(((((number*2)-1)-i)*2)-1,0,-1):
        if j == ((((number*2)-1)-i)*2)-1 or j == 1:
            print("*",end="")
        else:
            print("+",end="")
    for j in range(i):
        print(".",end="")
    print("")