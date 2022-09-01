class Stack :

    def __init__(self) :
        self.value = []
    
    def push(self,value) :
        self.value.append(value)

    def pop(self) :
        return self.value.pop(-1)
    
    def size(self) :
        return len(self.value)

    def isEmpty(self) :
        return len(self.value) == 0

    def __str__(self) :
        return "".join(self.value)

class Queue:

    def __init__(self) :
        self.item = []

    def enQueue(self,value) :
        self.item.append(value)

    def deQueue(self) :
        return self.item.pop(0)

    def isEmpty(self) :
        return len(self.item) == 0

    def size(self) :
        return len(self.item)

    def __str__(self) :
        return "".join(self.item)


def checkbomb(s,bomb,item,str):
    bomb1 = s.pop()
    bomb2 = s.pop()
    countbomb = 0
    if bomb == bomb1 and bomb1 == bomb2:
        countbomb += 1
        if str == "M":
            item.enQueue(bomb)
        else:
            if not item.isEmpty():
                temp = item.deQueue()
                if temp == bomb1 and temp == bomb:
                    s.push(bomb2)
                else:
                    s.push(bomb2)
                    s.push(bomb1)
                    s.push(temp)
                    s.push(bomb)
                    countbomb -= 1
    else:
        s.push(bomb2)
        s.push(bomb1)
        s.push(bomb)
    return countbomb


Smirror= Stack()
Qmirror = Queue()
Snormal = Stack()
Qnormal = Queue()
inp = input("Enter Input (Normal, Mirror) : ").split(" ")
mirrorbomb = 0
normalbomb = 0
fail = 0
item = Queue()
for x in inp[1][::-1]:
    if Smirror.size() < 2:
        Smirror.push(x)
    else:
        mirrorbomb += checkbomb(Smirror,x,item,"M")
for x in inp[0]:
    if Snormal.size() < 2:
        Snormal.push(x)
    else:
        temp = normalbomb
        useitem = item.size()
        normalbomb += checkbomb(Snormal,x,item,"N")
        if temp != normalbomb and useitem != 0:
            fail += 1
            normalbomb -= 1

print("NORMAL :")
print(Snormal.size())
if Snormal.isEmpty():
    print("Empty")
else:
    for x in range(Snormal.size()):
        Qnormal.enQueue(Snormal.pop())
    print(Qnormal)
print(str(normalbomb)+" Explosive(s) ! ! ! (NORMAL)")
if fail != 0:
    print("Failed Interrupted "+str(fail)+" Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(Smirror.size())
if Smirror.isEmpty():
    print("ytpmE")
else:
    for x in range(Smirror.size()):
        Qmirror.enQueue(Smirror.pop())
    print(Qmirror)
print("(RORRIM) ! ! ! (s)evisolpxE "+str(mirrorbomb))
# print(item)
