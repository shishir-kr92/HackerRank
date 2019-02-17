studentDetails ={}

def find_percentage(key):
    marksList = studentDetails.get(key)
    print(marksList)
    sum = 0
    count = len(marksList)
    for mark in marksList:
        sum += mark
    return float(sum/(100*count))*100

def save_details(detail):
    key = ""
    value = []
    detailToken = detail.split(' ')
    for i in range(len(detailToken)):
        if i == 0:
            key = detailToken[i].strip()
        else:
            value.append(int(detailToken[i].strip()))
        studentDetails[key] = value


if __name__=="__main__":
    n = int(input())
    for _ in range(n):
        name, *line = input().split()
        score = list(map(float, line))
        studentDetails[name] = score

    name  = input()
    print("%0.2f" %find_percentage(name))
