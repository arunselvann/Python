def firstsetbit(N):
    s = bin(N)[2:]
    for i in range(len(s)-1,-1,-1):
        if s[i] == '1':
            return len(s)-i
    return 0


T = int(input())
for t in range(T):
    N = int(input())
    print(firstsetbit(N))