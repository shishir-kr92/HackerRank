# number of character
d = 256


def count_substring(text, pattern):
    pattern_length  = len(pattern)
    text_length = len(line)
    occurance = 0

    if pattern_length > text_length:
        return 0

    '''for i in range(text_length - pattern_length + 1):
        if line[i:i+pattern_length] == pattern:
            occurance += 1'''
    for i in range(text_length - pattern_length + 1):
        pattern_found = True

        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                pattern_found = False
        if pattern_found :
            occurance += 1
    return occurance


# q is a prime number
# rabin karp algo
def count_substring(text, pattern, q=101):
    M = len(pattern)
    N = len(text)

    pattern_hash = 0
    text_hash = 0
    h = 1
    count = 0

    # value of h should be pow(d, M-1)*q
    for i in range(M):
        h = (h*d) % q

    for i in range(M):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    for i in range(N - M + 1):
        matched = False
        print(pattern_hash, text[i:i+M], text_hash)
        if pattern_hash == text_hash:
            for j in range(M):
                if text[i+j] != pattern[j]:
                    matched = False
                    print("not matched, ", text[i:i+j])
                    break
                matched = True

        if matched:
            print("matched" , text[i:i+M] )
            count += 1

        if i < N-M:
            text_hash = (d*(text_hash - ord(text[i])*h) + ord(text[i+M]))%q

            if text_hash< 0 :
                text_hash = text_hash + q

    return count

if __name__ == "__main__":
    line = input()
    pattern = input()
    # print(count_substring(line, pattern))
    print(count_substring(line, pattern, 101))
