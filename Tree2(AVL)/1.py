class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
            print("*")
        else:
            cur = self.root
            while True:
                if data > cur.data:
                    print("R",end="")
                    if cur.right is None:
                        cur.right = new
                        print("*")
                        break
                    else:
                        cur = cur.right
                if data < cur.data:
                    print("L",end="")
                    if cur.left is None:
                        cur.left = new
                        print("*")
                        break
                    else:
                        cur = cur.left
        return self.root

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)