'''
JavaScript Object Notation
it turns out that the one of the things that JSON has as its
 best advantage, is the fact that inside Python, we tend to 
 make lists and dictionaries. And in JavaScript, we tend to make 
 arrays and HashMaps. And JSON is a great way to represent both 
 of those structures. If you think of the goal of, one language has some data in it. We need 
 to serialize it, send it to another language, deserialize it, 
 pull it out to another language. Why not come up with a format 
 that's most natural between those, okay? And so, the syntax 
 again will seem familiar to you, 

Things that we get back is dictionary format

Service Oriented Approach: allows an app to be broken into parts and distributed across a network
Accessiong APIs in Python: API(application program interface)
SOAP(simple object access protocol)-- this is overly complex and should be updated.
REST(representational state transfer):
    create, read, update, and delete remotely
OAuth -- many companies use it for securaty 

'''
import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print ('Name:',info["name"])
print ('Hide:',info["email"]["hide"])