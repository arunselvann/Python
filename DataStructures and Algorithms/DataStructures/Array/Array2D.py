from Array.Array import Array

i=5
arr=Array(i)
arr.__setitem__(0,5)
arr.__setitem__(1,4)
arr.__setitem__(2,3)
arr.__setitem__(3,2)
arr.__setitem__(4,1)
for i in range(len(arr)):
    print(arr[i], end=" ")
