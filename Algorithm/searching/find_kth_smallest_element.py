def find_kth_smallest_element(num_list, low, high, k):
    return -1


def main():
    num_list = [1, 4, 45, 6, 10, -1]
    target = 10
    result = find_kth_smallest_element(num_list, 0, len(num_list), target)
    print(result)


if __name__ == "__main__":
    main()