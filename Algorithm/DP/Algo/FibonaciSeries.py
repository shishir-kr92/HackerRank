
def fibonacci_dp(n):
    fib = [0]*(n+1)

    fib[0] = 0
    fib[1] = 1

    for i in range(2, n+1):
        fib[i] = fib[i -1] + fib[i - 2]
    return fib[n]

def fibonacci_recurcive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recurcive(n-1) + fibonacci_recurcive(n-2)

def main():
    n = int(input("Position : ").strip())
    result = fibonacci_recurcive(n)
    print(result)
    result = fibonacci_dp(n)
    print(result)

if __name__ == "__main__":
    main()