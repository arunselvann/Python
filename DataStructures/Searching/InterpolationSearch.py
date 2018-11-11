class InterpolationSearch:
    def __init__(self,data=[]):
        self.data = data

    def search(self, item):
        lb = 0
        ub = len(self.data)-1
        while item >= self.data[lb] and item <= self.data[ub]:
            rise = ub - lb
            run = self.data[ub] - self.data[lb]
            m = rise/run
            x = item - self.data[lb]
            mid = int(m*x) + lb
            print(lb,ub,self.data[lb],self.data[ub],mid)
            if self.data[mid] == item:
                return mid
            elif self.data[mid] < item:
                lb = mid + 1
            else:
                ub = mid - 1
        return -1

arr = [1,3,5,7,9,11,13,15]
s = InterpolationSearch(arr)
print(s.search(8))