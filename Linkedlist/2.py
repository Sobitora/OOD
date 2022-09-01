class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "linked list : "
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s += "->"+str(cur.next.value)
            cur = cur.next
        return "linked list : "+str(s)

    def str_reverse(self):
        if self.isEmpty():
            return "reverse : "
        cur= self.head
        while cur.next:
            cur = cur.next
        s = str(cur.value)
        while cur.prev:
            s += "->"+str(cur.prev.value)
            cur = cur.prev
        return "reverse : "+str(s)

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
            p.prev = t

    def add_before(self,data):
        new = Node(data)
        if self.isEmpty():
            self.head = new
        else:
            current = self.head
            current.prev = new
            new.next = current
            self.head = new

    def insert(self,index,data):
        if index < 0 or index > self.size():
            return "Data cannot be added"
        new = Node(data)
        current = self.head
        if self.isEmpty():
            self.head = new
        elif index == 0:
            current.prev = new
            new.next = current
            self.head = new
        elif index == self.size():
            while current.next:
                current = current.next
            new.prev = current
            current.next = new
        else:
            for x in range(index):
                current = current.next
            new.next = current
            new.prev = current.prev
            current.prev.next = new
            current.prev  = new
        return "index = "+str(index)+" and data = "+str(data)

    def remove(self,data):
        if self.isEmpty():
            return "Not Found!"
        current = self.head
        index = 0
        while current:
            if current.value == data:
                if self.head.value == data:
                    if self.size() == 1:
                        self.head = None
                    else:
                        self.head = current.next
                        self.head.prev = None
                elif current.prev != None and current.next == None:
                    current.prev.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return "removed : "+str(data)+" from index : "+str(index)
            current = current.next
            index += 1
        return "Not Found!"

    def size(self):
        if self.head == None:
            return 0
        current = self.head
        n = 0
        while current:
            current = current.next
            n += 1
        return n

L = LinkedList()
inp = input("Enter Input : ").split(",")
for x in inp:
    temp = x.strip().split(" ")
    temp[0].replace(""," ")
    if temp[0] == "I":
        ind,data = temp[1].split(":")
        print(L.insert(int(ind),data))
    elif temp[0] == "Ab":
        L.add_before(temp[1])
    elif temp[0] == "A":
        L.append(temp[1])
    elif temp[0] == "R":
        print(L.remove(temp[1]))
    print(L)
    print(L.str_reverse())