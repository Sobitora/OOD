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

class Department(Queue):
    
    def __init__(self):
        super().__init__()
        self.id = 0

q = []
id,runq = input("Enter Input : ").split("/")
id = id.split(',')
runq = runq.split(',')
for x in runq:
    if x[0] == "E" :
        temp = x.split(" ")
        if len(q) == 0:
            q.append(Department())
            q[0].id = int(temp[1][0])
            q[0].enQueue(temp[1])
        else:
            check = False
            for x in range(len(q)):
                if int(temp[1][0]) == q[x].id:
                    q[x].enQueue(temp[1])
                    check = True
            if not check:
                    q.append(Department())
                    q[len(q)-1].id = int(temp[1][0])
                    q[len(q)-1].enQueue(temp[1])
    else:
            if len(q) != 0:
                print(q[0].deQueue())
                if q[0].isEmpty():
                    q.pop(0)
            else:
                print("Empty")