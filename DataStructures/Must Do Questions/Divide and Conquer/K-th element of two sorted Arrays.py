for _ in range(int(input())):
    n, m, k = map(int, input().strip().split())
    a1 = list(map(int, input().strip().split()))
    a2 = list(map(int, input().strip().split()))
    r = a1+a2
    r.sort()
    print(r[k-1])