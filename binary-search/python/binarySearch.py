def binarySearch(arr, key):
    left = 0
    right = len(arr)-1

    while (left <= right):
        index = (left+right)//2
        #print(arr[left:right])
        if arr[index] == key:
            return index
        # key to left of current index
        elif arr[index] > key:
            right = index-1
        # Key to right of current index
        else:
            left = index+1
    
    return -1
