def subarraySum(n, sum, arr):
    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > sum and start < i - 1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == sum:
            print(start+1, i)
            return 1
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
    print(-1)

T = int(input())
for t in range(T):
    n, s = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    subarraySum(n, s, arr)