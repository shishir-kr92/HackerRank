def binary_search(num_list, target, l, u):
    mid = 0

    while l <= u:
        mid = l + (u - l) // 2

        if num_list[mid] == target:
            return mid
        elif num_list[mid] > target:
            u = mid - 1
        else:
            l = mid + 1
    return -1


def find_rotation_point(num_list):
    index = 1
    while index < len(num_list):
        if num_list[index] < num_list[index - 1]:
            return index
        index += 1
    return 0


def search_element(num_list, target):
    rotation_point = find_rotation_point(num_list)

    if target == num_list[rotation_point]:
        return rotation_point
    elif target > num_list[rotation_point]:
        return binary_search(num_list, target, rotation_point + 1, len(num_list) - 1)
    else:
        return binary_search(num_list, target, 0, rotation_point - 1)


def main():
    # Driver Code
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    x = 11

    result = search_element(arr, x)
    if(result == -1):
        print(f"{x} is not present in array")
    else:
        print(f"{x} is present at index {result}")


if __name__ == "__main__":
    main()
