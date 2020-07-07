# Python implementation to
# count number of ways to
# tile a floor of size n x m
# using 1 x m tiles

def get_total_ways(n,m):
    # TODO
    pass

if __name__ == "__main__":
    '''
        https://www.geeksforgeeks.org/count-number-ways-tile-floor-size-n-x-m-using-1-x-m-size-tiles/
    '''
    temp = input().split()
    n, m = int(temp[0].strip()), int(temp[1].strip())
    print(get_total_ways(n,m))
