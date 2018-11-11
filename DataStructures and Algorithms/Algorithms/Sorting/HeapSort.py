import heapq


class HeapSort:
    def __init__(self,data):
        self.heap = data
        heapq._heapify_max(self.heap)

    def Heapify(self, n, i):
        left = (i * 2) + 1
        right = (i * 2) + 2
        largest = i
        if n > left and self.heap[largest] < self.heap[left]:
            largest = left
        if n > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.Heapify(n, largest)

    def sort(self):
        for i in range(len(self.heap)-1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.Heapify(i, 0)



a = [5,1,6,2,3,9,8,7,4]
s = HeapSort(a)
print(s.heap)
s.sort()
print(s.heap)