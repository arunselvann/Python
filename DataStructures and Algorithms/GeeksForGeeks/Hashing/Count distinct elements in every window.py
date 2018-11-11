def countDistinct(arr, n, k):
    w = (n - k) + 1
    result = []
    for i in range(w):
        a = set(arr[i:k+i])
        result.append(len(a))
    print(*result)


for _ in range(int(input())):
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    countDistinct(arr, n, k)