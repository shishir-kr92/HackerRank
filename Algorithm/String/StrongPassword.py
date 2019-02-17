def minimumNumber(n, password):
    missing = 0
    isCorrect = True
    condition = {
              "hasDigit": False,
              "hasLowerCase": False,
              "hasUpperCase": False,
              "hasSpecialChar": False}


    for c in password:

        if c in "!@#$%^&*()-+":
            condition['hasSpecialChar'] = True

        elif ord(c) >=65 and ord(c)  <= 90:
            condition['hasUpperCase'] = True

        elif ord(c) >= 97 and ord(c)  <= 122:
            condition['hasLowerCase'] = True

        elif ord(c) >= 48 and ord(c)  <= 57:
            condition['hasDigit'] = True

    for key in condition.keys():
        if condition[key] == False:
            missing += 1
            n += 1
    #print(condition)
    if n >= 6:
        return missing
    else:
        return (6 - n) + missing


n = int(input().strip())
password = input().strip()
print(minimumNumber(n, password))







