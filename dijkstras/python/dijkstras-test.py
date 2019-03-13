from dijkstras import Graph, Node, shortestPath
from random import random

def main():
    numNodes = 6
    numRange = 25

    g = Graph()
    # Setup up nodes
    for i in range(numNodes):
        n = Node()
        g.addNode(n)

    # Connect nodes
    g.connect(1,6,14)
    g.connect(1,3,9)
    g.connect(1,2,7)
    g.connect(2,3,10)
    g.connect(2,4,15)
    g.connect(3,6,2)
    g.connect(3,4,11)
    g.connect(4,5,6)
    g.connect(6,5,9)

    # Test shortest path using Dijkstra's:
    startID = 1
    endID = 5
    pathLen, pathNodes = shortestPath(g, startID, endID)

    print("The shortest path between nodes {} and {} is {}, by taking path {}"\
        .format(startID, endID, pathLen, pathNodes))

if __name__ == "__main__":
    main()