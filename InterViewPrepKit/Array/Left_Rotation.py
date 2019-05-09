

def left_rotation_old(arr, no_of_rotation):
    arr_length = len(arr)
    for i in range(no_of_rotation):
        temp = arr[0]
        for i in range(1, arr_length):
            arr[i-1] = arr[i]
        arr[-1] = temp
        # print(arr)
    return arr


def left_rotation(arr, no_of_rotation):
    arr_length = len(arr)
    new_arr = [0] * arr_length

    for i in range(0, arr_length):
        new_index = i - no_of_rotation
        if new_index < 0:
            new_arr[arr_length + new_index] = arr[i]
        else:
            new_arr[new_index] = arr[i]
    return new_arr

if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
    """
    size, no_of_rotation = [int(x) for x in input().rstrip().split()]
    arr = [int(x) for x in input().rstrip().split()]
    result = left_rotation(arr, no_of_rotation)
    print(result)
