arr= Array.arrayRot('i', [3, 4, 5, 6, 7, 1, 2])


def pivot(a):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            n = i+1

    if a >= arr[0]:
        for i in range(n):
            if a == arr[i]:
                return i
    else:
        for i in range(len(arr)-1, n-1, -1):
            if a == arr[i]:
                return i


print(pivot(3))
print(arr)
