import sys


class MergeSort:
    def __init__(self, data=[]):
        self.data = data

    def sort(self):
        self.sort2(self.data, 0, len(self.data)-1)

    def sort2(self, data, first, last):
        if first < last:
            middle = (first+last)//2
            self.sort2(self.data, first, middle)
            self.sort2(self.data, middle+1, last)
            self.merge(self.data, first, middle, last)

    def merge(self, data, first, middle, last):
        l = self.data[first:middle+1]
        r = self.data[middle+1:last+1]
        l.append(sys.maxsize)
        r.append(sys.maxsize)
        i = j = 0
        for k in range(first, last+1):
            if l[i] <= r[j]:
                self.data[k] = l[i]
                i += 1
            else:
                self.data[k] = r[j]
                j += 1


A = [5,9,1,2,4,8,6,3,7,1]
s = MergeSort(A)
s.sort()
print(s.data)