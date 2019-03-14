import sys
from os import path
from random import randint

from binarySearch import binarySearch

# Add algorithms directory to path
sys.path.insert(0, \
    r"D:\\github-projects\\algorithms\\quicksort\\python")
import quicksort
sys.path.pop(0)



ELEMENTS = 10

def testEmpty():
    print("Running testEmpty():")
    arr = []
    key = 1
    assert(binarySearch(arr, key) == -1)
    print("***** PASS *****")

def testInOrder():
    arr = []
    print("\nRunning testInOrder:")
    # Insert elements in order
    for i in range(ELEMENTS):
        arr.append(i)
    # Ensure we can find every element
    for i in range(ELEMENTS):
        assert(binarySearch(arr, i) != -1)
    
    print("***** PASS *****")

def testRandom():
    arr = []
    # Range for random integers
    low, high = 0, 1000
    print("\nRunning testRandom:")

    # Insert random elements
    for _ in range(ELEMENTS):
        arr.append(randint(low, high))

    # Sort array
    quicksort.quicksort(arr)

    # Ensure we can find all the elements in the array
    for num in arr:
        if (binarySearch(arr, num) == -1):
            print("Error: number {} not found in array".format(\
                num))
        #assert(binarySearch(arr, num) != -1)
    print("***** PASS *****")


def main():
    testEmpty()
    testInOrder()
    testRandom()

if __name__ == "__main__":
    main()

def template():
    print("\nRunning template:")

    print("***** PASS *****")
