
def get_count(coin_list, n, m):
    '''
    :param coin_list:  list of coins
    :param n: total amount
    :param m: number of types of coin
    :return: number of way we can get sum of n from m type of coins
    '''
    change_count = [[0] * (m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(1, m+1):
            if i == 0:
                change_count[i][j] = 1
            else:
                '''
                    either take the (j-1)th coin or dont take it
                    x : dont take the (j-1)th coint
                    y : take the (j-1)th coint
                '''
                x = change_count[i][j-1] if j-1 >=0 else 0
                y = change_count[i - coin_list[j-1]][j] if (i - coin_list[j-1]) >=0 else 0
                change_count[i][j] = x + y
    return change_count[n][m]


if __name__ == "__main__":
    '''
        n : number of unit
        m : number of coin type
        coint_list : list of each coin type
    '''
    n, m = map(int , input().split())
    coin_list = list(map(int, input().split()))
    print(coin_list)
    get_count(coin_list, n, m)