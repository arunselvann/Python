from collections import defaultdict

N, M = map(int, input().split())
A = defaultdict(list)
for i in range(N):
    A[input()].append(i+1)
for j in range(M):
    print(A[input()] or -1)