def Bubble_Sort(score):
    for i in range(len(score)):
        for j in range(len(score)-i-1):
            if score[j] > score[j+1]:
                swap(score, j, j+1)



def Insertion_Sort(score):
    for i in range(1, len(score)):
        key = score[i]
        j = i-1
        while j >= 0  and key < score[j]:
            score[j+1] = score[j]
            j -= 1
        score[j+1] = key

def get_second_largest_element(score):
    first = -2147483648
    second = -2147483648
    if len(score) < 2:
        print("array size is less the 2")
        return []

    for i in range(len(score)):

        if score[i] > first:
            second = first
            first = score[i]

        elif score[i] > second and score[i] != first:
            second = score[i]
        print(first, " ", second)

    return [first, second]


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

if __name__ == "__main__":
    n = int(input())
    temp = input()
    score = [int(i) for i in temp.split()]
    result = get_second_largest_element(score)
    print(result[0], result[1])
    #Bubble_Sort(score)
    #Insertion_Sort(score)
    print(score)
