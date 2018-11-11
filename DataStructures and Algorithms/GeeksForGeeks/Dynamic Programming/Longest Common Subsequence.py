def lcs(s1, s2, n, m):
    l = [[0]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i is 0 or j is 0:
                l[i][j] = 0
            elif s1[i-1] is s2[j-1]:
                l[i][j] = 1 + l[i-1][j-1]
            else:
                l[i][j] = max(l[i-1][j],l[i][j-1])
    print(l)
    return l[n][m]


T = int(input())
for t in range(T):
    n, m = map(int, input().strip().split())
    s1 = input()
    s2 = input()
    print(lcs(s1, s2, len(s1), len(s2)))


