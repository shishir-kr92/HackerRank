def count_word(word):
    result = 0
    for i in range(len(word)):
        print(word[i], ord(word[i]), result)
        if i == 0:
            result += 1

        elif ord(word[i]) >=65 and ord(word[i])  <= 90:
            result +=1
        else:
            pass
            #print(result)
    return result

word = input()
print(count_word(word))



