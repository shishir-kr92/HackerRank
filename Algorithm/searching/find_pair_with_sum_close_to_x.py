
def find_pair(num_list, target):
    # num_list.sort()

    i = 0
    j = len(num_list) - 1

    diff = 10**9
    pair = tuple()

    while i < j:

        if abs(num_list[i] + num_list[j] - target) < diff:
            diff = abs(num_list[i] + num_list[j] - target)
            pair = (num_list[i], num_list[j])
        elif num_list[i] + num_list[j] < target:
            i += 1
        else:
            j -= 1
        # print(pair, diff)
    return pair


def main():
    l = [10, 22, 28, 29, 30, 40]
    x = 54
    result = find_pair(l, x)

    print(result)


if __name__ == "__main__":
    main()
