import math

class BucketSort:
    def __init__(self, data=[]):
        self.data = data

    def insertionSort(self, bucket):
        self.data = []
        for i in bucket:
            for j in range(1, len(i)):
                v = i[j]
                k = j
                while i[k - 1] > v and k > 0:
                   i[k] = i[k - 1]
                   k -= 1
                i[k] = v
        for i in bucket:
            for j in i:
                self.data.append(j)
        return self.data

    def sort(self):
        n = len(self.data)
        max_value = max(self.data)
        b = [[] for _ in range(10)]
        divider = math.ceil((max_value + 1)/10)
        for i in self.data:
            j = math.floor(i/divider)
            b[j].append(i)
        print(self.insertionSort(b))


l = [22, 45, 12, 8, 10, 6, 72, 81, 33, 18, 50, 14]
s = BucketSort(l)
print(s.data)
s.sort()

