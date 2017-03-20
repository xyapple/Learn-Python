import urllib.request as url
from bs4 import BeautifulSoup
# url_in = input('Enter --')
# http://python-data.dr-chuck.net/known_by_Fikret.html 
# http://python-data.dr-chuck.net/known_by_Daniela.html

count = int(input('Enter count '))
position = int(input('Enter position: '))
lst = list()
link = 'http://python-data.dr-chuck.net/known_by_Daniela.html'
# Retrieve all of the numbers
while count > 0:
    
    html = url.urlopen(link).read()
    soup = BeautifulSoup(html,'html.parser')
    tag = soup('a')
    count = count - 1
    x = tag[position - 1].string
    lst.append(x)
    link = tag[position - 1 ]['href']
    print ("retrieving: {0}".format(link))
        
print('answer: ', lst[-1])



        
