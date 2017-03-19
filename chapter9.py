'''
# create a dictionary
bag = dict()
bag['money'] = 200
bag['candy'] = 3
print(bag)
bag['tissues'] = 'I donot have it'
bag['candy'] = bag['candy'] + 2
print(bag)
print(type(bag['money']))

# create a dictionary another way
fruits = {'apple':2,
         'pear':5,
         'orange':10}
print(fruits)
'''

# count something in dict Like the get method
counts = dict()
names = ['larry','tom','jane','gen','jerry','jane','tom','jane']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# count items with get()

counts = dict()
names = ['larry','tom','jane','gen','jerry','jane','tom','jane']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
print('keys', counts.keys())
print('values', counts.values())
for name, count in counts.items():
    print(name, count)

'''
# count the most common word 
dic = dict()
line = input('Enter a line of text: ')

words = line.split()
print('Words:', words)

print('Counting...')

for word in words:
    dic[word] = dic.get(word, 0) + 1
print('Counts', dic)
'''

fruits = {'apple':2,
         'pear':5,
         'orange':10,
         'banana':25,
         'pineapple':1}
for key in fruits:
    print(key, fruits[key])
