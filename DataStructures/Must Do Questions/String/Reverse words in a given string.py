for _ in range(int(input())):
    r = ''
    arr = list(input().split('.'))
    for i in range(len(arr)-1, -1, -1):
        if i != 0:
            r += arr[i]+'.'
        else:
            r += arr[i]
    print(r)
