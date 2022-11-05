class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self,table,maxcol):
        self.table = [None]*table
        self.maxcol = maxcol
    
    def insert(self,data):
        if self.isfull() :
            print("This table is full !!!!!!")
            exit(0)
        else:
            data = data.split(" ")
            sumas = 0
            for i in data[0]:
                sumas += ord(i)
            h = 0
            col = 0
            while True:
                if self.table[((sumas%len(self.table))+(h*h))%len(self.table)] != None and col < (self.maxcol+1):
                    if col < self.maxcol:
                        print(f'collision number {col+1} at {((sumas%len(self.table))+(h*h))%len(self.table)}')
                    else:
                        print("Max of collisionChain")
                        break
                    h += 1
                    col += 1
                else:
                    self.table[((sumas%len(self.table))+(h*h))%len(self.table)]= Data(data[0],data[1])
                    break
            for i in range(len(self.table)):
                print(f'#{i+1}	{self.table[i]}')
            print("---------------------------")

    def isfull(self):
        for i in self.table:
            if i == None:
                return False
        return True

print(" ***** Fun with hashing *****")
inp=input("Enter Input : ").split("/")
table = int(inp[0][0])
maxcol = int(inp[0][2])
inp = inp[1].split(",")
H = hash(table,maxcol)
for i in inp:
    H.insert(i)