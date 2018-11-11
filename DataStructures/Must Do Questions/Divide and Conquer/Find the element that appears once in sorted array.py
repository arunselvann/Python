def findDistinct(arr, n):
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-2] != arr[n-1]:
        return arr[n-1]
    for i in range(1,n-2):
        if arr[i] != arr[i+1] and arr[i+1] != arr[i+2]:
            return arr[i+1]


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    r = findDistinct(arr, n)
    print(r)

