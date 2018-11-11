def nop(n, m):
    if n == 1 or m == 1:
        return 1
    return nop(n, m-1) + nop (n-1, m)


for _ in range(int(input())):
    n, m = map(int, input().strip().split())
    print(nop(n, m))
