checksubset = False

def sumsubset(count,inp,newlist,num,sumlist:list,check):
    if count != 0:
        newlist.append(inp[0])
        sumsubset(count-1,inp[1:],newlist,num,sumlist,check)
        newlist.pop(-1)
        if len(inp) != count:
            sumsubset(count,inp[1:],newlist,num,sumlist,check)
    elif len(inp) != 0:
        newlist.append(inp[0])
        if sum(newlist) == num :
            sumlist.append([])
            sumlist[len(sumlist)-1]=list(newlist)
            sortlist(sumlist[len(sumlist)-1])
            sortiteminlist(sumlist)
            global checksubset
            checksubset = True
        if newlist == check:
            for i in sumlist:
                print(i)
        newlist.pop(-1)
        sumsubset(count,inp[1:],newlist,num,sumlist,check)


def sortlist(l):
    for i in range(len(l)-1):
                for j in range(i+1,len(l)):
                    if int(l[i]) > int(l[j]) :
                        temp = l[i]
                        l[i] = l[j]
                        l[j] = temp

def sortiteminlist(l):
    for i in range(len(l)-1):
                for j in range(i+1,len(l)):
                    if int(l[i][0]) > int(l[j][0]) :
                        temp = l[i]
                        l[i] = l[j]
                        l[j] = temp
                    elif int(l[i][0]) == int(l[j][0]):
                        for k in range(len(l)):
                            if int(l[i][k]) > int(l[j][k]) :
                                temp = l[i]
                                l[i] = l[j]
                                l[j] = temp
                                break
                            elif int(l[i][k]) < int(l[j][k]):
                                break



inp = input("Enter Input : ").split("/")
num = int(inp[0])
inp = [int(i) for i in inp[1].split(" ")]
sumlist = []
for i in range(len(inp)):
    sumsubset(i,inp,[],num,[],inp[-(i+1):])
if checksubset == False:
    print("No Subset")


