class Stack:
    def __init__(self) :
        self.value = []
        self.size = 0
    
    def add(self,value) :
        self.value.append(value)
        self.size += 1
        print("Add = "+value+" and Size = "+str(self.size))
    
    def pop(self) :
        if len(self.value) == 0:
            print("-1")
        else:
            print("Pop = "+self.value[len(self.value)-1]+" and Index = "+str(self.size-1))
            self.value.pop(-1)
            self.size -= 1
    
    def end(self):
        if len(self.value) == 0:
            return " Empty"
        else:
            text = ""
            for x in self.value:
                text = text+" "+str(x)
            return text

s = Stack()
text = input("Enter Input : ").split(",")
for x in text:
    # print(x)
    if x[0] == "A":
        temp = x.split(" ")
        s.add(temp[1])
    elif x[0] == "P":
        s.pop()
print("Value in Stack ="+s.end())
