from collections import defaultdict

class BreadthFirstSearch:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, s):
        visited = [s]
        q = [s]
        while q:
            s = q.pop(0)
            for i in self.graph[s]:
                if i not in visited:
                    q.append(i)
                    visited.append(i)
        return visited


g = BreadthFirstSearch()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(5,6)
g.addEdge(6,7)
g.addEdge(4,8)
g.addEdge(8,'A')
g.addEdge('A','B')

print(g.graph)
print(g.BFS(1))