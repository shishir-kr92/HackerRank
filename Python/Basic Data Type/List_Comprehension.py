def get_all_possible_combination( X, Y, Z, N ):
    return [[i, j, k]for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i + j +k != N]

def get_combination_forLoop( X, Y, Z, N ):
    output = ""
    for i in range(X+1):
        for j in range(Y+1):
            for k in range(Z+1):
                if i+j+k != N:
                    output += "[%d,%d,%d]," %(i,j,k)
    print(output.strip(","))


if __name__ == "__main__":
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())
    #get_all_possible_combination(X, Y, Z, N)
    get_combination_forLoop(X, Y, Z, N)