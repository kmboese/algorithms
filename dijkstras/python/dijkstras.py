from copy import copy, deepcopy

DEBUG = False
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
            if node.prev is not None:
                print("Node {}: value = {}\tprev = {}".format(\
                    node.ID, node.value, node.prev.ID))
            else:
                print("Node {}: value = {}\tprev = {}".format(\
                    node.ID, node.value, None))
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

    currentNode = None          # node currently being examined
    unvisitedList = []          # list of unvisited nodes
    returnPath = []             # Sequence of nodes to obtain shortest path

    # All nodes unvisited at the beginning
    
    for node in g.nodes.values():
        unvisitedList.append(node)
    #tentativeList = []

    # Start node has 0 value by definition
    currentNode = g.nodes[startID]
    currentNode.value = 0

    # print graph before Dijkstra's
    if DEBUG:
        g.print()

    # Main loop: update while nodes are unvisisted
    while len(unvisitedList) != 0:

        # Current node is unvisited node with smallest value
        unvisitedList.sort(key=lambda node: node.value, reverse=True)
        currentNode = unvisitedList[-1]
        unvisitedList.pop()

        dPrint("Current node: {}".format(currentNode.ID))

        # Update values of neighbor nodes
        for neighbor in currentNode.neighbors:
            node = g.nodes[neighbor]
            oldCost = node.value
            newCost = currentNode.value + g.edgeCost(currentNode.ID, node.ID)

            # Update cost if new cost is lower than previous cost
            if newCost < oldCost:
                dPrint("DEBUG: node {} cost updated from {} to {} by \
node {}".format(node.ID, oldCost, newCost, currentNode.ID))
                node.value = newCost
                node.prev = copy(currentNode)

    # DEBUG: print graph at the end
    if DEBUG:
        g.print()

    # Save the actual path
    currentNode = g.nodes[endID]
    while currentNode is not None:
        returnPath.append(currentNode.ID)
        currentNode = currentNode.prev
    returnPath = returnPath[::-1]
    
    return g.nodes[endID].value, returnPath

