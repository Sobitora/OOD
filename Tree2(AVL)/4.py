class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self) :
        self.root = None

    def insert(self,data):
        num = 0
        if self.root is None:
            self.root = Node([data,num])
        else:
            num += 1
            node = []
            node.append(self.root)
            while node:
                tree = node.pop(0)
                if tree.left is None:
                    tree.left = Node([data,num])
                    break
                else:
                    num += 1
                    node.append(tree.left)
                if tree.right is None:
                    tree.right = Node([data,num])
                    break
                else:
                    num += 1
                    node.append(tree.right)
        return self.root

    def search(self,ordinal):
        if self.root.data[1] == ordinal:
            return self.sumTree(self.root)
        else:
            node = []
            node.append(self.root)
            while node:
                tree = node.pop(0)
                if tree.data[1] == ordinal:
                    return self.sumTree(tree)
                if tree.left:
                    node.append(tree.left)
                if tree.right:
                    node.append(tree.right)

    def sumTree(self,Knight):
        sumpower = 0
        node = []
        node.append(Knight)
        while node:
            tree = node.pop(0)
            sumpower += tree.data[0]
            if tree.left:
                node.append(tree.left)
            if tree.right:
                node.append(tree.right)
        return sumpower

    def check(self,knight1,knight2):
        if self.search(knight1) > self.search(knight2):
            print(f'{knight1}>{knight2}')
        elif self.search(knight1) < self.search(knight2):
            print(f'{knight1}<{knight2}')
        else:
            print(f'{knight1}={knight2}')

T = Tree()
inp = input("Enter Input : ").split("/")
knight = inp[1].split(",")
inp = [int(i) for i in inp[0].split()]
for i in inp:
    root = T.insert(i)
print(T.search(0))
for i in knight:
    T.check(int(i[0]),int(i[2]))
