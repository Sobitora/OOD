class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def insertvan(self,num):
        if self.root is None:
            self.root = Node(num)
            self.root.right  = Node(0)
        else:
            cur = self.root
            while True:
                if cur.left is None:
                    cur.left = Node(num)
                    cur.left.right = Node(0)
                    break
                cur = cur.left
        return self.root

    def vanbooking(self,day):
        while True:
            cur = self.root
            while cur:
                if cur.right.data == 0:
                    cur.right.data = int(day)
                    print(f'Booking Van {cur.data} | {day} day(s)')
                    return
                cur = cur.left
            cur = self.root
            while cur:
                cur.right.data -= 1
                cur = cur.left

T = Tree()
inp = input("Enter Input : ").split("/")
for van in range(int(inp[0])):
    root = T.insertvan(van+1)
Booking = inp[1].split(" ")
Custommer = 0
for day in Booking:
    Custommer += 1
    print(f'Customer {Custommer} ',end="")
    T.vanbooking(day)