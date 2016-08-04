import datetime

year = int(input('please enter a year'))
month = int(input('please enter a month'))
day = int(input('please enter a day'))

date = datetime.date(year, month, day)

print(date.strftime('%j'))