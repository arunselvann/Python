import sys

def minDistance(d, spt, v):
    min = sys.maxsize
    r = 0
    for i in range(v):
        if d[i] < min and spt[i] == False:
            min = d[i]
            r = i
    return r

def dijkstra(graph, V, s):
    d = [sys.maxsize] * V
    d[s] = 0
    spt = [False] * V
    for _ in range(V):
        u = minDistance(d, spt, V)
        spt[u] = True
        for v in range(V):
            if graph[u][v] > 0 and spt[v] == False and d[v] > (d[u] + graph[u][v]):
                d[v] = d[u] + graph[u][v]
    print(*d, end='')

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n)]for j in range(n)]
        c=0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[c]
                c+=1
        s = int(input())
        dijkstra(matrix, n, s)
        print('')
