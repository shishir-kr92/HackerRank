

def get_frequency_query(queries):
    result = {}
    frequency = {}
    freq_counter = []
    for query in queries:
        ops = query[0]
        num = query[1]
        freq = 0

        if ops == 1:
            if num in result:
                result[num] += 1
                freq = result[num]
            else:
                result[num] = 1
                freq = 1

            if freq in frequency:
                frequency[freq] += 1
                if (freq  - 1) in frequency:
                    frequency[freq - 1] -= 1
            else:
                frequency[freq] = 1
        elif ops == 2:
            if ops in result:
                result[num] -= 1
                freq = result[num]

                if freq in frequency:
                    frequency[freq] += 1

                if (freq + 1) in frequency:
                    frequency[freq + 1] -= 1
        elif ops == 3:
            if num not in frequency or frequency[num] < 0:
                freq_counter.append(0)
            else:
                freq_counter.append(1)
    return freq_counter



if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps
    """

    no_of_query = int(input())
    queries = []
    for i in range(no_of_query):
        queries.append([int(i) for i in input().rstrip().split()])
    print(queries)
    result = get_frequency_query(queries)
    print(result)
