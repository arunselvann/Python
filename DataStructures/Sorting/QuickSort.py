class QuickSort:
    def __init__(self, data=[]):
        self.data = data

    def getPivot(self, data, first, last):
        mid = (first+last)//2
        s = sorted([data[first], data[mid], data[last]])
        if s[1] == data[first]:
            return first
        elif s[1] == data[mid]:
            return mid
        else:
            return last

    def sort(self, data, first, last):
        if first < last:
            p = self.partition(data, first, last)
            self.sort(data, first, p-1)
            self.sort(data, p+1, last)

    def partition(self, data, first, last):
        pi = self.getPivot(data, first, last)
        data[first], data[pi] = data[pi], data[first]
        pv = data[first]
        left = first+1
        right = last
        done = False
        while not done:
            while left <= right and data[left] <= pv:
                left += 1
            while right >= left and data[right] >= pv:
                right -= 1
            if left > right:
                done = True
            else:
                data[left], data[right] = data[right], data[left]
        data[first], data[right] = data[right], data[first]
        return right


l = [5,2,1,6,7,4,3,8,9]
s = QuickSort(l)
print(l)
s.sort(s.data,0,len(s.data)-1)
print(s.data)