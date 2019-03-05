

def find_golomb(n):
    if n ==1:
        return 1

    return 1 + find_golomb(n - find_golomb(find_golomb(n-1)))


def get_golomb_sequence(n):
    golomb_no_list = [0 for i in range(n+1)]
    golomb_no_list[1]  = 1
    for i in range(2, n+1):
        no = find_golomb(i)
        golomb_no_list[i] = no
    return golomb_no_list


if __name__ == "__main__":
    '''
        https://www.geeksforgeeks.org/golomb-sequence/
    '''
    n = int(input().strip())
    print(get_golomb_sequence(n))