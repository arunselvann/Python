def creategraph(e, n, arr, graph):
    i = 0
    while i<2*e:
        graph[arr[i]].append(arr[i+1])
        i+=2



def topoSort(n, graph):
    stack = []
    visited = []
    print(graph)
    for i in list(graph):
        if i not in visited:
            sortUtil(i,visited,stack)
    print(graph)
    return stack

def sortUtil(v,visited,stack):
    if v not in visited:
        visited.append(v)
    for i in graph[v]:
        if i not in visited:
            sortUtil(i,visited,stack)
    stack.insert(0,v)

from collections import defaultdict
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, N, arr, graph)
        res = topoSort(N, graph)
        valid=True
        for i in range(N):
            n = len(graph[res[i]])
            for j in range(len(graph[res[i]])):
                for k in range(i+1, N):
                    if res[k]==graph[res[i]][j]:
                        n-=1
            if n!=0:
                valid=False
                break
        if valid:
            print(1)
        else:
            print(0)


