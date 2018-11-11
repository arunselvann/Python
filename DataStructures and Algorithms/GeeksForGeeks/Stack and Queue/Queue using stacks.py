class queue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def enQueue(self, data):
        self.inStack.append(data)

    def deQueue(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()


Q = queue()
Q.enQueue(1)
Q.enQueue(2)
Q.enQueue(3)
print(Q.deQueue())
print(Q.deQueue())
print(Q.deQueue())