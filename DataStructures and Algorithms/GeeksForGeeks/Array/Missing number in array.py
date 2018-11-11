def missingNumber(arr, N):
    lb = 0
    ub = N
    if ub == 1:
        if arr[1] == 1:
            return 2
        else:
            return 1
    if arr[ub] == arr.index(arr[ub]):
        return ub + 1
    while lb <= ub:
        mid = (lb+ub)//2
        if ub - lb == 1:
            if arr[ub] != arr.index(arr[ub]):
                return ub
            else:
                return lb
        elif arr[mid] == arr.index(arr[mid]):
            lb = mid
        elif arr[mid] > arr.index(arr[mid]):
            ub = mid
    return -1

def msn(arr, N):
    t1 = 0
    t2 = 0
    for i in range(1,N+1):
        t1 += i
    for i in arr:
        t2 += i
    return t1-t2


T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(msn(arr,N))
    arr.sort()
    arr.insert(0,0)
    print(missingNumber(arr, N-1))

