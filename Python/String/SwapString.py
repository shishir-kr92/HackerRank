def swap_case(word):
    finalOutput = ""
    for char in word:
        charValue = ord(char)
        if charValue >= 65 and charValue <= 90:
            charValue += 32

        elif charValue >=97 and charValue <= 122:
            charValue -= 32
        finalOutput += chr(charValue)
    return finalOutput


if __name__ == "__main__":
    word = input()
    print(swap_case(word))

