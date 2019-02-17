def split_and_join(string):
    newString = ""
    for char in string:
        if ord(char) == 32:
            newString += "-"
        else:
            newString += char
    return newString


if __name__ == '__main__':
    word = input()
    print(split_and_join(word))

