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
        else:
            cur = self.root
            while True:
                if data > cur.data:
                    if cur.right is None:
                        cur.right = new
                        break
                    else:
                        cur = cur.right
                if data < cur.data:
                    if cur.left is None:
                        cur.left = new
                        break
                    else:
                        cur = cur.left
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self,data):
        if data == self.root.data:
            print("Root")
        else:
            cur = self.root
            while True:
                if data > cur.data:
                    if cur.right is None:
                        break
                    cur = cur.right
                elif data < cur.data:
                    if cur.left is None:
                        break
                    cur = cur.left
                else:
                    check = False
                    if cur.left != None:
                        check = True
                    if cur.right != None:
                        check = True
                    if check:
                        print("Inner")
                    else:
                        print("Leaf")
                    return
            print("Not exist")


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])