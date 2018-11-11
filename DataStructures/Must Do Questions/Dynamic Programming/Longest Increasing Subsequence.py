def lis(arr, n):
    if n <= 1:
        return n
    l = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1
    return max(l)


T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(lis(arr, n))


