
def array_manipulation(ops, size_of_array):
    M = [0] * size_of_array
    A = [1,2,3,4,5]
    max_value = 0
    for op in ops:
        a = op[0]
        b = op[1]
        k = op[2]
        M[a-1] += k
        if b < size_of_array:
            M[b] -= k
    for i in range(1, size_of_array):
        M[i] += M[i-1]
        if max_value < M[i]:
            max_value = M[i]
    return max_value





if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
    """
    size_of_array, no_of_ops = [int(i) for i in input().rstrip().split()]
    ops = []
    for i in range(no_of_ops):
        ops.append([int(i) for i in input().rstrip().split()])
    result = array_manipulation(ops, size_of_array)
    print(result)

