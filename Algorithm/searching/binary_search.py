import random


def binary_search(num_list, target):
    u = len(num_list) -1
    l = 0

    while l < u:
        mid = l + (u -l)//2

        if num_list[mid] == target:
            return mid
        elif num_list[mid] > target:
            u = mid - 1
        else:
            l = mid + 1
    return -1


def main():
    # Driver Code
    arr = [i for i in range(0, 500, 2)]
    x = random.randint(0, 500)
    result = binary_search(arr, x)
    if(result == -1):
        print(f"{x} is not present in array")
    else:
        print(f"{x} is present at index {result}")


if __name__ == "__main__":
    main()
