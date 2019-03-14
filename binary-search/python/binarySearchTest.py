from binarySearch import binarySearch

def main():
    arr = [1, 3, 5, 7, 8, 10, 15]
    key = 20
    index = binarySearch(arr, key)

    if (index == -1):
        print("Key not found")
    else:
        print("Key found at index {}".format(index))
    

if __name__ == "__main__":
    main()