

'''
An Array of integers is given, both +ve and -ve.
You need to find the two elements such that their sum is closest to zero.

Example
num_list = [1, 4, 45, 6, 10, -1]
pair (1, -1)

LINK:
https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/
'''


def find_pair_sorting(num_list, n):
    num_list.sort()
    print(num_list)
    abs_sum = 10**9
    l_num = r_num = -1

    i = 0
    j = n - 1

    while i < j:
        temp_sum = num_list[i] + num_list[j]
        # print(temp_sum, abs_sum)
        if abs(temp_sum) < abs(abs_sum):
            abs_sum = temp_sum
            l_num = num_list[i]
            r_num = num_list[j]

        if temp_sum > 0:
            j -= 1
        else:
            i += 1
    return (l_num, r_num)


# Driver program to test the functions
def main():
    num_list = [1, 4, 45, 6, 10, -1]
    required_sum = 0
    result = find_pair_sorting(num_list, len(num_list))
    if result:
        print(f"number with sum nearest to zero, number = {result}")
    else:
        print("Array doesn't have two elements with the given sum")


if __name__ == "__main__":
    main()
