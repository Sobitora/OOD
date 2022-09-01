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

row = Queue()
cashier1 = Queue()
cashier2 = Queue()
inp,min = input("Enter people and time : ").split(" ")
for x in inp:
    row.enQueue(x)
for m in range(1,int(min)+1,1):
    print(m,end='')
    if not cashier1.isEmpty():
        if m%3 == 1 :
            cashier1.deQueue()
    if not cashier2.isEmpty():
        if m%2 == 0 :
            cashier2.deQueue()
    if not row.isEmpty():
        if cashier1.size() < 5:
            cashier1.enQueue(row.deQueue())
        else :
            cashier2.enQueue(row.deQueue())
    print(" "+str(row.item),end='')
    print(" "+str(cashier1.item),end='')
    print(" "+str(cashier2.item))