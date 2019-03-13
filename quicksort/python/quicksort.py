def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition(arr, low, high):
    i = low-1
    j = low

    # Set pivot as last element
    pivotIndex = high

    for j in range(low, pivotIndex):
        if arr[j] < arr[pivotIndex]:
            i += 1
            swap(arr, i, j)
    
    # swap the pivot with the i+1 element
    swap(arr, i+1, pivotIndex)

    # Return new pivot index
    return (i+1)
        


def quicksort(arr, low=None, high=None):
    # Set bounds if first call
    if low is None or high is None:
        low = 0
        high = len(arr)-1

    # Recursively call quicksort
    if (low < high):
        partitionIndex = partition(arr, low, high)

        quicksort(arr, low, partitionIndex-1)
        quicksort(arr, partitionIndex+1, high)
