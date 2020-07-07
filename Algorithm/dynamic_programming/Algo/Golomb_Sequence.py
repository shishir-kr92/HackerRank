
def get_golomb_sequence(n):
    golomb_sequence = [0 for i in range(n+1)]
    golomb_sequence[1] = 1

    for i in range(2, n+1):
        golomb_sequence[i] = 1 + golomb_sequence[ i - golomb_sequence[golomb_sequence[i-1]]]

    return golomb_sequence[1:-1]



if __name__ == '__main__':
    '''
        https://www.geeksforgeeks.org/golomb-sequence/
    '''
    n  = int(input().strip())
    print(get_golomb_sequence(n))

