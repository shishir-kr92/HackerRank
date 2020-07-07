class Area:
    def __init__(self, a, b):
        if type(a) is str and type(b) is str:
            self.a = int(a.strip())
            self.b = int(b.strip())
        else:
            self.a = a
            self.b = b


def getSurvivalTime_rec(A, B, X, Y,  Z, time, loc):
    if A <=0 or B <= 0:
        return time

    time = time+1
    if loc == 0:
        # i am at X area sp check for Y abd Z
        return max(getSurvivalTime_rec(A+ Y.a, B + Y.b, X, Y, Z, time, 1),
                   getSurvivalTime_rec(A + Z.a, B + Z.b, X, Y, Z, time, 2))

    if loc == 1:
        # i am at X area sp check for Y abd Z
        return max(getSurvivalTime_rec(A+ X.a, B + X.b, X, Y, Z, time, 0),
                   getSurvivalTime_rec(A + Z.a, B + Z.b, X, Y, Z, time, 2))

    if loc == 2:
        # i am at X area sp check for Y abd Z
        return max(getSurvivalTime_rec(A+ X.a, B + X.b, X, Y, Z, time, 0),
                   getSurvivalTime_rec(A + Y.a, B + Y.b, X, Y, Z, time, 1))


def getMaxSurvivalTime_recurcive(X, Y, Z, A, B, isRecurcive = True):
    if A <=0 or B<=0:
        return 0

    if isRecurcive:
        time = 0

        a = getSurvivalTime_rec(A+ X.a, B + X.b, X, Y, Z, time, 0)
        b = getSurvivalTime_rec(A + Y.a, B + Y.b, X, Y, Z, time, 1)
        c = getSurvivalTime_rec(A + Z.a, B + Z.b, X, Y, Z, time, 2)

    #print("{}, {}, {} ".format(a, b, c))

    return max(a, b, c)


if __name__ == "__main__":
    '''
        https://www.geeksforgeeks.org/game-theory-choice-area/
    '''
    # temp = input().split()
    # X = Area(temp[0], temp[1])
    #
    # temp = input().split()
    # Y = Area(temp[0], temp[1])
    #
    # temp = input().split()
    # Z = Area(temp[0], temp[1])
    #
    # A = int(input())
    # B = int(input())
    X = Area(3, 2)
    Y = Area(-5, -10)
    Z = Area(-20, 5)

    A = 20
    B = 8
    print(getMaxSurvivalTime_recurcive(X, Y, Z, A, B))

