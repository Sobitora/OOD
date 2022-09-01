list = input("Enter Your List : ").split(" ")
listsum = []
listAll = []
i = 0
if len(list) >= 3: 
    while i < len(list)-2:
        for j in range(i+1,len(list)-1,1):
            for k in range(j+1,len(list),1):
                if int(list[i])+int(list[j])+int(list[k]) == 0 :
                    listsum.append(int(list[i]))
                    listsum.append(int(list[j]))
                    listsum.append(int(list[k]))
                    if len(listAll) != 0:
                        for x in range(len(listAll)):
                            if listsum != listAll[x]:
                                listAll.append(listsum)
                    else:
                        listAll.append(listsum)
                    listsum = []
                    break
        i += 1
    print(listAll)
else:
    print("Array Input Length Must More Than 2")
# print(listsum)