import random


def liner_search(arr, n, x):
    for index, num in enumerate(arr):
        if num == x:
            return index
    return -1


def main():
    # Driver Code
    arr = [i for i in range(0, 500, 2)]
    x = random.randint(0, 500)
    n = len(arr)
    result = liner_search(arr, n, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print(f"Element is present at index {result}")


if __name__ == "__main__":
    main()
