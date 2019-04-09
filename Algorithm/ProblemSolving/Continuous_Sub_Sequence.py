import sys
#

def get_Least_Sum(numArray):
    final_min = float("inf")
    temp_min = float("inf")

    for index in range(len(numArray)):
        if temp_min > 0 :
            temp_min = numArray[index]
        else:
            temp_min += numArray[index]

        final_min = min(final_min, temp_min)
    return final_min

def countSubSequence(nummArray, sum):
    pass

if __name__ == '__main__':
    testCase = int(input().strip())
    while testCase > 0:
        n = int(input().strip())
        temp = input().split(" ")
        numArray = [int(i.strip()) for i in temp]
        #print(numArray)
        print(get_Least_Sum(numArray))
        testCase -= 1

#1 1 -2 -1 2 4 2 1 0 -7
#3, -4, 2, -3, -1, 7, -5