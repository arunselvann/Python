def floodFill(matrix, x, y, k, c):
    if matrix[x][y] == c:
        matrix[x][y] = k
        if x != 0:
            floodFill(matrix, x-1, y, k, c)
        if y !=0 :
            floodFill(matrix, x, y-1, k, c)
        if x != len(matrix)-1:
            floodFill(matrix, x+1, y, k, c)
        if y != len(matrix[0])-1:
            floodFill(matrix, x, y+1, k, c)


T = int(input())
for t in range(T):
    i, j = map(int, input().split())
    a = list(map(int, input().split()))
    matrix = [0] * i
    for n in range(i):
        matrix[n] = [0] * j
        for m in range(j):
            matrix[n][m] = a.pop(0)
    x, y, k = map(int, input().split())
    c = matrix[x][y]
    floodFill(matrix, x, y, k, c)
    for n in range(i):
        for m in range(j):
            print(matrix[n][m], end=' ')
    print()