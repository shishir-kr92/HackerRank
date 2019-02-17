
# Gold Mine problem
# Returns maximum amount of
# gold that can be collected
# when journey started from
# first column and moves
# allowed are right, right-up
# and right-down
#https://www.geeksforgeeks.org/gold-mine-problem/

def get_max_gold(gold, m, n):
    profit = [[0]*n for i in range(m)]

    for column in range(n):
        for row in range(m):
            right_upper = 0
            right = 0
            right_lower = 0

            #condition for right_upper
            if row == 0 or column == 0:
                right_upper == 0
            else:
                right_upper = profit[row - 1][column - 1]

            #condition for right
            if column == 0:
                right = 0
            else:
                right = profit[row ][column - 1]

            #condition for right_lower
            if row == m -1:
                right_lower = 0
            else:
                right_lower = profit[row + 1][column - 1]

            profit[row][column] = gold[row][column] +  max(right_lower, right, right_upper)

    res = profit[m-1][n-1]
    for i in range(1, m):
        res = max(res, profit[i][n-1])
    return  res


if __name__ == "__main__":
    gold = [[1, 3, 1, 5],
            [2, 2, 4, 1],
            [5, 0, 2, 3],
            [0, 6, 1, 2]]

    m = 4
    n = 4

    print(get_max_gold(gold, m, n))