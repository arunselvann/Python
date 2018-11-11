def le(n, arr):
    r = []
    max = 0
    for i in arr:
        if i > max:
            max = i
    for i in range(n):
        if i == n-1:
            r.append(-1)
        elif arr[i] == max:
            r.append(-1)
        else:
            done = False
            for j in range(i+1, n):
                if arr[i] < arr[j]:
                    r.append(arr[j])
                    done = True
                    break
            if not done:
                r.append(-1)
    return(r)


T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(*le(N, arr))
