from math import floor

def get_Moser_De_Bruijn_Sequence(n):
    moser_de_bruijn_sequence = [0]*n
    moser_de_bruijn_sequence[0] = 0
    moser_de_bruijn_sequence[1] = 1

    for i in range(2, n):
        if i % 2 == 0:
            moser_de_bruijn_sequence[i] = 4 * moser_de_bruijn_sequence[floor(i/2)]
        else:
            moser_de_bruijn_sequence[i] = 4 * moser_de_bruijn_sequence[floor(i/2)] + 1
    return moser_de_bruijn_sequence

if __name__ == "__main__":
    '''
        https://www.geeksforgeeks.org/moser-de-bruijn-sequence/
    '''
    n = int(input().strip())
    print(get_Moser_De_Bruijn_Sequence(n))
