
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

if __name__ == "__main__":
    main()