print('This is calculate income tax')

income = float(input('Please enter the monthly income'))

tax = 0

if income<1500:
    tax = income * 0.03
elif 1500<income<= 4500:
    tax = income * 0.1
elif 4500<income<=9000:
    tax = income * 0.2
elif 9000<income<=35000:
    tax = income*0.25
elif 35000<income<=55000:
    tax= income * 0.3
elif 55000<income<=80000:
    tax= income * 0.35
elif 80000<income:
    tax=income * 0.45
print('your month income tax is ', tax)