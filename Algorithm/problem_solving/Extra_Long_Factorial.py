
def get_factorial(n):

    sub_result = [1] * (n+1)

    for i in range(2, n+1):
        sub_result[i] = i * sub_result[i-1]
    return sub_result[-1]


if __name__ == "__main__":
    n = int(input())
    result = get_factorial(n)
    print(result)