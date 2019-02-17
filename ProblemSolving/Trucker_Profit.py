'''
    0-1 Knapsack problem
'''
def findTruckCargo(maxCargoWeight, cargoList):
    N= len(cargoList)

    K = [[0 for x in range(maxCargoWeight + 1)] for x in range(N + 1)]

    for i in range(N+1):
        for j in range(maxCargoWeight + 1 ):
            if i ==0 or j == 0:
                K[i][j] = 0
            elif cargoList[i - 1][1] <= j:
                K[i][j] = max(cargoList[i-1][2] + K[i-1][j - cargoList[i-1][1]] , K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    print(K[i][j])


if __name__ == "__main__":
    maxCargoWeight = int(input("max weight :").strip())
    totalCargo = int(input("total no of cargo :").strip())
    entries = int(input("no of entries :").strip())
    cargoList = []

    #cargo_no weight_of_cargo profit_on_cargo

    for i in range(totalCargo):
        cargoList.append(list(map(int, input().rstrip().split())))
    result = findTruckCargo(maxCargoWeight, cargoList)
    print(result)

