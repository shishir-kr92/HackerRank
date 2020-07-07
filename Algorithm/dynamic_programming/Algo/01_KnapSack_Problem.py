def getKnapSackItem(K, value, weight, maxCargoWeight):
    i, j = len(weight), maxCargoWeight
    knapSack = []
    while ( i >= 0) and (j >= 0):

        if K[i][j] != K[i-1][j]:
            knapSack.append(weight[i - 1])
            j -= weight[i - 1]
            i -=1
        else:
            i -= 1
    return knapSack


def knapsack(value, weight, maxCargoWeight, N):
    '''
        Using Dynamic Programming
          0 1 2 3 4 5...N
        0 0 0 0 0 0 0...
        1 0 x x x x x...
        2 0 x x x x x...
        .
        .
        maxCargoWeight

    '''
    knapSack = [[ 0 for j in range(maxCargoWeight + 1) ] for i in range(N +1)]
    result = []

    for i in range(N + 1):
        for j in range(maxCargoWeight + 1):
            if i == 0 or j == 0:
                knapSack[i][j] = 0
            elif weight[i - 1] <= j:
                knapSack[i][j] = max(value[i-1] + knapSack[i-1][j - weight[i -1]], knapSack[i-1][j])
            else:
                knapSack[i][j] = knapSack[i-1][j]
    for i in range(N + 1):
            print(knapSack[i])
    result.append(knapSack[N][maxCargoWeight])
    result.append(getKnapSackItem(knapSack, value, weight, maxCargoWeight))
    return result


'''recurcive'''
def knapsack_recurcive(value, weight, maxCargoWeight, N):
    if maxCargoWeight == 0 or N == 0:
        return 0

    if weight[N] > maxCargoWeight:
        return  knapsack_recurcive(value,weight, maxCargoWeight, N-1)
    else:
       return  max(knapsack_recurcive(value,weight, maxCargoWeight, N-1),value[N] + knapsack_recurcive(value,weight, maxCargoWeight - weight[N], N))

if __name__ == "__main__":
    '''
        find the maximum profit that can be obtained
        by taking max weight specfied by maxCargoWeight
    '''
    print("enter value of each cargo")
    value = list(map(int , input().split()))

    print("enter weight of each cargo")
    weight = list(map(int , input().split()))

    maxCargoWeight = int(input("max weight :").strip())
    result = knapsack(value, weight, maxCargoWeight, len(weight))
    print(result)

