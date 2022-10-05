from dataclasses import dataclass
from operator import ne


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) :
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur,s = self.head , str(self.head.data)
        while cur.next:
            s += str(cur.next.data)
            cur = cur.next
        return s

    def str_reverse(self):
        if self.isEmpty():
            return "Empty"
        cur,s = self.tail , str(self.tail.data)
        while self.tail.prev:
            s += str(self.tail.prev.data)
            cur = cur.prev
        return s

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        if self.isEmpty():
            return 0
        cur = self.head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        return n

    def append(self,data):
        new = Node(data)
        if self.isEmpty():
            self.addHead(data)
        else:
            t = self.head
            while t.next:
                t = t.next
            new.prev = t
            t.next = new
            self.tail = new

    def addHead(self,data):
        new = Node(data)
        if self.isEmpty():
            self.head = new
            self.tail = new
        else:
            cur = self.head
            cur.prev = new
            new.next = cur
            self.head = new

    def insert(self,index,data):
        new = Node(data)
        if self.isEmpty() or index == 0:
            self.addHead(data)
        else:
            cur = self.head
            for x in range(index-1):
                cur = cur.next
            new.prev = cur
            new.next = cur.next
            cur.next.prev = new
            cur.next = new

    def remove(self,data):
        cur = self.head
        if cur.data == data:
            if self.size == 1:
                self.head = None
            else:
                cur.next.prev = None
                self.head = cur.next
        else:
            while cur:
                if cur.data == data:
                    if cur.next == None:
                        self.tail = cur.prev
                        cur.prev.next = None
                    else:
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev
                    break
                cur = cur.next

    def size(self):
        cur = self.head
        n = 0
        while cur:
            cur = cur.next
            n += 1
        return n