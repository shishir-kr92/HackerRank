"""
Count Me
Given an Array  of  integers and  queries. Each query is defined by three integers  ,  and . You need to print the count of numbers which can divide  and lie in index range  to .

Input

First Line: , defining size of array
Second Line:  space separated integers, defining array .

Third Line: , total no of Queries.

Fourth Line:  space separated integers which define .

Fifth Line:  space separated integers which define .

Sixth Line:  space separated integers which define .

Output

Print answers of all queries as space separated integers.

Constraints




Sample Input
5
2 1 5 18 6
5
1 3 2 5 1
5 5 4 5 4
20 36 10 13 5
Sample Output
3 2 2 0 2
Explanation
For First Query, Numbers dividing  in range  to  are  and . So answer is .
"""
def get_factor(num):
    factor = [1, num]
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            factor.append(i)
    return factor

def cnt(arr, X, u_limit, l_limit):
    result_dict = []

    arr = list(arr)
    X = list(X)
    u_limit = list(u_limit)
    l_limit = list(l_limit)

    for i in range(len(X)):
        divisor = 0
        for j in range(l_limit[i] - 1, u_limit[i]):
            if X[i] % arr[j] == 0:
                divisor += 1
        result_dict.append(divisor)
    return list(result_dict)


if __name__ == "__main__":
    """
    """
    size_of_array = int(input().rstrip())
    arr = [int(x) for x in input().rstrip().split()]
    query_count = int(input().rstrip())
    l_limit = [int(x) for x in input().rstrip().split()]
    r_limit = [int(x) for x in input().rstrip().split()]
    X = [int(x) for x in input().rstrip().split()]
    result = cnt(arr, l_limit, r_limit, X)
    print(result)