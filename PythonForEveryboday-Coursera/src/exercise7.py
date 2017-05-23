import datetime

# year = int(input('please enter a year'))
# month = int(input('please enter a month'))
# day = int(input('please enter a day'))
#
# date = datetime.date(year, month, day)
while True:
    try:
        date_entry = input('Enter a date in YYYY-MM-DD format')
        year, month, day = map(int, date_entry.split('-'))
        date1 = datetime.date(year, month, day)
    except ValueError:
        print ('Incorrect format, please try again')

        continue
    else:
        print(date1.strftime('%j'))