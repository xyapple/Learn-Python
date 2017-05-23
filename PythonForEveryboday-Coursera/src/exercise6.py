year = 0

dollar = 10000

while dollar < 30000:
        year += 1
        dollar = dollar * (1 + 0.02) **year

print(str(year) + ' yearly saving will be reaching 30000')