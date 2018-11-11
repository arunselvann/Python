class SelectionSort:
    def __init__(self, data=[]):
        self.data = data

    def sort(self):
        for i in range(len(self.data)-1):
            min_val = i
            j = i + 1
            while j < len(self.data):
                if self.data[j] < self.data[min_val]:
                    min_val = j
                j += 1
            if i != min_val:
                self.data[i], self.data[min_val] = self.data[min_val], self.data[i]


l = [2,6,3,2,4,9,1,0]
s = SelectionSort(l)
print(s.data)
s.sort()
print(s.data)
