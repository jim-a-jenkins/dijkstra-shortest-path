# NAME: James Jenkins
# STUDENT ID: 104479208

from random import uniform,randrange
class PriorityQueue:
    '''
      A very naive implementation of a priority queue using a dictionary
      pq.Inf refers to  the value INFINITY
      pq.n : number of vertices
      pq.d : the actual map from vertex ids to distance estimates

      Methods.
        pq.set(i,dist): set node i value to dist
        pq.hasKey(i): does node i exist in pq
        pq.get(i): get the value associated with node i
        pq.extractMin(): extract the minimum value and remove it from the queue
        pq.isEmpty(): is the priority queue empty?
    '''

    def __init__ (self, nNodes):
        #
        # Create a priority code with nNodes vertices in the graph
        #
        self.n = nNodes
        self.d = {}
        self.Inf = float('inf') # A very large number

    def set(self, i, dist):
        # Set the distance of vertex i to dist
        assert(i >= 0 and i < self.n)
        self.d[i] = min(dist, self.Inf)

    def hasKey(self,i):
        # Check if the vertex i belongs to the priority queue
        return i in self.d

    def get(self,i):
        # Get the value associated with vertex i in the queue
        assert(i >= 0 and i < self.n)
        assert(i in self.d)
        return self.d[i]

    def extractMin(self):
        # Extract the minimum distance node from priority queue along with the value
        # of the minimum distance.
        # Remove the node from the queue as well.

        m = len(self.d)
        assert (m > 0), 'You are attempting to extract min from an empty queue'

        minDist = self.Inf
        minKey = -1

        for (i,dist) in self.d.items(): # Iterate through all the items in the dictionary d
            if (dist <= minDist): # If it is smaller than minimal distance so far
                minDist = dist    # update the minimal distance
                minKey = i
        assert (minKey >=  0.0), ('minKey = '+str(minKey)+' dist='+str(dist))
        self.d.pop(minKey,None)   # Remove from the queue


        return (minKey, minDist)  # Return the minimum key and the distance.

    def isEmpty(self):
        # Is the priority queue empty? If yes, return TRUE otherwise, return FALSE.
        m = len(self.d)
        return (m <= 0)

class MyGraph:

    # self.n : number of vertices in the graph
    # self.adjList: Adjacency list stored as a list of lists.
    #    self.adjList[i] stores all adjacent nodes to vertex ID i along with edge weights.
    # Eg., if vertex 2 has three edges (2,3) with weight 4.5, (2,4) with weight 3.2, and (2,5) with 2.1
    #    self.adjList[2] is the list [ (3,4.5), (4,3.2), (5,2.12) ]
    # your goal is to implement the singleSourceShortestPath function.
    
    
    def __init__(self, nVertices):
        # self.n represents the number of vertices of the graph
        self.n = nVertices
        # Adjacency list is initially emtpy
        # adjList[i] = [ (j1, w1), ..., (jk,wk) ]
        #   is a list of adjacent vertices and associated edge weights w1,...,wk
        
        self.adjList = [ [] for i in range(0,nVertices) ]
        

    def getName(self,i):
        # Get the name for vertex i: currently it is just i
        return str(i)

        
    def addEdge(self,i,j,w):
        # Add an edge to graph from i to j with weight w
        assert( i >= 0 and i < self.n)
        assert( j >= 0 and j < self.n and j != i)
        # Append j to adjacency list of i
        lst = self.adjList[i]
        lst.append( (j,w) ) # Add j as adjacent with weight w
      

        
    def prettyPrintAdjacencyList(self):
        # Pretty print the adjacency list
        for i in range(0,self.n): #Iterate over all vertices
            lst = self.adjList[i] # Get the list of adjacent vertices
            print(self.getName(i), '---> [', end='')
            sep='' # Pretty printing stuff
            for (j,w) in self.adjList[i]:
                print(sep, '( ', self.getName(j), ',', w,' )',end='')
                sep=', '
            print(']')


        
    def singleSourceShortestPath(self, srcID):
        assert (srcID >= 0 and srcID < self.n)
        # Implement Dijkstra's algorithm
        # Input:
        # self --> a reference to a MyGraph instance
        # srcID: the id of the source vertex.
        # Expected Output: (d,pi)
        #    d  --> Map each vertex id v to the distance from srcID
        #    pi --> Map each reachable vertex id v (except for srcID) to a parent.

        # Initialize the priority queue
        pq = PriorityQueue(self.n) #create the priority queue
        
        for i in range(0,self.n): # Iterate through all vertex ID
            if ( i == srcID):     # If ID is srcID
                pq.set(i,0.0)     # Distance of srcID should be zero
            else:                 # ID is not srcID
                pq.set(i, pq.Inf) # Distance should be infinity


        d = {}  # Initialize the map with distances to nodes

        pi = {} # Initialize the map with parents of vertices

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
        # Routine to retreive shortest path
        # d: map for each vertex v to its distance from shortest path
        # pi: map from each reachable vertex id to parent
        # srcID: source id (should be the same source id as call to singleSourceShortestPath function)
        # destID: destination id
        # RETURN
        #  lst : a list of nodes to visit with first element of the list as srcID and last one as destID.
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
#graph.prettyPrintAdjacencyList()

(d,pi) = graph.singleSourceShortestPath(0)
print(graph.getShortestPath(d,pi,0,6))

#heuristic = {0:10, 1:8, 2:10, 3:12, 4:10, 5:8, 6:0, 7:8, 8:6, 9:4, 10:4, 11:2, 12:8, 13:8, 14:6, 15:4, 16:12, 17:8, 18:6}
heuristic = {0:8, 1:10, 2:12, 3:10, 4:8, 5:0, 6:8, 7:6, 8:4, 9:4, 10:2, 11:8, 12:8, 13:6, 14:4, 15:12, 16:8, 17:6, 18:10}


