import time


def forma(tim):
    minutes = tim // 60
    seconds = tim % 60

    return str(minutes)+":"+str(seconds)


sec = int(input("Enter the time in number of seconds: "))
time_remaining = sec
while time_remaining > 0:
    print(forma(time_remaining), end="\r")
    time.sleep(1)
    time_remaining -= 1

print("Times up!")
