def calculate_subString_search(numString):
    result1 = [int(numString[0])]
    result2 = [int(numString[0])]
    sum = 0
    for i in range(1, len(numString)):
        tempResult =  (i + 1)* int(numString[i]) + (10*  result1[i-1])
        result1.append(tempResult)
        result2.append(tempResult + (result2[i-1]))
    return result2[-1]

if __name__ == "__main__":
    numString = input()
    sum = calculate_subString_search(numString)
    print(sum)

#[9, 104, 1046, 10484, 104885, 1048898, 10489008, 104890104, 48901105, 489011100, 890110994, 901109896]