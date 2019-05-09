
def hour_glass_sum(arr):
    pattern = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]
    sum_arr = []
    max_sum = -999
    x_limit = len(arr)
    y_limit = len(arr[0])
    for i in range(x_limit - 3 + 1):
        for j in range(y_limit - 3 + 1):
            temp_sum = 0
            for cell in pattern:
                x_cor = i + cell[0]
                y_cor = j + cell[1]
                temp_sum += arr[x_cor][y_cor]
            if max_sum < temp_sum :
                max_sum = temp_sum
    return max_sum

if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
    """
    arr = []
    for i_ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hour_glass_sum(arr)
    print(result)
