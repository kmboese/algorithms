from copy import copy

DEBUG = True
graphID = 0
nodeID = 1

class Node:
    def __init__(self):
        global nodeID

        self.ID = nodeID
        self.neighbors = []
        self.prev = None
        self.visited = False
        self.value = float('inf')

        nodeID += 1

    def getNeighbors(self):
        return self.neighbors

class Graph:
    def __init__(self):
        global graphID

        # nodes dictionary:
        # key: node ID
        # value: Node object
        self.nodes = {}
        self.edges =  {}
        self.ID = graphID

        graphID += 1

    # Add a node to the graph
    def addNode(self, node):
        #n = copy(node)
        self.nodes[node.ID] = node

    # Add and edge to a graph
    def connect(self, startID, endID, travelCost):
        self.nodes[startID].neighbors.append(endID)
        self.edges[(startID, endID)] = travelCost
    
    # Returns the edge cost of two nodes, if it exists, or -1 otherwise
    def edgeCost(self, startID, endID):
        if startID == endID:
            return 0
        else:
            return self.edges[(startID,endID)]

    # Returns True if graph g contains node n, False otherwise
    def contains(self, node):
        if node.ID in self.nodes.keys():
            return True
        else:
            return False

    def print(self):
        for node in self.nodes.values():
            print("Node {}: value = {}".format(\
                node.ID, node.value))
            print("Neighbors: {}".format(\
                node.neighbors))

    def printVisited(self):
        print("Visited nodes: ", end="")
        for node in self.nodes.values():
            if node.visited:
                print("{} ".format(node.ID), end="")
        print()

# Validate graph for dijkstra's
def isValidGraph(g, startID, endID):
    # Verify that the start and end nodes are in the graph
    if g.nodes[startID] is None:
        print("Error: start node not in graph!")
        return False
    if g.nodes[endID] is None:
        print("Error: end node not in graph!")
        return False

    # Verify that all nodes are unvisited at start
    for node in g.nodes.values():
        if node.visited:
            print("Error: node is visited at start!")
            return False
    
    return True


def toString(nodes):
    ret = ""
    for node in nodes:
        ret += str(node.ID)
        ret += " "

    return ret

def dPrint(message):
    if DEBUG:
        print(message)

'''
Finds the shortest path between a start node and and end node.
Inputs:
    g: graph containing nodes and connectivity
    start: node in graph at which to start
    end: node in graph at we wish to reach
Returns:
    Length of the shortest path between start and end, or -1 if error occurs.
'''
def shortestPath(g, startID, endID): 
    if not isValidGraph(g, startID, endID):
        print("Error: graph not valid to perform dijkstra's")
        return -1


    # List of nodes that have not been visited
    unvisitedList = []
    tentativeList = []

    # Start node has 0 value by definition
    currentNode = g.nodes[startID]
    currentNode.value = 0
    endNode = g.nodes[endID]

    # All nodes are unvisited at beginning
    unvisitedList.extend(g.nodes.keys())
    print("Unvisited list: {}".format(unvisitedList))
    # Tentative list starts as just the start node
    tentativeList.append(currentNode)

    print("Tentative list: {}".format(toString(tentativeList)))

    # Main loop: update while end node is not visited
    while not endNode.visited:

        # Update values of neighbor nodes
        for neighbor in currentNode.neighbors:
            node = g.nodes[neighbor]
            oldCost = node.value
            newCost = currentNode.value + g.edgeCost(currentNode.ID, node.ID)

            # Update cost if new cost is lower than previous cost
            if newCost < oldCost:
                dPrint("DEBUG: node {} cost updated from {} to {}".format\
                    (node.ID, oldCost, newCost))
                node.value = newCost

        # Mark the current node as visisted
        currentNode.visited = True

        # if end node was visited, return value as the shortest path
        if endNode.visited:
            return endNode.value

        # Add currentNode neighbors to tentative list (no duplicates)
        # Add neighbors to tentative list
        
        for neighbor in currentNode.neighbors:
            valid = True
            for node in tentativeList:
                if node.ID == neighbor:
                    valid = False
            if valid:
                tentativeList.append(g.nodes[neighbor])

        # sort tentative list by current value
        tentativeList.sort(key=lambda node: node.value, reverse=True)

        # Choose lowest value node as the new current node
        tentativeList.pop()
        print("Node " + str(currentNode.ID) + " removed from tentative list")
        currentNode = tentativeList[-1]
        print("Current node: {}".format(currentNode.ID))
        print("Tentative list: {}".format(toString(tentativeList)))
        g.printVisited()
    
    return g.nodes[endID].value

