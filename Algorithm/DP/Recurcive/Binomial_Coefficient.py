
def binomial_coefficient_recurcive(n,k):
    if k==0 or k == n:
        return 1
    else:
        return binomial_coefficient_recurcive(n-1, k-1) + binomial_coefficient_recurcive(n-1, k)

def main():
    temp = input().split()
    n,k = int(temp[0]),int(temp[1])
    print(binomial_coefficient_recurcive(n,k))

if __name__ == "__main__":
    '''
        https://www.geeksforgeeks.org/binomial-coefficient-dp-9/
    '''
    main()