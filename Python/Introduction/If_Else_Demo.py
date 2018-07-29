if __name__ == '__main__':
    result = ""
    n = int(input().strip())
    if n % 2 == 0 :
        if n >=2 and n <=5 :
            result = "Not Weird"
        elif n >= 6 and n <= 20 :
            result = "Weird"
        elif n >21:
            result = "Not Weird"

    else:
        result = "Weird"
    print(result)


