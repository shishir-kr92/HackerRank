
def timeConversion(timeStamp):
    time = timeStamp[0:len(timeStamp)-2].split(":")
    hrs = int(time[0])
    converted_time = ""
    prefix = str(timeStamp[-2:])

    if prefix == "AM" and hrs != 12:
        converted_time = time[0] + ":" + time[1] + ":" + time[2]
    elif prefix == "AM" and hrs == 12:
        converted_time = "00" + ":" + time[1] + ":" + time[2]
    elif prefix == "PM" and hrs == 12:
        converted_time = "12" + ":" + time[1] + ":" + time[2]
    elif prefix == "PM" and hrs != 12:
        hrs += 12
        converted_time = str(hrs) + ":" + time[1] + ":" + time[2]

    return converted_time


if __name__== '__main__':
    timeStamp = "11:59:00PM"
    result = timeConversion(timeStamp)
    print(result)