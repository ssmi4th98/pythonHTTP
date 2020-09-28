import requests
from pprint import pprint

resp_obj = requests.get('http://httpbin.org/')
print(resp_obj.status_code)

print(resp_obj.encoding)

resp_obj.encoding = 'ISO 1859-1'  #here encoding is configurable

print(resp_obj.encoding)

#encoding impacts data format, e.g.:

resp_git = requests.get('https://github.com/timeline.json')
print(resp_git.status_code)

print(resp_git.text)
#we'll change the encodeing of the response and look at the "'" in you're and didn't
resp_git.encoding = 'ISO 1859-1'
print(resp_git.encoding)
print(resp_git.text)

