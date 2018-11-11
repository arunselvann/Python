d=int(input())
arr= Array.arrayRot('i', [1, 2, 3, 4, 5])
print ("The new created array is : ",end="")
for i in range(5):
    print (arr[i],end=" ")
print("\r")

for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")
print("\r")

def rot(d):
    for i in range(d):
        arr.append(arr[0])
        arr.pop(0)
rot(d)

for i in range(5):
    print (arr[i],end=" ")
print("\r")
