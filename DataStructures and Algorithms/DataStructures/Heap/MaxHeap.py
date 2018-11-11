class MaxHeap:
    def __init__(self):
        self.heap = []

    def isHeapEmpty(self):
        return len(self.heap) == 0

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

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
        if self.isHeapEmpty():
            print('Heap is Empty')
        else:
            return self.heap[0]

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, i):
        parent = (i - 1) // 2
        if i == 0:
            return
        elif self.heap[i] > self.heap[parent]:
            self.__swap(i, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, i):
        left = (i*2) + 1
        right = (i*2) + 2
        largest = i
        if len(self.heap)-1 > left and self.heap[largest] < self.heap[left]:
            largest = left
        elif len(self.heap)-1 > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != i:
            self.__swap(i, largest)
            self.__bubbleDown(largest)

h = MaxHeap()
print(h.peak())
for i in range(5):
    h.push(i)
print(h.heap)
print(h.peak())
h.pop()
print(h.heap)
print(h.peak())