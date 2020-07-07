from math import  floor

def get_sequence_element(n, debug = False):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if debug:
        print(n)

    if n % 2 == 0:
        return 4 * get_sequence_element(floor(n/2))

    else:
        return  4 * get_sequence_element(floor(n/2)) + 1

def get_sequence(n):
    '''
    :param n: numbers of element of Moser-De-Brujin sequence we want
    :return: list of first n number of Moser-De-Brujin
    '''
    moser_de_brujin_sequence = [0]*n
    moser_de_brujin_sequence[0] = 0
    moser_de_brujin_sequence[1] = 1

    for i in range(2, n):
        debug = False
        moser_de_brujin_sequence[i] = get_sequence_element(i, debug)

    return moser_de_brujin_sequence


if __name__ == "__main__":
    '''
        https://www.geeksforgeeks.org/moser-de-bruijn-sequence/
    '''
    n = int(input().strip())
    print(get_sequence(n))