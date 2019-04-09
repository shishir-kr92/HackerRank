
def remove_duplicate(word):
    char_list = [-1 for i in range(24)]
    final_result = ""
    for c in word:
        index = 97 - ord(c)
        char_list[index] += 1

    for c in word:
        index = 97 - ord(c)
        if char_list[index] != -1:
            final_result += c
            char_list[index] = -1
    return final_result


if __name__ == "__main__":
    word = input()
    print(remove_duplicate(word))
