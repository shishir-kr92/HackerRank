def binomial_coefficient_dp(n,k):
    result = [[0]*(k+1) for i in range(n+1)]

    # for i in range(n+1):
    #     result[i][0] = result[i][i] = 1

    for i in range(n+1):
        for j in range(()+1):
            if j == 0 or i ==j:
                result[i][j] = 1
            else:
                result[i][j] = result[i-1][j-1] + result[i-1][j]
    for i in result:
        print(i)
    return result[n][k]



def binomial_coefficient_recurcive(n,k):
    if k==0 or k == n:
        return 1
    else:
        return binomial_coefficient_recurcive(n-1, k-1) + binomial_coefficient_recurcive(n-1, k)

def main():
    temp = input().split()
    n,k = int(temp[0]),int(temp[1])
    # print(binomial_coefficient_recurcive(n,k))
    print(binomial_coefficient_dp(n,k))

if __name__ == "__main__":
    '''
        https://www.geeksforgeeks.org/binomial-coefficient-dp-9/
    '''
    main()