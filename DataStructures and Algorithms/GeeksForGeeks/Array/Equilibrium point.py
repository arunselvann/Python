for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().strip().split()))
    r = 0
    if N is 1:
        print(N)
    else:
        for i in range(1, N-1):
            if sum(arr[0:i]) == sum(arr[i+1:N]):
                r = i
                break
        if r is 0:
            print(-1)
        else:
            print(r+1)