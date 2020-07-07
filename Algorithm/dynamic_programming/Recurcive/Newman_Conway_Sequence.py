
def get_newman_conway_element(n):
    if n == 1 or n == 2:
        return 1
    else:
        return get_newman_conway_element(get_newman_conway_element(n-1)) + \
               get_newman_conway_element(n - get_newman_conway_element(n - 1))


def get_newman_conway_sequence(n):
    newman_conway_sequence = [0]* (n + 2)
    newman_conway_sequence[1] = 1
    newman_conway_sequence[2] = 1

    for i in range(3, n+2):
        newman_conway_sequence[i] = get_newman_conway_element(i)

    return newman_conway_sequence[1:-1]


if __name__ == "__main__":
    '''
        https://www.geeksforgeeks.org/newman-conway-sequence/
    '''
    nextIt = 'y'
    while nextIt == 'Y' or  nextIt == 'y':
        n = int(input().strip())
        print(get_newman_conway_sequence(n))
        nextIt = input()

