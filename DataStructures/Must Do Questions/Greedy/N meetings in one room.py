def meetings(arr,arr_s, N):
    result = [arr.index(arr_s[0])+1]
    prev = arr_s[0][1]
    for i in range(1,N):
        if arr_s[i][0] > prev:
            prev = arr_s[i][1]
            result.append(arr.index(arr_s[i])+1)
    print(*result)


for _ in range(int(input())):
    N = int(input())
    temp1 = list(map(int, input().strip().split()))
    temp2 = list(map(int, input().strip().split()))
    arr = list(map(list, zip(temp1, temp2)))
    arr_s = sorted(arr, key=lambda x: x[1])
    meetings(arr,arr_s, N)
