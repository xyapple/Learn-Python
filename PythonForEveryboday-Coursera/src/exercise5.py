print('This is calculate income tax')

income = float(input('Please enter the monthly income'))

tax = 0

if income<=1500:
    tax = income * 0.03

elif 1500<income<= 4500:
    tax = (income - 1500) * 0.1 + 1500 * 0.03

elif 4500<income<=9000:
    tax = income - (income - 4500) * 0.2 + 4500 * 0.1 + 1500 * 0.03

elif 9000<income<=35000:
    tax = (income - 9000)*0.25 + 9000*0.2 + 4500 * 0.1 + 1500 * 0.03

elif 35000<income<=55000:
    tax= (income - 35000) * 0.3 + 35000*0.25 + 9000*0.2 + 4500 * 0.1 + 1500 * 0.03
elif 55000<income<=80000:
    tax= (income-55000) * 0.35 + 55000*0.5 + 35000*0.25 + 9000*0.2 + 4500 * 0.1 + 1500 * 0.03
elif 80000<income:
    tax=(income-80000) * 0.45 + 80000*0.35 + 55000*0.5 + 35000*0.25 + 9000*0.2 + 4500 * 0.1 + 1500 * 0.03
print('your month income tax is ', tax)