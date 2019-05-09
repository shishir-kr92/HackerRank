

def get_min_swap_count(arr, size_of_array):
    misplaced_count = 0
    gap = int(size_of_array/2)

    while gap > 0:
        for i in range(gap, size_of_array):
            temp = arr[i]
            j = i
            while j >= gap   and arr[ j - gap] > temp:
                arr[j] = arr[j - gap]
                misplaced_count += 1
                j -= gap
            arr[j] = temp
        gap //= 2
    #print(arr)
    return misplaced_count



if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
    """
    size_of_array = int(input())
    arr = [int(x) for x in input().split()]
    result = get_min_swap_count(arr, size_of_array)
    print(result)
'''
    12 34 52 2 3
    n = 5/2 = 2
    
    4

       
'''