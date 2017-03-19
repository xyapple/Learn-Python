'''
9.4 Write a program to read through the mbox-short.txt and figure out 
who has the sent the greatest number of mail messages. The program looks 
for 'From ' lines and takes the second word of those lines as the person 
who sent the mail. The program creates a Python dictionary that maps the 
sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using 
a maximum loop to find the most prolific committer.

'''
fh = open('mbox-short.txt')

dics = {}
for line in fh:
    if not line.startswith('From:'):
        continue
    line = line.rstrip().split()
    line = line[1]
    dics[line] = dics.get(line, 0) + 1


most_count = None
most_word = None

for word, dic in dics.items():
    if most_count == None or dic > most_word:
        most_count = word
        most_word = dic
print(most_count, most_word, dics)