class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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


    def addHead(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
        else:
            p.next = self.head
            self.head = p

    def search(self, item):
        current = self.head
        while current:
            if current.value == item:
                return "Found"
            current = current.next
        return "Not Found"

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.value == item:
                return index
            current = current.next
            index += 1
        return -1

    def size(self):
        current = self.head
        n = 0
        while current:
            current = current.next
            n += 1
        return n

    def pop(self, pos):
        if self.isEmpty() or pos < 0 or pos >= self.size():
            return "Out of Range"
        current = self.head
        prev = None
        if pos == 0:
            self.head = current.next
            return "Success"
        for x in range(pos):
            prev = current
            current = current.next
        prev.next = current.next
        return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH": 
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} ".format(L.search(i[3:]), i[3:]),end="")
        print("in "+str(L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)