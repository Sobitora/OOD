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

    def findrank(self,node,num):
        if node:
            if (node.data) <= num:
                return 1+self.findrank(node.left,num)+self.findrank(node.right,num)
            else:
                return self.findrank(node.left,num)
        return 0

T = BST()
inp = input("Enter Input : ").replace('/',' ').split(" ")
num = inp[len(inp)-1]
inp = inp[:len(inp)-1]
for i in inp:
    root = T.insert(int(i))
rank = T.findrank(root,int(num))
T.printTree(root)
print("--------------------------------------------------")
print(f'Rank of {num} : {rank}')