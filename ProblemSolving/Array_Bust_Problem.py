
def getShrunkArray(inputArray, burstLength):
    element_dict = {}
    resultantArray = []
    for element in inputArray:
        if element in element_dict:
            temp = element_dict[element]
            element_dict[element] = temp + 1
        else:
            element_dict[element] = 1
    for element in inputArray:
        if element_dict[element] >= burstLength:
            pass
        else:
            resultantArray.append(element)
    print(resultantArray)


if __name__ == '__main__':
    arraySize = int(input().strip())
    inputArray = []
    for i in range(arraySize):
        c = input().strip()
        inputArray.append(c)
    burstLength = int(input().strip())
    getShrunkArray(inputArray, burstLength)