def activityselection(arr, n):
    r = []
    r.append(arr[0])
    prev = arr[0][1]
    for i in range(n-1):
        if arr[i+1][0] >= prev:
            prev = arr[i+1][1]
            r.append(arr[i+1])
    return len(r)


for t in range(int(input())):
    n = int(input())
    temp1 = list(map(int, input().strip().split()))
    temp2 = list(map(int, input().strip().split()))
    arr = list(map(list, zip(temp1, temp2)))
    arr = sorted(arr, key=lambda x: x[1])
    print(activityselection(arr, n))