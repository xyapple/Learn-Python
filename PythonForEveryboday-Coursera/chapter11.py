'''
Regular Expression
fh = open('mbox-short.txt')
for line in fh:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
'''
# import Expression
import re
'''
fh = open('mbox-short.txt')
for line in fh:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
'''
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2010'

# One way to do it
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos + 1 : sppos]
print (host)

# Second way to do it -- double split
data1 = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2010'
words = data1.split()
email = words[1]
posi = email.split('@')
print(posi[1])

# Third way to do it Regular Expression
data2 = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2010'
z = re.findall('@([^ ]*)', data2)
print(z)
