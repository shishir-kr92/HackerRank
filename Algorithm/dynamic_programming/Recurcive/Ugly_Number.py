
def get_max_divide(number, divisor):
    while number % divisor == 0:
        number = int(number / divisor)
    return number

def is_ugly(num):
    num = get_max_divide(num, 2)
    num = get_max_divide(num, 3)
    num = get_max_divide(num, 5)

    if num == 1:
        return 1
    else:
        return 0

def get_ugly_number_simple(n):
    count = 1
    num = 1
    while count < n :
        num += 1
        if is_ugly(num):
            count += 1
            #print("{} -> {}".format(count, num))
    return num


if __name__ == "__main__":
    '''
        Ugly Numbers are number whose only prime factors are 2,3,5
        https://www.geeksforgeeks.org/ugly-numbers/
    '''
    n = int(input("enter the index : "))
    print(get_ugly_number_simple(n))