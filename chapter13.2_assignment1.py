'''
Extracting Data from json
This is not a simple assignment due to the version python3.5 

'''

import urllib.request
import json

# http://python-data.dr-chuck.net/comments_42.json
# http://python-data.dr-chuck.net/comments_363697.json

link = 'http://python-data.dr-chuck.net/comments_363697.json'
req = urllib.request.Request(link)

##parsing response
data = urllib.request.urlopen(req).read()
info = json.loads(data.decode('utf-8'))
# print(info)
comment = info['comments']
lst = list()

##parcing json
for item in comment:
    lst.append(item['count'])

print('Count: {0}'.format(len(lst)))
print('Sum: {0}'.format(sum(lst)))