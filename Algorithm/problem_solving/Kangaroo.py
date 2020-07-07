
"""
    x_a = a_i + d*a_jump
    x_b = b_i + d*b_jump
    suppose at time t both are at same position
    x_a = x_b
    a_i + t*a_jump = b_i  + t*b_jump
    t(a_jump - b_jump) = b_i - a_i
    t = (b_i - a_i)/(a_jump - b_jump)

    a_i, a_jump, b_i, b_jump
    0, 3, 4, 2
    t = (4-0)/(3-2) = 4

    0, 6, 5, 3
    t = (5 - 0)/(6-3) = 5/3
"""

def does_kangaroo_meet(x1, v1, x2, v2):
    if x1 == x2 and v1 == v2:
        return "YES"
    elif x1 == x2 and v1 != v2:
        return "NO"
    elif x1 != x2 and v1 == v2:
        return "NO"
    else:
        time = (x2 - x1)/(v1 - v2)
        check_condition = (x2 - x1)%(v1 - v2)

        if time >= 0 and check_condition == 0:
            return "YES"
        else:
            return "NO"

if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/kangaroo/problem
    """
    x1, v1 = map(int, input().strip().split())
    x2, v2 = map(int, input().strip().split())
    result = does_kangaroo_meet(x1, v1, x2, v2)
    print(result)
