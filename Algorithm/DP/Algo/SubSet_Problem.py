def checkSubSet(arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    if(arr[n-1] > sum):
        checkSubSet(arr, n-1, sum)

    return checkSubSet(arr, n-1, sum) or checkSubSet(arr, n -1, sum - arr[n-1])



if __name__=="__main__":

    arr = [2,4,9,1,3,6]
    sum = 2
    result = []
    print(checkSubSet(arr, len(arr), sum))
    print(result)