import time


def form(tim):
    minu = tim//60
    sec = tim % 60
    return str(minu)+":"+str(+sec)


raw = input("How long?[Min:Sec] ")
startTime = int(time.time())
[minute, second] = raw.split(":")

timerTime = int(minute) * 60 + int(second)
endTime = startTime + timerTime
while endTime > time.time():
    print(form(endTime - int(time.time())))

print("Timer ended")
