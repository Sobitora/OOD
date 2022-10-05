class Node:
    def __init__(self,data) :
        self.data  = data
        self.next = None

class LinkedList:
    def __init__(self) :
        self.head = None
        self.tail = None

    def size(self):
        cur = self.head
        n = 0
        while cur:
            cur = cur.next
            n += 1
        return n

    def append(self,data):
        new = Node(data)
        if self.isEmpty():
            self.head = new
            self.tail = new
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = new
            self.tail = new

    def addHead(self,data):
        new = Node(data)
        if self.isEmpty():
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new

    def search(self,data):
        cur = self.head
        n = 0
        while cur:
            if cur.data == data:
                return n
            n += 1
            cur = cur.next
    
    def insert(self,index,data):
        cur = self.head
        new = Node(data)
        for x in range(index-1):
            cur = cur.next
        new.next = cur.next
        cur.next = new


    def isEmpty(self):
        return self.head == None

    def __str__(self) : 
        if self.isEmpty():
            return "Enpty"
        cur,s = self.head , str(self.head.data) + " "
        while cur.next:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

