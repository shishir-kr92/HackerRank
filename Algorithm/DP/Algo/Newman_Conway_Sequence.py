

def get_newman_conway_sequence(n):
    newman_conway_sequence = [0] * (n + 1)
    newman_conway_sequence[1] = 1
    newman_conway_sequence[2] = 1

    for i in range(3, n+1):
       # print(  newman_conway_sequence[newman_conway_sequence[i-1]],  newman_conway_sequence[i - newman_conway_sequence[i-1]])
        newman_conway_sequence[i] = newman_conway_sequence[newman_conway_sequence[i-1]] \
                                    + newman_conway_sequence[i - newman_conway_sequence[i-1]]
    return newman_conway_sequence[1:]


if __name__ == "__main__":
    n = int(input().strip())
    print(get_newman_conway_sequence(n))