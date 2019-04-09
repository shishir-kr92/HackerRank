
def divisible_sum_pairs(arr, n, k):
    divisor_count = 0
    for i in range(len(arr)-1):
        j = i + 1
        while j < len(arr):
            if (arr[i] + arr[j]) >= k  and int((arr[i]+arr[j]) % k) == 0:
                divisor_count += 1
            j += 1
    print(divisor_count )


if __name__ == "__main__":
    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    divisible_sum_pairs(arr, n, k)