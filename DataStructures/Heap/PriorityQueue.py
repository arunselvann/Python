import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, data):
        heapq.heappush(self.heap, data)

    def pop(self):
        print(-heapq.heappop(self.heap))

    def remove(self, i):
        self.heap.remove(i)
        heapq.heapify(self.heap)

    def peak(self):
        return self.heap[0]


PQ = PriorityQueue()

Q = int(input())
for i in range(Q):
    v = list(map(int, input().split()))
    if v[0] == 1:
        PQ.push(v[1])
    elif v[0] == 2:
        PQ.remove(v[1])
    else:
        print(PQ.peak())

print(PQ.heap)
PQ.pop()
print(PQ.heap)