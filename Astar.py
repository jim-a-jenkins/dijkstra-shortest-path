# NAME: James Jenkins
# REFERENCES: Code based on my work from last semester Algorithms class
# STUDENT ID: 104479208

class PriorityQueue:
    def __init__ (self, nNodes):
        self.n = nNodes
        self.d = {}
        self.Inf = float('inf')

    def set(self, i, dist):
        assert(i >= 0 and i < self.n)
        self.d[i] = min(dist, self.Inf)

    def hasKey(self,i):
        return i in self.d

    def get(self,i):
        assert(i >= 0 and i < self.n)
        assert(i in self.d)
        return self.d[i]

    def extractMin(self):

        m = len(self.d)
        assert (m > 0), 'Empty Queue'

        minDist = self.Inf
        minKey = -1

        for (i,dist) in self.d.items():
            if (dist <= minDist):
                minDist = dist
                minKey = i
        assert (minKey >=  0.0), ('minKey = '+str(minKey)+' dist='+str(dist))
        self.d.pop(minKey,None)


        return (minKey, minDist)

    def isEmpty(self):
        m = len(self.d)
        return (m <= 0)

class MyGraph:
    def __init__(self, nVertices):
        self.n = nVertices
        self.adjList = [ [] for i in range(0,nVertices) ]
        

    def getName(self,i):
        return str(i)

        
    def addEdge(self,i,j,w):
        assert( i >= 0 and i < self.n)
        assert( j >= 0 and j < self.n and j != i)
        lst = self.adjList[i]
        lst.append( (j,w) )
        
    def singleSourceShortestPath(self, srcID):
        assert (srcID >= 0 and srcID < self.n)
        pq = PriorityQueue(self.n)
        
        for i in range(0,self.n):
            if ( i == srcID):
                pq.set(i,0.0)
            else:
                pq.set(i, pq.Inf)


        d = {}

        pi = {}

        while(not pq.isEmpty()):
            (u, cost) = pq.extractMin()
            d[u] = cost
            for i in range(len(self.adjList[u])):
                if(pq.hasKey(self.adjList[u][i][0]) and self.adjList[u][i][1] + d[u] < pq.get(self.adjList[u][i][0])):
                    pq.set(self.adjList[u][i][0],self.adjList[u][i][1] + d[u])
                    #print(self.adjList[u])
                    pi[self.adjList[u][i][0]] = u
                    #print("Current Distance:",d[u], "Node:",u)

        return (d,pi)
        
    def getShortestPath(self,d,pi,srcID, destID):
        assert (srcID in d), 'It looks like your Dijkstra code is not complete'
        assert (d[srcID] <= 0.0)
        if (destID not in pi):
            assert False , ' No path from the given source : %d to destination: %d'%(srcID,destID)
        lst = [destID]
        curNode = destID
        while (curNode != srcID):
            assert(curNode in pi)
            curNode = pi[curNode]
            lst.insert(0,curNode)
        return lst





# TEST
graph = MyGraph(19)
s = 0
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
graph.addEdge(s, a, 2)
graph.addEdge(a, b, 1)
graph.addEdge(b, c, 4)
graph.addEdge(b, p, 6)
graph.addEdge(c, d, 4)
graph.addEdge(d, g, 5)
graph.addEdge(d, e, 4)
graph.addEdge(e, r, 3)
graph.addEdge(g, h, 3)
graph.addEdge(g, r, 4)
graph.addEdge(h, i, 2)
graph.addEdge(h, j, 3)
graph.addEdge(r, j, 2)
graph.addEdge(r, l, 2)
graph.addEdge(p, q, 7)
graph.addEdge(q, l, 2)
graph.addEdge(l, m, 2)
graph.addEdge(m, n, 3)
graph.addEdge(n, o, 4)
graph.addEdge(o, k, 5)
graph.addEdge(i, k, 3)
graph.addEdge(k, f, 2)

(d,pi) = graph.singleSourceShortestPath(0)
myList = graph.getShortestPath(d,pi,0,6)

convert = {0:'S', 1:'A', 2:'B', 3:'C', 4:'D', 5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R'}


for i in myList:
    print(convert[i])

heuristic = {0:8, 1:10, 2:12, 3:10, 4:8, 5:0, 6:8, 7:6, 8:4, 9:4, 10:2, 11:8, 12:8, 13:6, 14:4, 15:12, 16:8, 17:6, 18:10}


