from collections import defaultdict

def creategraph(e, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2

def isCyclicUtil(v, visited, recStack):
    visited[v] = True
    recStack[v] = True
    for neighbour in graph[v]:
        if visited[neighbour] == False:
            if isCyclicUtil(neighbour, visited, recStack) == True:
                return True
        elif recStack[neighbour] == True:
            return True
    recStack[v] = False
    return False

def isCyclic(n, graph):
    visited = [False] * n
    recStack = [False] * n
    for node in range(n):
        if visited[node] == False:
            if isCyclicUtil(node, visited, recStack) == True:
                return True
    return False

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        print(graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)


