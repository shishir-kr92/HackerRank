

def find_missing_number_summation(num_list):
    n = len(num_list)
    expected_sum = (n + 1) * (n + 2) // 2

    actual_sum = 0

    for i in num_list:
        actual_sum += i

    return expected_sum - actual_sum


def find_missing_number_xor(num_list):
    a = num_list[0]
    b = 1
    n = len(num_list)

    for i in range(1, n):
        a = a ^ num_list[i]

    for i in range(2, n + 2):
        b = b ^ i

    return  b ^ a


def main():
    # Driver Code
    arr = [1, 2, 4, 6, 3, 7, 8]

    print("###############summation###############")
    result = find_missing_number_summation(arr)
    if(result == 0):
        print("no number missing")
    else:
        print(f"{result} is is missing ")

    print("############### XOR ###############")
    result = find_missing_number_xor(arr)
    if(result == 0):
        print("no number missing")
    else:
        print(f"{result} is is missing ")



if __name__ == "__main__":
    main()