class InsertionSort:
    def __init__(self, data=[]):
        self.data = data

    def sort(self):
        for i in range(1, len(self.data)):
            v = self.data[i]
            j = i
            while self.data[j-1] > v and j > 0:
                self.data[j] = self.data[j-1]
                j -= 1
            self.data[j] = v


l = [2,6,3,2,4,9,1,0]
s = InsertionSort(l)
print(s.data)
s.sort()
print(s.data)
