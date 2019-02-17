if __name__ == "__main__":
    n = int(input().strip())
    numList = map(int, input().split())
    numList = tuple(numList)
    print(hash(numList))