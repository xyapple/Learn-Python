import re

sum = 0
fh = open('regex_sum_363691.txt').read()

numbers = re.findall("[0-9]+", fh)
for num in numbers:
    num = int(num)
    sum = sum + num
print(sum)