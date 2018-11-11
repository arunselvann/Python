class ShellSort:
    def __init__(self, data=[]):
        self.data = data

    def sort(self):
        n = len(self.data)
        gap = n//2
        while gap > 0:
            for i in range(gap,n):
                temp = self.data[i]
                j = i
                while j >= gap and self.data[j-gap] > temp:
                    self.data[j] =  self.data[j-gap]
                    j -= gap
                self.data[j] = temp
            gap //= 2
        return self.data


l = [5,33,1,22,9,0,65,4,5,7]
s = ShellSort(l)
print(l)
print(s.sort())