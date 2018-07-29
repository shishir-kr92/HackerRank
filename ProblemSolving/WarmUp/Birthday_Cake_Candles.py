
def birthdayCakeCandles(candles):
    maxNum = 0
    maxCount = 0
    for i in candles:
        if i > maxNum:
            maxNum = i
            maxCount = 1

        elif i == maxNum:
            maxCount += 1

    return [maxNum, maxCount]
if __name__ == '__main__':
    candles =list( map(int, input().rstrip().split(" ")))
    result = birthdayCakeCandles(candles)
    print(result)

