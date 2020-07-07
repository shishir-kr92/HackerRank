def swap(numArray, i, j):
    temp = numArray[i]
    numArray[i] = numArray[j]
    numArray[j] = temp


def partition(numArray, lowerLimit, upperLimit):
    pivot = numArray[upperLimit]
    i = lowerLimit

    for j in range(lowerLimit, upperLimit):
        if(numArray[j] <= pivot):
            swap(numArray, i, j)
            i += 1

    swap(numArray, i, upperLimit)
    print(numArray, pivot)
    return i


def quickSort(numArray, lowerLimit, upperLimit):
    if upperLimit > lowerLimit:
        p = partition(numArray, lowerLimit, upperLimit)

        quickSort(numArray, lowerLimit, p - 1)
        quickSort(numArray, p +  1, upperLimit)


l = [10, 80, 30, 90, -40, 50, 70]
quickSort(l, 0, len(l) - 1)
print(l)