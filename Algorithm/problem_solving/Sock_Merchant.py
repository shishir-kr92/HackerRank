

def get_total_pair(no_of_socks, colour):
    pairs = 0
    pair_count = {}

    for sock in colour:
        if pair_count.get(sock):
            count = pair_count.get(sock) + 1
            if count == 2:
                pairs += 1
                pair_count[sock] = 0
        else:
            pair_count[sock] = 1
    print(pair_count)
    return pairs


if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/sock-merchant/problem
    """
    no_of_socks = int(input().strip())
    colour = list(map(int, input().strip().split()))
    result = get_total_pair(no_of_socks, colour)
    print(result)