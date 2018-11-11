class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.capacity = capacity
        self.rear = capacity - 1
        self.q = [None] * capacity

    def isQueueFull(self):
        return self.size == self.capacity

    def isQueueEmpty(self):
        return self.size == 0

    def enQueue(self, Item):
        if self.isQueueFull():
            print('Queue is Full')
            return
        self.rear = (self.rear+1) % self.capacity
        self.q[self.rear] = Item
        self.size += 1
        print("Enqueued", Item)

    def deQueue(self):
        if self.isQueueEmpty():
            print('Queue is Empty')
            return
        print('Dequeued', self.q[self.front])
        self.front = (self.front+1) % self.capacity
        self.size -= 1

    def que_front(self):
        if self.isQueueEmpty():
            print("Queue is empty")
            return
        print("Front item is", self.q[self.front])

    def que_rear(self):
        if self.isQueueEmpty():
            print("Queue is empty")
            return
        print("Rear item is", self.q[self.rear])

    def print(self):
        if self.isQueueEmpty():
            print("Queue is empty")
            print(self.front, self.rear, self.size)
            return
        for i in range(self.front,self.rear+1):
            print(self.q[i], end =" ")
        print(self.front,self.rear,self.size,self.q)



Q = Queue(5)
Q.enQueue(0)
Q.enQueue(1)
Q.enQueue(2)
Q.enQueue(3)
Q.deQueue()
Q.enQueue(4)
Q.print()
Q.enQueue(5)
Q.print()
