
def get_pairing_count_iterative(n):
    N = [0 for i in range(n + 1)]

    for i in range(1, n+1):
        if i <=2:
            N[i] = i
        else:
            N[i] = N[i-1] + (i-1) * N[i-2]
    return N[n]


def get_pairing_count_naive(n):
    if n <= 2:
        return n

    return (get_pairing_count_naive(n-1) + (n - 1) * get_pairing_count_naive(n-2))

if __name__ == "__main__":
    '''
        https://www.geeksforgeeks.org/friends-pairing-problem
        
        n: number of friend
        requirement is to find number of way we can pair them
        
        F(n) = F(n-1) + (n-1) * F(n-2)
        
    '''
    n = int(input())
    #result = get_pairing_count_naive(n)
    result = get_pairing_count_iterative(n)
    print(result)