


def breaking_records(scores):
    min_record = scores[0]
    max_record = scores[0]
    min_record_break = 0
    max_record_break = 0
    for i in range(1, len(scores)):
        if scores[i] < min_record :
            print(min_record)
            min_record = scores[i]
            min_record_break += 1
        if scores[i] > max_record:
            max_record = scores[i]
            max_record_break += 1
    return (max_record_break, min_record_break)



if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().split()))

    print(breaking_records(scores))