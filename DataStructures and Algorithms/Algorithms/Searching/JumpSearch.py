import math

class JumpSearch:
    def __init__(self, data=[]):
        self.data = data

    def search(self, item):
        n = len(self.data)
        m = math.floor(math.sqrt(n))
        while self.data[min(m,n)-1] < item:
            prev = m
            if m >= n:
                return -1
            m += m
        while self.data[prev] < item:
            prev += 1
            if prev == min(m,n):
                return -1

        if self.data[prev] == item:
            return prev
        return -1


arr = [1,3,5,7,9,11,13,14,16,19,22,33,44]
s = JumpSearch(arr)
print(s.search(33))


