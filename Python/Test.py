def check_prime(num):
    isPrime = True
    if num == 2 or num == 3 or num == 5:
        return True
    for i in range(2, int(num/2)+1):
        if int(num % i) == 0:
            isPrime = False
            break
    return isPrime

print(check_prime(4))