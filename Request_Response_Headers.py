import requests
from pprint import pprint

url = 'http://swapi.dev/api/people/3'
#specifiy the header field by creating a dictionary

headers = {'user-agent':'Googlechrome'}  # this specifies the app
resp = requests.get(url,headers=headers)  # here you pass the url and a value for headers
pprint(resp.headers)

pprint(resp.headers['Content-Type']) # call this as a list

resp_obj = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
pprint(resp_obj.headers['content-type'])

# to see what was set by default when the get request was made use a request.headers

pprint(resp_obj.request.headers)

#with the above, the user-agent is set to the python app being used with the same version.
# If you want to see what the response looks like in another format, set the user-agent header:

r = requests.get('http://httpbin.org/user-agent', headers= {'User-Agent' : 'Internet Explorer/2.0'})
pprint(r.request.headers)

# you can return data using the r.json function which only return value if the response is in json format

data = r.json()

pprint(data['user-agent'])  #this calls out the field for user-agent in the response header.


