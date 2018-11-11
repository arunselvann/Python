class TopologicalSort:
    def __init__(self):
        self.graph = {'A': ['C'],
                      'B': ['C', 'D'],
                      'C': ['E'],
                      'D': ['F'],
                      'E': ['F','H'],
                      'F': ['G']}
        self.visited = []
        self.stack = []
        self.path =[]

    def sort(self):
        for i in self.graph:
            self.sortUtil(i)
        return self.stack

    def sortUtil(self, v):
        if v not in self.visited:
            self.visited.append(v)
            try:
                for i in self.graph[v]:
                    self.sortUtil(i)
                self.stack.append(v)
            except KeyError as e:
                self.stack.append(v)


'''def topoSort(n, graph):
    stack = []
    visited = []
    for i in list(graph):
        if i not in visited:
            sortUtil(i,visited,stack)
    return stack

def sortUtil(v,visited,stack):
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            sortUtil(i,visited,stack)
    stack.insert(0,v)'''

s = TopologicalSort()
print(s.sort())