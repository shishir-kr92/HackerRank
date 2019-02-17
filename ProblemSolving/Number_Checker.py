def convert_to_string(numArray):
    resultant_str = ""
    for num in numArray:
        resultant_str += str(num )+ ","
    return resultant_str.rstrip(",")

def findQualifiedNumbers(numberArray):
    has_One = False
    has_Two = False
    has_Three = False

    final_result = []

    for num in numberArray:
        n = num
        while n > 0 :
            r = n%10;
            if r == 1:
                has_One = True
            if r ==2 :
                has_Two = True
            if r ==3 :
                has_Three = True
            n = int(n / 10)
        if has_One and has_Two and has_Three :
            final_result.append(num)

        has_One = False
        has_Two = False
        has_Three = False
    if len(final_result) != 0:
        final_result = sorted(final_result)
    else:
        final_result.append(-1)
    return convert_to_string(final_result)


if __name__ == "__main__":
    num_count = int(input().strip())
    numberArray = []
    for i in range(num_count):
        num = int(input().strip())
        numberArray.append(num)
    print(findQualifiedNumbers(numberArray))
