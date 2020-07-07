
def car_assembly_time_recurcive(a, t, e, x):
    NUM_STATION = len(a[0])
    T1 = [0 for i in range(NUM_STATION)]
    T2 = [0 for i in range(NUM_STATION)]

    T1[0] = a[0][0] + e[0]
    T2[0] = a[1][0] + e[1]

    for i in range(1, NUM_STATION):
        T1[i] = min(T1[i-1] + a[0][i], T2[i-1] + a[0][i] + t[1][i])
        T2[i] = min(T2[i - 1] + a[1][i], T1[i - 1] + a[1][i] + t[0][i])
        #print(T1[i], T2[i])

    return min( T1[-1] + x[0], T2[-1] + x[1])




if __name__ == "__main__":
    a =  [[4, 5, 3, 2],
          [2, 10, 1, 4]]
    t = [[0, 7, 4, 5],
         [0, 9, 2, 8]]
    e = [10, 12]
    x = [18, 7]
    result = car_assembly_time_recurcive(a, t, e, x)
    print(result)

