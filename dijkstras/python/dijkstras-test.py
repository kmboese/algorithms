from dijkstras import Graph, Edge, Node, dijkstras
from random import random

def main():
    numNodes = 3
    numRange = 25

    g = Graph()
    # Setup up nodes
    nodes = []
    for i in range(numNodes):
        n = Node()
        nodes.append(n)

    # Connect nodes

    g.addEdge(nodes[0], nodes[1], int(random()*numRange) + 1)
    g.addEdge(nodes[0], nodes[2], int(random()*numRange) + 1)
    g.addEdge(nodes[1], nodes[2], int(random()*numRange) + 1)

    # Print graph
    g.print()

if __name__ == "__main__":
    main()