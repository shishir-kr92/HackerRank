
def get_count(s, n):
    a_count = 0
    for c in s:
        if c == 'a':
            a_count += 1
    if (n % len(s)) == 0:
        a_count *= (n/len(s))
    else:
        a_count = a_count * int(n / len(s))
        for i in range(0, (n% len(s))):
            if s[i] == 'a':
                a_count += 1
    return a_count


if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup
    """
    s = input()
    n = int(input().strip())
    print(get_count(s, n))