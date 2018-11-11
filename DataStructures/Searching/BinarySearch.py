class BinarySearch:
    def __init__(self, arr=[]):
        self.arr = arr

    def search(self, item):
        lb = 0
        ub = len(self.arr)-1
        while lb <= ub:
            mid = (lb+ub)//2
            if self.arr[mid] == item:
                return mid
            elif self.arr[mid] < item:
                lb = mid + 1
            else:
                ub = mid - 1
        return -1

    def search2(self, lb, ub, item):
        mid =(lb+ub)//2
        if lb > ub:
            return -1
        elif self.arr[mid] == item:
            return mid
        elif self.arr[mid] < item:
            return self.search2(mid+1, ub, item)
        else:
            return self.search2(lb, mid-1, item)


arr = [1,3,5,7,9,11,13,14,16,19,22,33,44]
s = BinarySearch(arr)
print(s.search(13))
print(s.search2(0, len(s.arr)-1, 13))
