class Queue:

    def __init__(self):
        self.item = []

    def enQueue(self,data):
        self.item.append(data)

    def deQueue(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)

    def isEmmpty(self):
        return self.size() == 0

    def __str__(self):
        return str(self.item)
