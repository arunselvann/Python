from collections import deque

d, N = deque(), int(input())
for _ in range(N):
    item = list(input().strip().split())
    if len(item) is 2:
        cmd = 'd.'+item[0]+'('+item[1]+')'
    else:
        cmd = 'd.'+item[0]+'()'
    eval(cmd)
print(*d)
