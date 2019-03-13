from quicksort import quicksort

def main():
    arr = [10,80,30,90,40,50,70]
    print("Original array: {}".format(arr))
    quicksort(arr)
    print("Sorted array: {}".format(arr))

if __name__ == "__main__":
    main()