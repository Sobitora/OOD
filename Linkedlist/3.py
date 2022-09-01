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
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

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

    def size(self):
        current = self.head
        n = 0
        while current:
            current = current.next
            n += 1
        return n

L1 = LinkedList()
L2 = LinkedList()
Mesh = LinkedList()
line1,line2 = input("Enter Input (L1,L2) : ").split(" ")
line1 = line1.split("->")
line2 = line2.split("->")
for x in line1:
    L1.append(x)
print("L1    : "+str(L1))
for x in line2:
    L2.append(x)
print("L2    : "+str(L2))
cur = L1.head
for x in range(L1.size()):
    Mesh.append(cur.value)
    cur = cur.next
cur = L2.head
while cur.next:
    cur = cur.next
while cur.prev:
    Mesh.append(cur.value)
    cur = cur.prev
Mesh.append(cur.value)
print("Merge : "+str(Mesh))