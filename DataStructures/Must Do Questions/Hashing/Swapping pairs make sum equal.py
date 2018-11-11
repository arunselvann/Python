def swap(N, M, n, m):
    sum1 = 0
    sum2 = 0
    s = set()
    for i in range(max(n,m)):
        if i < n:
            sum1 += N[i]
            s.add(N[i])
        if i < m:
            sum2 += M[i]
    diff = (sum1 - sum2)/2
    for i in range(m):
        if M[i]+diff in s:
            return 1
    return -1


T = int(input())
for t in range(T):
    n, m = map(int,input().strip().split())
    N = list(map(int,input().strip().split()))
    M = list(map(int,input().strip().split()))
    print(swap(N, M, n, m))
