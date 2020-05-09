
def find_missing_and_repeating_number(num_list, num_limit):
    lookup_list = [0 for _ in range(num_limit + 1)]
    missing_num = None
    duplicate_num = None

    for i in num_list:
        lookup_list[i] += 1


    for index, num in enumerate(lookup_list):
        if index == 0:
            continue
        if num == 0:
            missing_num = index

        if num > 1:
            duplicate_num = index
    return (missing_num, duplicate_num)



def main():
    num_list = [4, 3, 6, 2, 5, 1]
    num_limit = len(num_list)
    result = find_missing_and_repeating_number(num_list, num_limit)

    if result[0]:
        print(f"missing num = {result[0]}")
    else:
        print("No missing num")

    if result[1]:
        print(f"duplicate num = {result[1]}")
    else:
        print("No duplicate num")

if __name__ == "__main__":
    main()