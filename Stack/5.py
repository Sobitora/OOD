class Stack :

    def __init__(self) :
        self.value = []
        self.size = 0
    
    def push(self,value) :
        self.value.append(value)
        self.size += 1

    def pop(self) :
        self.size -= 1
        return self.value.pop(-1)
    
    def size(self) :
        return self.size

    def isEmpty(self) :
        return len(self.value) == 0

def dec2bin(decnum):

    s = Stack()
    n = 0
    while decnum > pow(2,n):
        n+=1
    n -= 1
    while n >= 0:
        if decnum >= pow(2,n):
            decnum -= pow(2,n)
            s.push("1")
        else:
            s.push("0")
        n -=1
    return "".join(s.value)

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))