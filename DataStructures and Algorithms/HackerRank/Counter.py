from collections import Counter

profit = 0
S = int(input())
c = Counter(list(map(int, input().strip().split())))
N = int(input())
for _ in range(N):
    i, j = map(int, input().strip().split())
    if c[i] > 0:
        c[i] -= 1
        profit += j
print(profit)