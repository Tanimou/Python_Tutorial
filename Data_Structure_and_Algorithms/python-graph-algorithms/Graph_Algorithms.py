##https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-5-graph-algorithms-bfs-dfs-shortest-paths
"""In this lesson, we look at the graph data structure and implement common graph algorithms like breadth-fist search, depth-first search, and shortest paths."""

#num_nodes=5
#edges=[(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

#!Create a class to represent a graph as an adjency list
class Graph():
    def __init__(self, num_nodes, edges):
      self.data=[[] for _ in range(num_nodes)]
      for n1,n2 in edges:
          self.data[n1].append(n2)
          self.data[n2].append(n1)
    def __repr__(self):
        return "\n".join(["{}:{}".format(n,m) for n,m in enumerate(self.data)])
    def __str__(self):
        return self.__repr__()

#graph1=Graph(num_nodes,edges)
#print(graph1)

#!BreadhFirstSearch
#*search in every direction
#*we're gonna represent our graph as a queue using the breadth first search algorithm
def bfs(graph,head):
    queue=[]
    #*we need a discovered list to memorize nodes that have been already discovered, to avoid rediscover them again
    #*and it must as the same length than the graph data
    discovered=[False for _ in range(len(graph.data))]
    
    #*he head node is discovered
    #*note that here the indexes represent the nodes
    #*once discovered we add the node to the queue
    discovered[head] = True
    queue.append(head)
    parent=[None for _ in range(len(graph.data))]
    distance=[None for _ in range(len(graph.data))]
    distance[head]=0
    idx=0
    while idx < len(queue):
        current=queue[idx]
        idx+=1
        #*for each node we look at his edges(relations) with other nodes
        for node in graph.data[current]:
            #*if the node is discovered we add it to the discovered list as True and add the node to the queue
            if not discovered[node]:
                discovered[node]=True
                parent[node]=current
                distance[node]=1+distance[current]
                queue.append(node)
    return queue,distance,parent

#print(bfs(graph1,2))

#!DepthFirstSearch
#*search in one direction only
def dfs(graph,head):
    stack=[]
    result=[]
    discovered=[False for _ in range(len(graph.data))]
    stack.append(head)
    while stack:
        current=stack.pop()
        if not discovered[current]:
            discovered[current]=True
            result.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                     stack.append(node)
            
    return result
#print(dfs(graph1,3))

#!Directed and Weighted graph
class DWGraph():
    def __init__(self, num_nodes,edges,directed=False,weighted=False):
        self.directed=directed
        self.weighted=weighted
        self.data=[[] for _ in range(num_nodes)]
        self.weight=[[] for _ in range(num_nodes)]

        for edge in edges:
            node1, node2,weight=edge
            if self.weighted:
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)
    def __repr__(self):
        return "".join(
            "{}: {}\n".format(i, list(zip(self.data[i], self.weight[i])))
            for i in range(len(self.data))
        )

    def __str__(self):
        return repr(self)

# Graph with weights
#num_nodes5 = 9
#edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6),
 #         (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

#graph2=DWGraph(num_nodes5,edges5,False,True)
#print(graph2)

#!shortest path in a graph-Dijkstra's algorithm applied to a directed weighted graph
"""
1.Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.

2.Assign to every node a tentative distance value: set it to zero for our initial node 
and to infinity for all other nodes. Set the initial node as current.[16]

3.For the current node, consider all of its unvisited neighbours 
and calculate their tentative distances through the current node.
Compare the newly calculated tentative distance to the current assigned value 
and assign the smaller one. For example, if the current node A is marked with a distance of 6, 
and the edge connecting it with a neighbour B has length 2, then the distance to B through A 
will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. 
Otherwise, the current value will be kept.

4.When we are done considering all of the unvisited neighbours of the current node, 
mark the current node as visited and remove it from the unvisited set.
A visited node will never be checked again.

5.If the destination node has been marked visited (when planning a route between two specific nodes) 
or if the smallest tentative distance among the nodes in the unvisited set is infinity
(when planning a complete traversal; occurs when there is no connection between the initial node
and remaining unvisited nodes), then stop. The algorithm has finished.

6.Otherwise, select the unvisited node that is marked with the smallest tentative distance, 
set it as the new "current node", and go back to step 3.
"""
def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current


def pick_next_node(graph,current,distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    neighbors = graph.data[current]
    for  node in neighbors:
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node


def shortest_path(graph, source, dest):
    """Find the length of the shortest path between source and destination"""
    visited = [False] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    parent = [None] * len(graph.data)
    queue = []
    idx = 0

    queue.append(source)
    distance[source] = 0
    visited[source] = True

    while idx < len(queue) and not visited[dest]:
        current = queue[idx]
        update_distances(graph, current, distance, parent)

        next_node = pick_next_node(graph,current,distance, visited)
        
        if next_node is not None:
            visited[next_node] = True
          #  visited1 = visited[next_node:]
            queue.append(next_node)
        idx += 1

    return distance[dest],queue


num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10),
          (2, 4, 3), (4, 3, 4), (3, 5, 11)]
graph7 = DWGraph(num_nodes7, edges7, directed=True,weighted=True)
print(graph7)
print(shortest_path(graph7, 0, 5))

##another way for shortest path using BreadhFirstSearch applied in an undirected unweighted graph

def SPBFS(graph, src, dest):
    visited = [False] * len(graph.data)
    visited[src] = True
    parent = [None] * len(graph.data)
    queue = [(src, 0)]
    idx = 0
    while idx < len(queue) and not visited[dest]:
        (node, distance) = queue[idx]

        if node == dest:
            return queue
        for neighbor in graph.data[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, distance+1))
                parent[neighbor] = node
        idx += 1
    if visited[dest]:
        path = [dest]
        idx = parent[dest]
        path.append(idx)
        while parent[idx] is not None:
            idx = parent[idx]
            path.append(idx)
        path.reverse()
        for node, dist in enumerate(queue):
            if dist[0] == dest:
              return path, queue[node]

    return -1


num_nodes8 = 5
edges8 = [(0, 1), (0, 3), (1, 2), (2, 4), (3, 4)]
num_nodes9 = 6
edges9 = [(0, 1), (0, 2), (1, 2), (1, 3),
          (2, 4), (4, 3), (3, 5)]
#graph8 = Graph(num_nodes8, edges8)
graph9 = Graph(num_nodes9, edges9)
print(graph9)
print(SPBFS(graph9, 0, 5))


