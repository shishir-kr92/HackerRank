
def count_valley(no_of_steps, steps):
    in_valley = False

    valley_count = 0
    temp_step = 0

    for step in steps:
        if step == 'D':
            temp_step -= 1
        else:
            temp_step += 1
        if temp_step < 0:
            in_valley = True

        if in_valley and temp_step ==0:
            valley_count +=1
            in_valley = False
        #print(step, temp_step, in_valley)
    return valley_count


if __name__ == "__main__":
        """
            https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
        """
        no_of_steps = int(input().rstrip())
        steps = input()
        result  = count_valley(no_of_steps, steps)
        print(result)