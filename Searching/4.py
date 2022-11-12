class hash:

    def __init__(self,table,maxcol,Threshold) :
        self.table = [None]*table
        self.maxcol = maxcol
        self.Threshold = Threshold
        self.data = []
        print("Initial Table :")
        self.print()

    def insert(self,data):
        h = 0
        col = 0
        if data not in self.data:
            self.data.append(data)
            print(f'Add : {data}')
        while True:
            ind = (data%len(self.table)+(h*h))%len(self.table)
            if self.dataover():
                print("****** Data over threshold - Rehash !!! ******")
                self.rehash()
                return False
            if self.table[ind] != None and col < (self.maxcol+1):
                if col < self.maxcol:
                    print(f'collision number {col+1} at {ind}')
                h += 1
                col += 1
                if col == self.maxcol:
                    print("****** Max collision - Rehash !!! ******")
                    self.rehash()
                    return False
            else:
                self.table[ind] = data
                break
        if data == self.data[-1]:
            self.print()

    def dataover(self):
        data = 0
        for i in self.table:
            if i is not None:
                data += 1
            if data+1 >= float(self.Threshold*len(self.table)/100):
                return True
        return False

    def rehash(self):
        table = self.Nextprime(len(self.table)*2)
        self.table = [None]*table

    def Nextprime(self,num):
        while True:
            check = True
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    check = False
                    break
            if check:
                return num
            num += 1

    def print(self):
        for i in range(len(self.table)):
                print(f'#{i+1}	{self.table[i]}')
        print("----------------------------------------")


print(" ***** Rehashing *****")
inp = input("Enter Input : ").split("/")
data = inp[1].split(" ")
inp = inp[0].split(" ")
table = int(inp[0])
maxcol = int(inp[1])
Threshold = int(inp[2])
H = hash(table,maxcol,Threshold)
while True:
    check = True
    for i in data:
        if H.insert(int(i)) == False:
            check = False
            break
    if check:
        exit(0)