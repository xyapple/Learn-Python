import datetime

# def add_time(userH, userM, userS, hour, min, sec):
userH = int(input('enter a hour'))
userM = int(input('enter a minute'))
userS = int(input('enter a second'))
userTime = datetime.time(userH, userM, userS)
print(userTime)

sec = userS + 30
mic = userM +9
if sec >= 60:
    sec = sec - 60
    mic1 = mic + 1
    if mic1 >= 60:
        mic = mic1 - 60
        userH = userH + 1
        if userH >=24:
            userH = userH - 24

addTime = datetime.time(userH, mic, sec)
print(addTime)





