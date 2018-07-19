def check_difference(arr):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        sum1 += arr[i][i]
        sum2 += arr[0+i][len(arr)-i-1]
    return abs(sum1 - sum2)

if __name__ == '__main__':
    n = int(input("Enter The Limit - "))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = check_difference(arr)
    print(result)

