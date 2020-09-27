import requests
from pprint import pprint
import json


# a put overwrites a value, if it exists, where a post does not. See: restfulapi.net/rest-put-vs-post
# this is used as a "setter" value to set the value of an original value

# general format of put: r_put = requests.put('http://httpbin.org/put',data={'key':'value'})

r_put = requests.put('http://httpbin.org/put',data={'key':'value'})

print(r_put.status_code)

print(r_put.text)

r_option = requests.options('http://httpbin.org/get')
print(r_option.text)
pprint(r_option.headers)

r_delete = requests.delete('http://httpbin.org/delete')
pprint(r_delete.status_code)
pprint(r_delete.text)
pprint(r_delete.headers)



