class noofrots:
    def findmid(self, arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return i + 1
        return "Not Rotated"


nor = noofrots()
arr = [7, 9, 11, 12, 15]
print(nor.findmid(arr))