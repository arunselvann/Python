class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            max_val = self.heap.pop()
        elif len(self.heap) > 1:
            self.__swap(0, len(self.heap)-1)
            max_val = self.heap.pop()
            self.__bubbleDown(0)
        else:
            max_val = False
        return max_val

    def peak(self):
        if len(self.heap) == 0:
            print('Heap is empty')
        else:
            return self.heap[0]

    def __swap(self, i, j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    def __floatUp(self, i):
        parent = (i-1)//2
        if i == 0:
            return
        elif self.heap[i] < self.heap[parent]:
            self.__swap(i, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, i):
        left = (i*2) +1
        right = (1*2) + 2
        smallest = i
        if len(self.heap)-1 > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        elif len(self.heap)-1 > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != i:
            self.__swap(i,smallest)
            self.__bubbleDown(smallest)


h = MinHeap()
print(h.peak())
for i in reversed(range(5)):
    h.push(i)
print(h.heap)
print(h.peak())
h.pop()
print(h.heap)
print(h.peak())

