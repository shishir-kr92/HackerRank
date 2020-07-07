
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

def get_ugly_number_dp(n):
    uglyNum = [0]*n
    i2 = i3 = i5 = 0
    uglyNum[0] = 1

    next_multiple_of_2 = uglyNum[i2] * 2
    next_multiple_of_3 = uglyNum[i3] * 3
    next_multiple_of_5 = uglyNum[i5] * 5

    for i in range(1,n):
        next_ugly_num = min(next_multiple_of_2,
                   next_multiple_of_3,
                   next_multiple_of_5)
        uglyNum[i] = next_ugly_num

        if(next_ugly_num == next_multiple_of_2):
            i2 +=1
            next_multiple_of_2 = uglyNum[i2] * 2

        if (next_ugly_num == next_multiple_of_3):
            i3 += 1
            next_multiple_of_3 = uglyNum[i3] * 3

        if (next_ugly_num == next_multiple_of_5):
            i5 += 1
            next_multiple_of_5 = uglyNum[i5] * 5

    return uglyNum[n-1]

if __name__ == "__main__":
    '''
        Ugly Numbers are number whose only prime factors are 2,3,5
        https://www.geeksforgeeks.org/ugly-numbers/
    '''
    n = int(input("enter the index : "))
    #print(get_ugly_number_simple(n))
    print(get_ugly_number_dp(n))