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
    result = using_recurcion(coins, total_sum, coin_type - 1)
    print(result)

