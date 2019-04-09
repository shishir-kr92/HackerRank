

def get_fruits_count_in_house(start_point, end_point, apple_pos, orange_pos,
                              fallen_apple_pos, fallen_orange_pos):

    check_conditon = lambda x: x >= start_point and x <= end_point
    fallen_apple_cor = [i + apple_pos for i in fallen_apple_pos if check_conditon(i + apple_pos)]
    fallen_orange_cor = [i+ orange_pos for i in fallen_orange_pos if check_conditon(i + orange_pos)]
    print(len(fallen_apple_cor))
    print(len(fallen_orange_cor))

if __name__ == "__main__":
    '''
        https://www.hackerrank.com/challenges/apple-and-orange/problem
    '''
    start_point, end_point = [ int(x) for x in input().split()]
    apple_pos, orange_pos = [ int(x) for x in input().split()]
    apple_count, orange_count = [ int(x) for x in input().split()]
    fallen_apple_pos = [ int(x) for x in input().split()]
    fallen_orange_pos = [ int(x) for x in input().split()]
    get_fruits_count_in_house(start_point, end_point, apple_pos, orange_pos,
                              fallen_apple_pos, fallen_orange_pos)

