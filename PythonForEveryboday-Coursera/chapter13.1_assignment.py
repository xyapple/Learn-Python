import urllib.request as url
import xml.etree.ElementTree as ET

# http://python-data.dr-chuck.net/comments_42.xml
# http://python-data.dr-chuck.net/comments_363693.xml 
link = 'http://python-data.dr-chuck.net/comments_363693.xml'

total = 0
count = 0

# Retrieve all of the numbers


data = url.urlopen(link).read()
print('Retrieved:', len(data), 'characters')
tree = ET.fromstring(data)
result = tree.findall('./comments/comment')
for i in result:
    num = int(i.find('count').text)
    count = count + 1
    total = total + num

print('sum: ', total)
print('count: ', count)