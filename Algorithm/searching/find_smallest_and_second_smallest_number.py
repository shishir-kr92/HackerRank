

def find_smallest_pair(num_list):
    num1 = num2 = 10**9

    for i in num_list:
        if i < num1:
            num2 = num1
            num1 = i
        elif i < num2 and i != num1:
            num2 = i
    return num1, num2


# Driver program to test the functions
def main():
    num_list = [3, 6, 100, 9, 10, 12, 7, -1, 10]
    result = find_smallest_pair(num_list)
    print(result)


if __name__ == "__main__":
    main()
