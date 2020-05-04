import math
import random


def jump_search(num_list, target):
    jump = int(math.sqrt(len(num_list)))

    for index in range(0, len(num_list), jump):
        if num_list[index] == target:
            return index
        elif num_list[index] > target:
            lower = min(0, index - jump)
            for i in range(index, lower - 1, -1):
                if num_list[i] == target:
                    return i
        else:
            pass
    return -1


def main():
    # Driver Code
    arr = [i for i in range(0, 500, 2)]
    x = random.randint(0, 500)

    result = jump_search(arr, x)
    print(arr)
    if(result == -1):
        print(f"{x} is not present in array")
    else:
        print(f"{x} is present at index {result}")


if __name__ == "__main__":
    main()
