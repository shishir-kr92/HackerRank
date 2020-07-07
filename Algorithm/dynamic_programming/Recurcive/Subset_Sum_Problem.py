
from datetime import datetime as dt

def check_sum_exist(num, sum, n):

    if sum == 0:
        return True

    if sum != 0 and n  == 0:
        return False



    return check_sum_exist(num, sum - num[n-1], n-1) or check_sum_exist(num, sum, n-1)

def check_sum_exist_dp(num, sum, n):
    result = [[False]* (n + 1) for i in range(sum+1)]

    for i in range(sum +1):
        for j in range(n + 1):
            if i == 0:
                result[i][j] = True

            elif i != 0 and j == 0:
                result[i][j] = False

            elif i < num[j-1]:
                result[i][j] = result[i][j-1]

            elif i>= num[j-1]:
                result[i][j] = result[i][j-1] or result[i-num[j-1]][j-1]
    return result[sum][n]


if __name__ == "__main__":
    '''
        https://www.geeksforgeeks.org/subset-sum-problem-osum-space/
        given a list of number, num, and a digit ,sum,
        find whether there is a subset whose sum of all elements in the subset is equal to reqSum
    '''
    temp = input().split(",")
    num = [ int(i) for i in temp]
    reqSum = int(input())

    startTime = dt.now()
    result = check_sum_exist(num, reqSum, len(num) - 1)
    print(result)
    endTime =  dt.now()
    print(endTime - startTime)

    startTime = dt.now()
    check_sum_exist_dp(num, reqSum, len(num))
    print(result)
    endTime = dt.now()
    print(endTime  - startTime)

    #print(result)