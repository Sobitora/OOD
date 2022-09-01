class Queue:

    def __init__(self) :
        self.item = []

    def enQueue(self,value) :
        self.item.append(value)

    def deQueue(self) :
        return self.item.pop(0)

    def isEmpty(self) :
        return len(self.item) == 0

    def size(self) :
        return len(self.item)

def encodemsg(q1,q2):
    for x in q1.item:
        num = q2.deQueue()
        char = q1.deQueue()
        ascii = ord(char)+int(num)
        if ord(char) <= 90 and ord(char) >=65:
            if ascii > 90:
                ascii -= 26
        else:
            if ascii > 122:
                ascii -= 26
        q1.enQueue(chr(ascii))
        q2.enQueue(num)
    print("Encode message is :  "+str(q1.item))
    for x in range(q2.size()-(q1.size()%q2.size())):
        q2.enQueue(q2.deQueue())

def decodemsg(q1,q2):
    for x in q1.item:
        num = q2.deQueue()
        char = q1.deQueue()
        ascii = ord(char)-int(num)
        if ord(char) <= 90 and ord(char) >=65:
            if ascii < 65:
                ascii += 26
        else:
            if ascii < 97:
                ascii += 26
        q1.enQueue(chr(ascii))
        q2.enQueue(num)
    print("Decode message is :  "+str(q1.item))

inp = input("Enter String and Code : ").split(",")
q1 = Queue()
q2 = Queue()
for x in inp[0]:
    if not x == " ":
        q1.enQueue(x)
for x in inp[1]:
    q2.enQueue(x)
encodemsg(q1, q2)
decodemsg(q1, q2)