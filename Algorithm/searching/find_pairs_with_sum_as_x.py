
'''
Write a program that, given an array A[] of n
numbers and another number x, determines whether or not there exist
two elements in S whose sum is exactly x.


Input: arr[] = {0, -1, 2, -3, 1}
        sum = -2
        Output: -3 ,1
        Explanation: If we calculate the sum,
        1 + (-3) = -2

Input: arr[] = {1, -2, 1, 0, 5}
       sum = 0
       Output: -1
       Explanation: No valid pair exists

LINK:
https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/
'''


def find_pair_sorting(num_list, n, required_sum):
    num_list.sort()

    i = 0
    j = n - 1

    while i < j:
        temp = num_list[i] + num_list[j]

        if temp == required_sum:
            return (num_list[i], num_list[j])
        elif temp > required_sum:
            j -= 1
        else:
            i += 1
    return None


def find_pair_hashing(num_list, n, required_sum):
    temp_set = set()

    for index, num in enumerate(num_list):
        temp = required_sum - num
        if temp in temp_set:
            return (num, temp)
        else:
            temp_set.add(num)
    print(temp_set)
    return None


# Driver program to test the functions
def main():
    num_list = [1, 4, 45, 6, 10, -8]
    required_sum = 11
    result = find_pair_sorting(num_list, len(num_list), required_sum)
    if result:
        print(f"Array has two elements with the given sum, number = {result}")
    else:
        print("Array doesn't have two elements with the given sum")

    result = find_pair_hashing(num_list, len(num_list), required_sum)
    if result:
        print(f"Array has two elements with the given sum, number = {result}")
    else:
        print("Array doesn't have two elements with the given sum")


if __name__ == "__main__":
    main()