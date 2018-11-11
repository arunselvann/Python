from collections import defaultdict

class DepthFirstSearch:
    def __init__(self):
        self.graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

    def addVertex(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start, visited=[]):
        if start not in visited:
            visited.append(start)
            for i in self.graph[start]:
                self.dfs(i, visited)
        return visited

    def dfs2(self, start):
        visited = []
        stack = [start]
        while stack:
            v = stack.pop()
            if v not in visited:
                visited.append(v)
            for i in reversed(self.graph[v]):
                if i not in visited and i not in stack:
                    stack.append(i)
        return visited


g = DepthFirstSearch()
print(g.dfs('A'))
print(g.dfs2('A'))


