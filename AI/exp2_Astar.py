from collections import deque
from operator import truediv

class Graph:
    # constructor
    def __init__(self,adjac_list):
        self.adj=adjac_list

    # return neighbours of a node
    def get_neighbours(self,n):
        return self.adj[n]
    
    # heuristic function
    def h(self,n):
        return 1
    # Astar alg
    def a_star(self,start,stop):
        open_list=set([start])
        closed_list=set()
        g={}
        g[start]=0
        par={}
        par[start]=start
        while len(open_list)>0:
            n=None
            for i in open_list:
                if(n==None or g[i]+self.h(i)<g[n]+self.h(n)):
                    n=i
            if(n==None):
                print("Path does not exist")
                return None
            if(n==stop):
                ans=[]
                while par[n]!=n:
                    ans.append(n)
                    n=par[n]
                ans.append(start)

                ans.reverse()

                print("path found : {}".format(ans))
                return ans
            for (m,weight) in self.get_neighbours(n):
                if m not in open_list and m not in closed_list:
                    g[m]=g[n]+weight
                    par[m]=n
                    open_list.add(m)
                else:
                    if(g[m]>g[n]+weight):
                        g[m]=g[n]+weight
                        par[m]=n
                        if(m in closed_list):
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)


adjac_list = {
'A': [('B', 1), ('C', 3), ('D', 7)],
'B': [('D', 5)],
'C': [('D', 12)]
}
g=Graph(adjac_list)
g.a_star('A','D')
