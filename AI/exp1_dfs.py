from collections import defaultdict

class Graph:
    # constructor
    def __init__(self):
        self.graph=defaultdict(list)

    # add edge
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # dfsUtility
    def dfsUtil(self,s,visited):
        print(s,end=' ')
        visited[s]=True
        for i in self.graph[s]:
            if(visited[i]==True):
                continue
            self.dfsUtil(i,visited)

    # dfs
    def dfs(self,s):
        visited=[False] *(max(self.graph)+1)
        self.dfsUtil(s,visited)

g=Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.dfs(1)