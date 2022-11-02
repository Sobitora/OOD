checksubset = False

def sumsubset(count,inp,newlist,num,check):
    if count != 0:
        newlist[len(newlist)-1].append(inp[0])
        sumsubset(count-1,inp[1:],newlist,num,check)
        newlist[len(newlist)-1].pop(-1)
        if len(inp) != count:
            sumsubset(count,inp[1:],newlist,num,check)
    elif len(inp) != 0:
        newlist[len(newlist)-1].append(inp[0])
        if sum(newlist[len(newlist)-1]) == num :
            newlist.append([])
            newlist[len(newlist)-1]=list(newlist[len(newlist)-2])
            sortlist(newlist[len(newlist)-2])
            global checksubset
            checksubset = True
        if newlist[len(newlist)-1] == check:
            l = sortiteminlist(newlist[:-1])
            for i in l:
                print(i)
        newlist[len(newlist)-1].pop(-1)
        sumsubset(count,inp[1:],newlist,num,check)


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
    return l



inp = input("Enter Input : ").split("/")
num = int(inp[0])
inp = [int(i) for i in inp[1].split(" ")]
for i in range(len(inp)):
    sumsubset(i,inp,[[]],num,inp[-(i+1):])
if checksubset == False:
    print("No Subset")