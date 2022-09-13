def TowerOfHanoi(n , A, C, B ,tow):
    if n==1:
        print ("move 1 from  "+A+" to "+C)
        print("|  |  |")
        changeTOH(int(n),A,C,tow)
        showTOH(tow,0,len(tow[0]))
    else:
        TowerOfHanoi(n-1, A, B, C ,tow)
        print ("move "+str(n)+" from  "+A+" to "+C)
        print("|  |  |")
        changeTOH(int(n),A,C,tow)
        showTOH(tow,0,len(tow[0]))
        TowerOfHanoi(n-1, B, C, A ,tow)

def changeTOH(num,move,to,tow):
    if move == 'A':
        tow[0].pop(tow[0].index(num))
        tow[0].insert(0,0)
    elif move == 'B':
        tow[1].pop(tow[1].index(num))
        tow[1].insert(0,0)
    else:
        tow[2].pop(tow[2].index(num))
        tow[2].insert(0,0)
    if to == 'A':
        tow[0].pop(0)
        tow[0].append(num)
    elif to == 'B':
        tow[1].pop(0)
        tow[1].append(num)
    else:
        tow[2].pop(0)
        tow[2].append(num)
    tow[0].sort()
    tow[1].sort()
    tow[2].sort()
    

def showTOH(tow,n,k):
    A = tow[0][n]
    B = tow[1][n]
    C = tow[2][n]
    if A == 0 :
        A = '|'
    if B == 0:
        B = '|'
    if C == 0:
        C = '|'
    print(f'{A}  {B}  {C}')
    if n == k-1:
        return
    showTOH(tow,n+1,k)

def numtow(n,str,tow:list,k):
    if n != k+1:
        if str == "A":
            tow.append(n)
        else:
            tow.append(0)
    else:
        return
    numtow(n+1,str,tow,k)



n = input("Enter Input : ")
A = []
B = []
C = []
numtow(1,"A",A,int(n))
numtow(1,"B",B,int(n))
numtow(1,"C",C,int(n))
tow = [A,B,C]
print("|  |  |")
showTOH(tow,0,len(tow[0]))
TowerOfHanoi(int(n),'A','C','B',tow)
