
time = ["o' clock",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "quarter",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine",
        "half"
        ]


def time_in_word(hrs, minute):
    time_str_format = ""
    hrs_part = (12 - hrs + 1) if hrs == 12 else (hrs + 1)
    if minute == 0:
        time_str_format = f"{time[hrs]} o' clock"
    elif minute == 1:
        time_str_format = f"{time[minute]} minute past {time[hrs]}"
    elif minute == 15 or minute == 30:
        time_str_format = f"{time[minute]} past {time[hrs]}"
    elif minute < 30:
        time_str_format = f"{time[minute]} minutes past {time[hrs]}"
    elif minute == 45:
        time_str_format = f"{time[60 - minute ]} to {time[hrs_part]}"
    elif minute < 59:
        time_str_format = f"{time[60 - minute ]} minutes to {time[hrs_part]}"
    elif minute == 59:
        time_str_format = f"{time[60 - minute ]} minute to {time[hrs_part]}"
    return time_str_format



if __name__ == "__main__":
    """
        https://www.hackerrank.com/challenges/the-time-in-words/problem
    """
    hrs = int(input().strip())
    minute = int(input().strip())
    result = time_in_word(hrs, minute)
    print(result)
