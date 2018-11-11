class Queue:
    def __init__(self, capacity):
        self.front = self.rear = -1
        self.capacity = capacity
        self.q = [None] * capacity

    def isQueueFull(self):
        return (self.front == 0 and self.rear == self.capacity-1) or (self.rear == (self.front-1)%(self.capacity-1))

    def isQueueEmpty(self):
        return self.front == -1

    def enQueue(self, data):
        if self.isQueueFull():
            print ('Q is Full')
            return
        elif self.front == -1:
            self.front = self.rear = 0
            self.q[self.rear] = data
        else:
            self.rear += 1
            self.q[self.rear] = data
        print('Enqueued', data,self.front,self.rear,self.capacity)

    def deQueue(self):
        if self.isQueueEmpty():
            print('Q is empty')
            return
        print('Dequeued',self.q[self.front])
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.capacity -1:
            self.front = 0
        else:
            self.front += 1


q = Queue(5)
q.enQueue(0)
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)


