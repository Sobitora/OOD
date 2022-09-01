class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.loop = False

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s += "->"+str(cur.next.value)
            cur = cur.next
        return str(s)

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p

    def size(self):
        current = self.head
        n = 0
        while current:
            current = current.next
            n += 1
        return n

    def set_next(self,index1,index2):
        if self.isEmpty():
            return "Error! {list is empty}"
        elif self.size()-1 < int(index1):
            return "Error! {index not in length}: "+str(index1)
        elif self.size()-1 < int(index2):
            self.append(index2)
            return "index not in length, append : "+str(index2)
        curind1 = self.head
        for x in range(int(index1)):
            curind1 = curind1.next
        curind2 = self.head
        for x in range(int(index2)):
            curind2 = curind2.next
        if index1 >= index2:
            self.loop = True
        else:
            self.loop = False
            curind1.next = curind2
        return "Set node.next complete!, index:value = "+str(index1)+":"+str(curind1.value)+" -> "+str(index2)+":"+str(curind2.value)
        
    def Isloop(self,Truth):
        return self.loop

L = LinkedList()
inp = input("Enter input : ").split(",")
for x in inp:
    temp = x.split(" ")
    if temp[0] == "A":
        L.append(temp[1])
        print(L)
    if temp[0] == "S":
        data = temp[1].split(":")
        print(L.set_next(data[0],data[1]))
if L.loop:
    print("Found Loop")
else:
    print("No Loop")
    print(L)

