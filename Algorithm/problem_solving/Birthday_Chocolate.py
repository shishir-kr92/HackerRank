
def birthday(bar_value, birth_date, birth_month):
    count = 0
    for i in range(len(bar_value)):
        j = i
        temp_sum = 0
        while (j - i) < birth_month and j < len(bar_value):
            temp_sum += bar_value[j]
            j += 1
        #print(temp_sum)
        if temp_sum == birth_date:
            count += 1
    return count



if __name__ == "__main__":
    no_of_chocolate = int(input().strip())
    bar_value = list(map(int, input().strip().split()))
    birth_date, birth_month = [int(i) for i in input().strip().split()]
    print(birthday(bar_value, birth_date, birth_month))