def leaders(arr, n):
    result = ''
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            r = arr[i]
            result = str(r) + ' ' + result
        else:
            if arr[i] >= r:
                r = arr[i]
                result = str(r) + ' ' + result
    print(result)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    leaders(arr, n)