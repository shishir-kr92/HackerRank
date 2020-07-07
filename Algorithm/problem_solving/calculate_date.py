
# MAP
MONTH_DICT = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}

# array
MONTHS_SET = [None, 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG',
              'SEP', 'OCT', 'NOV', 'DEC']

# set
MONTH_LEN = ((0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
             (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))


def is_leap_year(year):
    if ((year % 4 == 0) or (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False


def get_date(current_date, days_to_add):
    date_token = current_date.split("-")
    date = int(date_token[0])
    month = MONTH_DICT[date_token[1].upper()]
    year = int(date_token[2])
    is_leap = is_leap_year(year)


    print(date, MONTHS_SET[month], year)
    while days_to_add > 0:

        date += 1
        if month == 2 and is_leap:
            month_limit = MONTH_LEN[1][month]
        else:
            month_limit = MONTH_LEN[0][month]

        if date > month_limit:
            date = 1
            month += 1

        if month > 12:
            year += 1
            is_leap = is_leap_year(year)
            month = 1

        days_to_add -= 1
        print(date, MONTHS_SET[month], year)
    print(date, MONTHS_SET[month], year)
    return f"{date}-{MONTHS_SET[month]}-{year}"


def main():
    current_date = '31-DEC-2019'
    new_date = get_date(current_date, 365)
    print()
    print(f"new date :- {new_date}")



if __name__ == "__main__":
    main()