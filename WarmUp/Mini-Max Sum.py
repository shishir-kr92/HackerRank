def sort_list(numlist):
    for i in range(len(numlist)):
        for j in  range(len(numlist)-i-1):
            if(numlist[j] > numlist[j+1]):
                temp = numlist[j]
                numlist[j] = numlist[j+1]
                numlist[j+1] = temp


def min_sum(numlist):
    return numlist[0] + numlist[1] + numlist[2] + numlist[3]



def max_sum(numlist):
    return  numlist[1] + numlist[2] + numlist[3] + numlist[4]


if __name__ == '__main__':
    numlist = list(map(int, input().rstrip().split(" ")))
    sort_list(numlist)
    print(min_sum(numlist), max_sum(numlist))

