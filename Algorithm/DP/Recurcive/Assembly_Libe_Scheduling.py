
def car_assembly_time(a, t, e, x, i, j):
    if j == 0:
        return e[i] + a[i][j]

    if j == len(a[0]):
        m = car_assembly_time(a, t, e, x, 0, j - 1)
        n = car_assembly_time(a, t, e, x, 1, j - 1)
        print(m,n)
        return min(m + x[0],
                    n + x[1])

    else:
        if i == 0:
            return  min(car_assembly_time(a, t, e, x, 0, j - 1) + a[0][j],
                        car_assembly_time(a, t, e, x, 1, j - 1) + a[0][j] + t[1][j])
        if i == 1:
            return min(car_assembly_time(a, t, e, x, 1, j - 1) + a[1][j],
                       car_assembly_time(a, t, e, x, 0, j - 1) + a[1][j] + t[0][j])




if __name__ == "__main__":
    a =  [[4, 5, 3, 2],
          [2, 10, 1, 4]]
    t = [[0, 7, 4, 5],
         [0, 9, 2, 8]]
    e = [10, 12]
    x = [18, 7]
    print(a[0][-1])
    result = car_assembly_time(a, t, e, x, 1, len(a[0]))
    print(result)

