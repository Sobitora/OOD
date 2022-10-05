from dataclasses import dataclass


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
            self.head = new
        else:
            t = self.head
            while t.next:
                t = t.next
            new.prev = t
            t.next = new

    def 