
def max_size(arr, n, k):
    sum = 0
    max_cnt = 0
    cnt = 0

    for i in range(n):

        if(sum + arr[i]) <= k:
            sum += sum + arr[i]
            cnt += 1
        elif sum != 0:
            sum -= arr[i - cnt] + arr[i]
        max_sum = max(max_cnt, sum)


if __name__  == "__main__":
    """
       https://www.geeksforgeeks.org/longest-subarray-sum-elements-atmost-k/
    """
    n = int(input())
    arr = [int(i) for i in input().strip().split()]
    k = int(input())
    max_size(arr, n, k)
