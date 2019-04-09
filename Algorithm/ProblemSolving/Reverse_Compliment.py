def main():
    dnaString = input()
    for index in range(len(dnaString) - 1, -1, -1):
        if dnaString[index] == 'A':
            print('T', end="")
        elif dnaString[index] == 'T':
            print('A', end="")
        elif dnaString[index] == 'C':
            print('G', end="")
        elif dnaString[index] == 'G':
            print('C', end="")


main()