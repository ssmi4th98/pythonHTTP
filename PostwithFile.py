import requests
from pprint import pprint
import webbrowser

url = 'http://httpbin.org/post'

files = {'files': open('text.txt','rb')}    #'rb' is read or open without truncation.
values = {'upload_file': 'text.txt', 'OUT':'csv'}

# make the post request

r_post = requests.post(url,files=files,data=values)

print(r_post.status_code)

# response body

pprint(r_post.text)