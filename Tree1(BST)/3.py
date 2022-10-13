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

    def printTreeredX3(self, node,num, level = 0):
        if node != None:
            self.printTreeredX3(node.right,num , level + 1)
            if node.data > num:
                print('     ' * level, node.data*3)
            else:
                print('     ' * level, node)
            self.printTreeredX3(node.left,num , level + 1)
            
T = BST()
inp = input("Enter Input : ").replace('/',' ').split(" ")
num = inp[len(inp)-1]
inp = inp[:len(inp)-1]
for i in inp:
    root = T.insert(int(i))
T.printTree(root)
print("--------------------------------------------------")
T.printTreeredX3(root,int(num))
