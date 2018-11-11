class Sumofpairs:
    def search(self, arr, sf):
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if arr[i]+arr[j] == sf:
                    return arr[i],arr[j]
                    break
        return 'Not Found'


sf = int(input())
arr = [1,2,3,4,5,6,7,8,9]
sp = Sumofpairs()
result = sp.search(arr, sf)
print(result)