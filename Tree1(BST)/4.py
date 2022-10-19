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

    def preorder(self,root):
        if root==None:
            return
        if root.data == self.root.data:
            print("Preorder : ",end="")
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self,root):
        if root == None:
            return
        if root.data == self.root.data:
            print("\nPostorder : ",end="")
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")

    def inorder(self,root):
        if root == None:
            return
        if root.data == self.root.data:
            print("\nInorder : ",end="")
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)

    def breadth(self,root):
        node = []
        node.append(root)
        if root.data == self.root.data:
            print("\nBreadth : ",end="")
        while node:
            tree = node.pop(0)
            print(tree.data,end=" ")
            if tree.left:
                node.append(tree.left)
            if tree.right:
                node.append(tree.right)




T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.preorder(root)
T.inorder(root)
T.postorder(root)
T.breadth(root)