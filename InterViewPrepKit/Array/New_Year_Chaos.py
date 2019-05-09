

def min_bribe(queue_state):
    bribe_count = 0
    queue_length = len(queue_state)
    for i in range(queue_length-1, -1, -1):
        temp = queue_state[i]
        j = i + 1
        jump_count = 0
        index  = i

        while j < queue_length and temp > queue_state[j] :
            queue_state[j - 1] = queue_state[j]
            index = j
            jump_count += 1
            j += 1
            # print(jump_count, queue_state)

        if jump_count <= 2:
                bribe_count += jump_count
                queue_state[index] = temp
        else:
                print("Too chaotic")
                return 0

    print(bribe_count)


def min_bribe_old(queue_state):
    bribe_count = 0
    queue_length = len(queue_state)
    for i in range(queue_length-1, -1, -1):
        temp = queue_state[i]
        j = i + 1
        jump_count = 0
        index  = i
        #if i + 1 != queue_state[i]:

        while j < queue_length:
            if temp > queue_state[j]:
                queue_state[j - 1] = queue_state[j]
                index = j
                jump_count += 1
            j += 1
            # print(jump_count, queue_state)

        if jump_count <= 2:
                bribe_count += jump_count
                queue_state[index] = temp
        else:
                print("Too chaotic")
                return 0

    print(bribe_count)


if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays
    """
    test_case = int(input().rstrip())
    while test_case > 0:
        size_of_queue = int(input().rstrip())
        queue_final_state = [int(x) for x in input().rstrip().split()]
        min_bribe(queue_final_state)
        test_case -= 1