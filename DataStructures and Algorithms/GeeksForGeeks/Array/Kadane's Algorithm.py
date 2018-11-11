def maxSum(N,A):
    max = A[0]
    maxend = 0
    for i in range(N):
        maxend = maxend + A[i]
        if max < maxend:
            max = maxend
        if maxend < 0:
            maxend = 0
    return max


T = int(input())
R = []
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    R.append(maxSum(N,A))
for i in R:
    print(i)

