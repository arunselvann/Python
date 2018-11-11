def cap(n,m):
    l = [[1]*(m)]*(n)
    for i in range(1,n):
        for j in range(1,m):
            l[i][j] = l[i-1][j] + l[i][j-1]
    print(l[n-1][m-1])

for t in range(int(input())):
    n, m = map(int, input().strip().split())
    cap(n,m)