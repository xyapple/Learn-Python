'''
10.2 Write a program to read through the mbox-short.txt and figure out 
the distribution by hour of the day for each of the messages. You can pull
 the hour out from the 'From ' line by finding the time and then splitting 
 the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, 
sorted by hour as shown below.

'''
# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)

fh = open('mbox-short.txt')
dics = dict()
lst = list()
for line in fh:
    if not line.startswith('From '):
        continue
    line = line.split()
    position = line[5]
    time = position[0:2]
    dics[time] = dics.get(time, 0) + 1
    # print(dics)

for k, v in dics.items():
    lst.append((k, v))
# print(lst)

lst.sort(reverse=False)
for k, v in lst[0:20]:
    print(k, v)