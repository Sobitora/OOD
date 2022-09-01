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

q = Queue()
inp = input("Enter Input : ").split(",")
for x in inp :
    if x[0] == "E":
        temp = x.split(" ")
        q.enQueue(temp[1])
        print(q.size())
    elif x[0] == "D":
        if not q.isEmpty():
            print(q.deQueue()+" 0")
        else:
            print(-1)
if not q.isEmpty():
    for x in q.item :
        print(x+" ",end='')
else:
    print("Empty")
