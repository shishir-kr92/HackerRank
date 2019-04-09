
def get_GCD(x, y):
    res = 0
    while x != 0:
        res = y%x
        y = x
        x = res
    return y

def get_LCM(x, y):
    return int((x*y)/get_GCD(x, y))


def getTotalX(a, b):
    count = 0
    resultant_LCM = 0
    resultant_GCD = 0
    for i in range(len(a)):
        if i == 0:
            resultant_LCM = a[i]
        else:
            resultant_LCM = get_LCM(resultant_LCM, a[i])

    for i in range(len(b)):
        if i == 0:
            resultant_GCD = b[i]
        else:
            resultant_GCD = get_GCD(resultant_GCD, b[i])
    print(resultant_LCM)
    print(resultant_GCD)
    for i in range(resultant_LCM, resultant_GCD + 1):
        if resultant_GCD % i == 0 and i % resultant_LCM == 0:
            print(i)
            count += 1
    return count

if __name__ == "__main__":
    '''
        https://www.hackerrank.com/challenges/between-two-sets/problem
    '''
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(getTotalX(a, b))
