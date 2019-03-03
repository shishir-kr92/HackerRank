

def fibonacci_recurcive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recurcive(n-1) + fibonacci_recurcive(n-2)

def main():
    n = int(input("Position : ").strip())
    result = fibonacci_recurcive(n)
    print(result)

if __name__ == "__main__":
    main()