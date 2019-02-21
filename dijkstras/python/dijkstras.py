graphID = 0
nodeID = 1

class Node:
    def __init__(self):
        global nodeID

        self.ID = nodeID
        self.neighbors = []
        self.visited = False

        nodeID += 1

    def addNeighbor(self, n):
        self.neighbors.append(n)

class Edge:
    def __init__(self, _start, _end, _weight):
        self.start = _start
        self.end = _end
        self.weight = _weight

class Graph:
    def __init__(self):
        global graphID

        self.edges = []
        self.ID = graphID
        graphID += 1

    # Add and edge to a graph
    def addEdge(self, n1, n2, _weight):
        e = Edge(n1, n2, _weight)
        self.edges.append(e)

    def print(self):
        for edge in self.edges:
            print("({},{}: {})".format\
                (edge.start.ID, edge.end.ID, edge.weight))


def dijkstras(g, start, end):   
    pass

