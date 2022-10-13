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

    def findbelow(self,node,num,below:list):
        if node:
            self.findbelow(node.left,num,below)
            if (node.data) < num:
                below.append(str(node.data))
            self.findbelow(node.right,num,below)
            # if node < num:
            #     below += node.data
        return below


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input("Enter Input : ").replace('|',' ').split(" ")
num = inp[len(inp)-1]
inp = inp[:len(inp)-1]
# print(num)
for i in inp:
    root = T.insert(int(i))
below = T.findbelow(root,int(num),[])
T.printTree(root)
print("--------------------------------------------------")
if below != []:
    print(f'Below {num} : {" ".join(below)}')
else:
    print(f'Below {num} : Not have')