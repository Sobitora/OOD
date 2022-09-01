print("*** Fun with countdown ***")
number = input("Enter List : ").split(" ")
list = []
listsum = []
countlist = 0
for x in range(len(number)-1) :
        # list.append(number[x])
        if int(number[x])-int(number[x+1]) == 1 or int(number[x]) == 1:
                list.append(int(number[x]))
                if int(number[x]) == 1:
                        listsum.append(list)
                        list=[]
                        countlist += 1

if int(number[len(number)-1]) == 1:
        list.append(int(number[len(number)-1]))
        listsum.append(list)
        countlist += 1
listAll = []
listAll.append(countlist)
listAll.append(listsum)
print(listAll)

