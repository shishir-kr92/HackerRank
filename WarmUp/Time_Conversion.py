
def timeConversion(timeStamp):
    time = str(timeStamp[0:-2]).split(":")
    min = time[1]
    hrs = time[0]
    sec = time[2]
    prefix = str(timeStamp[-2:])

    if prefix == "AM":
        if hrs == "12":



    if hrs == 12 and prefix == "AM":
        return "00:" + str(min) + ":" + str(sec)
    elif hrs == 12 and prefix == "PM":
        return "12:" + str(min) + ":" + str(sec)
    elif hrs > 12 and prefix == "PM":
        str(hrs + 12) + ":" + str(min) + ":" + str(sec)



if __name__== '__main__':
    timeStamp = "12:59:00AM"
    result = timeConversion(timeStamp)
    print(result)