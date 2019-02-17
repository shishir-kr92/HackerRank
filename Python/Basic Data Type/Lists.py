if __name__ == '__main__':
    N = int(input())
    List = []
    for _ in range(N):
        command, *value = input().strip().split()
        value = list(map(int, value ))

        head = 0

        if command == "insert":
            List.insert(value[0], value[1])

        elif command == "append":
            List.append(value[0])

        elif command == "remove":
            List.remove(value[0])

        elif command == "print":
            print(List)

        elif command == "sort":
            List.sort()

        elif command == "pop":
            List.pop()

        elif command == "reverse":
            List.reverse()