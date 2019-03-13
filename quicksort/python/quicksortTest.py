from quicksort import quicksort
from random import randint
import sys

ELEMENTS = 3000

# Increase max recursion limit
sys.setrecursionlimit(ELEMENTS*2)

def fillArrayRandom(arr, elements, low, high):
    for _ in range(elements):
        arr.append(randint(low, high))

def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def testRandom():
    print("Beginning testRandom:")
    arr = []
    low = 0
    high = 1000
    fillArrayRandom(arr, ELEMENTS, low, high)
    quicksort(arr)
    if not isSorted(arr):
        print(arr)
    assert(isSorted(arr))
    print("*****\tPASS\t*****")

def testInOrder():
    print("Beginning testInOrder:")
    arr = [i for i in range(ELEMENTS)]
    quicksort(arr)
    assert(isSorted(arr))
    print("*****\tPASS\t*****")


def main():
    testRandom()
    testInOrder()

if __name__ == "__main__":
    main()