import urllib.request as url
from bs4 import BeautifulSoup
# url_in = input('Enter --')
# http://python-data.dr-chuck.net/comments_363696.html
# http://python-data.dr-chuck.net/comments_42.html
html = url.urlopen(' http://python-data.dr-chuck.net/comments_363696.html').read()

soup = BeautifulSoup(html,'html.parser')

# Retrieve all of the numbers
spans = soup('span')
total = 0
for span in spans:
    span = int(span.contents[0])
    total = total + span
print(total)
    #Look for the parts of a span
    # print('span:', span)
    # print ('URL:',span.get('class', None))
    # print ('Contents:',span.contents[0])
    # print ('Attrs:',span.attrs)
