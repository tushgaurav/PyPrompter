import time

def currentTime(format=12, hour=True, minutes=True, seconds=True):
    format = ""
    if hour and format==12:
        format = "%I"
    elif hour and format==24:
        format = "%H"
    else:
        format = ""

    if minutes:
        format = format + ":%M"
    if seconds:
        format = format + ":%S"

    time_string = time.strftime(format, time.localtime())

    return [time_string, 0]
