class Stack:
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

class StackCalc:

    def __init__(self) :
        self.S=Stack()

    def run(self,value):
        for x in value:
            if self.check(x):
                self.S.push(x)
            elif x == "DUP":
                temp = self.S.pop()
                self.S.push(temp)
                self.S.push(temp)
            elif x == "POP":
                self.S.pop()
            elif x in "+-*/":
                num1 = int(self.S.pop())
                num2 = int(self.S.pop())
                self.S.push(int(self.cal(x,num1,num2)))
            else:
                self.S.push(x)
                break

    def cal(self,ops,num1,num2):
        if ops == '+':
            sum = int(num1)+int(num2)
        elif ops == '-':
            sum = int(num1)-int(num2)
        elif ops == '*':
            sum = int(num1)*int(num2)
        elif ops == '/':
            sum = int(num1)/int(num2)
        return sum

    def check(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def getValue(self):
        if self.S.isEmpty():
            return 0
        temp = self.S.pop()
        if self.check(temp):
            return temp
        return "Invalid instruction: "+temp

print("* Stack Calculator *")
arg = input("Enter arguments : ").split(" ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
