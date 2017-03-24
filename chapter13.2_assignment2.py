'''
Using the GeoJSON API
python version 3.5
'''
import urllib.request
import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Please Enter location:')
    # South Federal University
    if len(address)<1:
        break
    url = serviceurl + urllib.parse.urlencode({'sensor':'false','address':address})
    print('retrieving: ', url)

    req = urllib.request.Request(url)
    data = urllib.request.urlopen(req).read()
    print('retrived:', len(data), 'characters')

    try:
        info = json.loads(data.decode('utf-8'))
    except:
        info = None
    # if 'status' not in info or info['status'] != 'OK':
    #     print ('==== Failure To Retrieve ====')
    # # print (data)
    # continue
    # print(json.dumps(info, indent = 4, sort_keys=True))
    place_id = info['results'][0]['place_id']
    print('Place id',place_id)



  


