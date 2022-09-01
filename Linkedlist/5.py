class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return ""
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s += " "+str(cur.next.value)
            cur = cur.next
        return str(s)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        n = 0
        while current:
            current = current.next
            n += 1
        return n

    def append(self,value):
        new = Node(value)
        if self.isEmpty():
            self.head = new
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = new

    def pop(self,pos):
        current = self.head
        prev = None
        if pos == 0:
            data = current.value
            self.head = current.next
            return data
        for x in range(pos):
            prev = current
            current = current.next
        data = current.value
        prev.next = current.next
        return data

    def insert(self, index, data) :
        p = Node(data)
        if int(index) == 0 :
            p.next = self.head
            self.head = p
        else :
            q = self.head
            for _ in range(int(index)-1) :
                q = q.next
            p.next = q.next
            q.next = p

    def print(self):
        if self.isEmpty():
            return ""
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s += " -> "+str(cur.next.value)
            cur = cur.next
        return str(s)

    def __getitem__(self,index):
        current = self.head
        for n in range(index):
            current = current.next
        return current.value

def get_num_digit(num):
    m = 0
    for x in num:
        m = max(m,abs(int(x)))
    return len(str(m))

def radix(l,num_digit):
    lq = Linkedlist()
    for x in l:
        lq.append(x)
    for digit in range(0,num_digit+1):
        done = True
        Lsort = Linkedlist()
        for i in range(10):
            Lsort.append(Linkedlist())
        for i in range(lq.size()):
            data = lq[i]
            num = abs(int(data)) // 10 ** (digit) % 10
            if Lsort[num].size() == 0:
                Lsort[num].append(data)
            else:
                for x in range(Lsort[num].size()):
                    if int(data) > int(Lsort[num][x]):
                        Lsort[num].insert(x,data)
                        break
                    elif x+1 == Lsort[num].size():
                        Lsort[num].append(data)
        print("------------------------------------------------------------")
        print("Round : "+str(digit+1))
        for x in range(Lsort.size()):
            print(str(x)+" : ",end="")
            print(Lsort[x])
        for x in range(Lsort.size()-1):
            if Lsort[x+1].size() != 0:
                done = False
        lq = Linkedlist()
        while Lsort.size() != 0:
            if Lsort[Lsort.size()-1].size() == 0:
                Lsort.pop(Lsort.size()-1)
            else:
                lq.append(Lsort[Lsort.size()-1].pop(0))
        if done:
                print("------------------------------------------------------------")
                print(str(digit)+" Time(s)")
                break
    return lq

L = Linkedlist()
inp = input("Enter Input : ").split(" ")
num_digit = get_num_digit(inp)
for x in inp:
    L.append(x)
Lafter = radix(inp,num_digit)
print("Before Radix Sort : {0}".format(L.print()))
print("After  Radix Sort : {0}".format(Lafter.print()))
