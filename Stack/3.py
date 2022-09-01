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

inp = input('Enter Infix : ')
S = Stack()
print('Postfix : ', end='')
opareter = {'-':1,'+':1,'*':3,'/':3,'^':5,'(':6}
for x in inp :
    if x in "+-*/^(" :
        if S.isEmpty():
            S.push(x)
        else:
            temp = S.pop()
            if opareter[x] > opareter[temp] or temp == '(':
                S.push(temp)
                S.push(x)
            else:
                while opareter[x] <= opareter[temp] :
                    print(temp,end='')
                    if not S.isEmpty():
                        temp = S.pop()
                        if opareter[x] > opareter[temp] or temp == '(':
                            S.push(temp)
                            S.push(x)
                            break
                    else:
                        S.push(x)
                        break
    elif x == ')':
        while not S.isEmpty():
            temp = S.pop()
            if temp == '(':
                break
            else:
                print(temp,end='')
    elif x == inp[len(inp)-1]:
        print(x,end='')
        while not S.isEmpty():
            print(S.pop(),end='')
    else:
        print(x,end='')