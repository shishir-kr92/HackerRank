def using_dp(coins, total_sum, N):
    K = [[0 for j in range(total_sum + 1)] for i in range(N + 1 )]

    for i in range(1, N + 1 ):
        for j in range(total_sum + 1):
            if j == 0:
                K[i][j] = 1
            else:
                x = K[i][j-coins[i - 1]] if j - coins[i - 1] >= 0 else 0
                y = K[i-1][j] if i-1 >=0 else 0
                K[i][j] = x + y
    print(K)
    return K[i][j]


def using_recurcion(coins, total_sum, N):
    if(total_sum < 0 or N < 0):
        return 0

    elif total_sum == 0:
        return 1
    else:
        return (using_recurcion(coins, total_sum - coins[N], N ) + using_recurcion(coins, total_sum , N - 1 ))





if __name__ == "__main__":
    '''
        https://www.hackerrank.com/challenges/coin-change/problem
        determine the number of ways of making change for a particular
        number of units using the given types of coins
        
        total_sum = total amount that need to be converted into change
        coin_type = number of diff type of coins
        coins = list of coins
        count(S[], m, n) = count(S[], m-1, n) + count(S[], m, n-S[m])
    '''
    tempInput = input().split()
    total_sum = int(tempInput[0].strip())
    coin_type = int(tempInput[1].strip())
    coins = list(map(int, input().rstrip().split()))
    #result = using_recurcion(coins, total_sum, coin_type - 1)
    result = using_dp(coins, total_sum, coin_type)
    print(result)

