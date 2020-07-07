def permutation_coefficient_dp(n, k):
    result = [[-1]*(k+1)for i in range(n+1)]

    for i in range(n+1):
        for j in range(min(k,i)+1):
            if j == 0:
                result[i][j] = 1
            else:
                result[i][j] = result[i-1][j] + (j* result[i-1][j-1])

            if (j  < k):
                 result[i][j + 1] = 0
    for i in result:
        print(i)
    return result[n][k]

def permutation_coefficient_recurcive(n,k):
    if k > n:
        return 0
    elif k == 0 :
        return 1
    else:
        return permutation_coefficient_recurcive(n-1, k) + k * permutation_coefficient_recurcive(n-1, k-1)


def main():
    temp = input().split()
    n, k = int(temp[0]), int(temp[1])
    print(permutation_coefficient_recurcive(n, k))
    print(permutation_coefficient_dp(n, k))

if __name__ == "__main__":
    main()