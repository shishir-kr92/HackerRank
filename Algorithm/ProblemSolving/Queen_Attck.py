import math

def check_obstacles(x, y):
    index = 0
    for cor in obs_pos:
        if cor[0] == x and cor[1] == y:
            obs_pos.pop(index)
            return True
        index += 1

    return False


def left_corner_forward(i, j):
    """ left corner forward """
    total_attack_count = 0
    i -= 1
    j -= 1
    while i >= 1 and j >=1:
        if not check_obstacles(i, j):
            total_attack_count += 1
        else:
            break
        i -= 1
        j -= 1

    return total_attack_count


def forward_movement(i, j):
    """ forward movement """
    total_attack_count = 0
    i -= 1
    while i >= 1:
        if not check_obstacles(i, j):
            total_attack_count += 1
        else:
            break
        i -= 1
    return total_attack_count


def right_corner_forward(i, j, board_size):
    """ right corner forward"""
    total_attack_count = 0
    i -= 1
    j += 1

    while i >= 1 and j <= board_size:
        if not check_obstacles(i, j):
            total_attack_count += 1
        else:
            break
        i -= 1
        j += 1
    return total_attack_count


def right_movement(i, j , board_size):
    """ right """
    total_attack_count = 0
    j += 1

    while j <= board_size:
        if not check_obstacles(i, j):
            total_attack_count += 1
        else:
            break

        j += 1
    return total_attack_count


def right_corner_backward(i, j , board_size):
    """ right corner backward """
    total_attack_count = 0
    i += 1
    j += 1

    while i <= board_size and j <= board_size:
        if not check_obstacles(i, j):
            total_attack_count += 1
        else:
            break

        i += 1
        j += 1
    return total_attack_count


def backward_movement(i, j, board_size):
    """ backward """
    total_attack_count = 0
    i += 1

    while i <= board_size:
        if not check_obstacles(i, j):
            total_attack_count += 1
        else:
            break

        i += 1
    return total_attack_count


def left_corner_backward(i, j, board_size):
    """ left corner movement """
    total_attack_count = 0
    i += 1
    j -= 1

    while i <= board_size and j >= 1:
        if not check_obstacles(i, j):
            total_attack_count += 1
        else:
            break
        i += 1
        j -= 1
    return total_attack_count


def left_movement(i, j):
    """ left """
    total_attack_count = 0
    j -= 1

    while j >= 1:
        if not check_obstacles(i, j):
            total_attack_count += 1
        else:
            break
        j -= 1
    return total_attack_count


def queens_attack_old(board_size, queen_x, queen_y):
    i = queen_x
    j = queen_y

    total_attack = left_corner_forward(i, j) + forward_movement(i, j) + right_corner_forward(i, j, board_size) +\
                   right_movement(i, j, board_size) + right_corner_backward(i, j, board_size) +\
                   backward_movement(i, j, board_size) + left_corner_backward(i, j, board_size) + left_movement(i, j)

    return total_attack


def find_no_squares(queen_x, queen_y, pos):
    """ this code find the number of squares between two points"""
    dist = math.sqrt(pow((queen_x - pos[0]), 2) + pow((queen_y - pos[1]), 2))
    print(f"dist {dist}")
    print(math.sqrt(2))
    return (dist/math.sqrt(2)) - math.sqrt(2)


def queens_attack(board_size, queen_x, queen_y, obs_pos):
    no_of_sqr = 0
    if obs_pos:
        for pos in obs_pos:
            no_of_sqr += (find_no_squares(queen_x, queen_y, pos))
    else:
        no_of_sqr = find_no_squares(queen_x, queen_y, [1, 1]) + \
                    find_no_squares(queen_x, queen_y, [1, queen_y]) + \
                    find_no_squares(queen_x, queen_y, [1, board_size]) + \
                    find_no_squares(queen_x, queen_y, [queen_x, board_size]) + \
                    find_no_squares(queen_x, queen_y, [board_size, board_size]) + \
                    find_no_squares(queen_x, queen_y, [board_size, queen_y]) + \
                    find_no_squares(queen_x, queen_y, [board_size, 1]) + \
                    find_no_squares(queen_x, queen_y, [queen_x, 1])
    print(no_of_sqr)


if __name__ == "__main__":
    board_size, obs_count = [int(x) for x in input().split()]
    queen_x, queen_y = [int(x) for x in input().split()]
    obs_pos = []
    for _ in range(obs_count):
        obs_pos.append(list(map(int, input().rstrip().split())))
    queens_attack(board_size, queen_x, queen_y, obs_pos)
