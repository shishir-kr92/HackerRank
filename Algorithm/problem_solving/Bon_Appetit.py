
def bon_appetit(bill, k, b_charged):
    b_total = 0
    b_actual = 0
    for i in bill:
        b_total += i

    b_actual = (b_total - bill[k])/2
    if b_actual == b_charged:
        print("Bon Appetit")
    else:
        print(int(b_charged - b_actual))



if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/bon-appetit/problem
    """
    n, k = map(int, input().strip().split())
    bill = list(map(int, input().strip().split()))
    b_charged = int(input().strip().split())
    result = bon_appetit(bill, k, b)
    print(result)
