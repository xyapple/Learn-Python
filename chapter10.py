'''
d = {'a':10, 'b': 1, 'c':22}
d.items()
t = sorted(d.items())
t
for k,v in sorted(d.items()):
    print(k, v)

c = {'a':101, 'b': 111, 'c':220}
tmp = list()
for key, value in c.items():
    tmp.append((value, key))
print(tmp)
tmp_reverse= tmp.sort(reverse = True)
print('After sorted:', tmp_reverse)

'''
fh = open('romeo.txt')
#create a dictonary and count each word
counts = dict()
for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
    print (counts)

#
lst = list()
for key, val in counts.items():
    lst.append((val, key))
print(lst)
lst.sort(reverse=True)

for val, key in lst[:10]:
    print(key, val)
