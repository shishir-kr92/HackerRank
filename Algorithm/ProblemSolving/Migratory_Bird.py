
def get_migratory_birds(arr):
    max_type_bird = 0
    birds_count = [0]*(len(arr)+1)
    for i in arr:
        birds_count[i] += 1

    print(birds_count)
    for i in range(len(birds_count)):
        if birds_count[i] > birds_count[max_type_bird]:
            max_type_bird = i
    return max_type_bird


if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/migratory-birds/problem
    """
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(get_migratory_birds(arr))