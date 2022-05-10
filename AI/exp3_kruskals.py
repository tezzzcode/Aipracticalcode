from collections import defaultdict
from ctypes import Union

class Graph:
    # constructor
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]

    # addEdge
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    # disjoint set code
    def find_parent(self,parent,n):
        if parent[n]==n:
            return n
        return self.find_parent(parent,parent[n])
        
    def union(self,parent,rank,u,v):
        x=self.find_parent(parent,u)
        y=self.find_parent(parent,v)
        if rank[x]<rank[y]:
            parent[x]=y
        elif rank[y]<rank[x]:
            parent[y]=x
        else:
            parent[y]=x
            rank[x]+=1
    
    # kruskalsAlgorithm
    def kruskal(self):
        self.graph=sorted(self.graph,key=lambda item:item[2])
        MST=[]
        i=0
        e=0
        parent=[]
        rank=[]
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u,v,w=self.graph[i]
            i=i+1
            x=self.find_parent(parent,u)
            y=self.find_parent(parent,v)
            if x!=y:
                e+=1
                MST.append([u,v,w])
                self.union(parent,rank,x,y)
        mincost=0
        for (u,v,w) in MST:
            mincost+=w
            print(u,"--",v,"=",w)
        print(mincost)


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.kruskal()