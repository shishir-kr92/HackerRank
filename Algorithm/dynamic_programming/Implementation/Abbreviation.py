


def change_string(a, b ):
    '''
    :param a: String to modified
    :param b: String to match
    :param i: index of last element of a
    :param j: index of last element of a
    :return: True/False
    '''
    i = 0
    j = 0
    result = [[0]*(len(b) + 1) for k in range(len(a) + 1)]
    result[0][0] = 1
    while i < len(a) and j < len(b):
        if result[i][j] == 1:
            if a[i] == b[j]:
                result[i+1][j+1] = result[i][j]
                i += 1
                j += 1
            else:
                if a[i].upper() == b[j]:
                    result[i+1][j+1] = result[i][j]
                    i += 1
                    j += 1
                else:
                    result[i+1][j+1] = 0
                    i += 1
        else:
            i += 1
            j += 1
    for k in result:
        print(k)
    print(result[len(a) -1 ][len(b)-1])
    return result[len(a) -1 ][len(b)-1]


if __name__ == "__main__":
    testCase = int(input().strip())
    while(testCase > 0):
        a = input()
        b = input()
        change_string(a,b)
        testCase  -= 1