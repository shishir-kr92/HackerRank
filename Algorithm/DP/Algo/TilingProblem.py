# Python implementation to
# count number of ways to
# tile a floor of size n x m
# using 1 x m tiles

def get_total_ways(n,m):
    arr = [0]*(n+1)
    arr[0] = 0

    for i in range(1, n+1):
        if i > m:
            arr[i] = arr[i-1] + arr[i-2]
        elif i < m:
            arr[i] = 1
        else:
            arr[i] = 2
    print(arr)
    return arr[-1]

if __name__ == "__main__":
    '''
        https://www.geeksforgeeks.org/count-number-ways-tile-floor-size-n-x-m-using-1-x-m-size-tiles/
    '''
    temp = input().split()
    n, m = int(temp[0].strip()), int(temp[1].strip())
    print(get_total_ways(n,m))
