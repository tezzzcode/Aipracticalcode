from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def bfs(self,s):
        visited=[False]*(max(self.graph)+1)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            a=queue.pop(0)
            print(a,end=' ')
            for i in self.graph[a]:
                if(visited[i]==True):
                    continue
                visited[i]=True
                queue.append(i)

g=Graph()
g.addEdge(0,1) 
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.bfs(0)