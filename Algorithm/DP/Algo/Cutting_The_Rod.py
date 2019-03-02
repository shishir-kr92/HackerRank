
def getMaxProfit_recurcive(cost, size, n):
    if size <= 0  :
        return 0

    if n == 0  and size != 0:
        return cost[0] * size
    if n> size:
        return  getMaxProfit_recurcive(cost, size, n-1)

    totalProfit = max(cost[n -1] + getMaxProfit_recurcive(cost, size - n,  n-1),
                      getMaxProfit_recurcive(cost, size, n-1))

    return totalProfit



if __name__ == "__main__":
    '''
    1, 5, 8, 9, 10, 17, 17, 20
    Given a rod of length n inches and an array of prices that contains prices of
    all pieces of size smaller than n.Determine the maximum value obtainable by
    cutting up the rod and selling the pieces
    
    https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
    '''
    temp = input().split(",")
    cost = [ int(i.strip()) for i in temp]
    size = len(cost)
    print(getMaxProfit_recurcive(cost, size, len(cost)))
