
def get_character_dict(word):
    char_dict = {}
    for c in word:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def check_common_substring(string_one, string_two):
    reference_dict = {}
    search_string = ""

    if len(string_one) > len(string_two):
        reference_dict = get_character_dict(string_one)
        search_string = string_two
    else:
        reference_dict = get_character_dict(string_two)
        search_string = string_one

    for  c in search_string:
        if c in reference_dict:
            return "YES"
    return "NO"

if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
    """
    test_case = int(input().rstrip())
    while test_case:
        string_one = input().rstrip()
        string_two = input().rstrip()
        result = check_common_substring(string_one, string_two)
        print(result)
        test_case -= 1