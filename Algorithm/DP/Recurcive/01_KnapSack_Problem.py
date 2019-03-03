
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
    result = knapsack_recurcive(value, weight, maxCargoWeight, len(weight))
    print(result)

