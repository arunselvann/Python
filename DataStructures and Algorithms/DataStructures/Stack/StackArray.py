class Astack:
    def __init__(self):
        self.stack = []

    def isstackempty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)
        print ("Pushed",data)

    def pop(self):
        if self.isstackempty():
            return -1
        return self.stack.pop()

    def top(self):
        if self.isstackempty():
            print ('Stack is empty')
        else:
            print('The top is',self.stack[len(self.stack)-1])

    def size(self):
        print(len(self.stack))


s = Astack()
s.size()
print(s.pop())
s.push(1)
s.push(2)
print(s.stack)
s.push(3)
print(s.stack)
s.top()
s.pop()
s.top()
s.size()
