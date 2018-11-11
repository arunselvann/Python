class BubbleSort:
    def __init__(self, data=[]):
        self.data = data

    def sort(self):
        swapped = 1
        for j in range(len(self.data)-1):
            if swapped == 1:
                swapped = 0
                for i in range(len(self.data)-(j+1)):
                    if self.data[i] > self.data[i+1]:
                        self.data[i],self.data[i+1] = self.data[i+1],self.data[i]
                        swapped = 1


l = [2,6,3,2,4,9,1,0,0]
s = BubbleSort(l)
print(s.data)
s.sort()
print(s.data)

