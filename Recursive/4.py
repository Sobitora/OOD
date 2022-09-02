def TowerOfHanoi(n , A, C, B):
    if n==1:
        print ("move 1 from  "+A+" to "+C)
    else:
        TowerOfHanoi(n-1, A, B, C)
        print ("move "+str(n)+" from  "+A+" to "+C)
        TowerOfHanoi(n-1, B, C, A)

def showTOH():
    print("|  |  |")
# Driver code
n = input("Enter Input : ")
TowerOfHanoi(int(n),'A','C','B')