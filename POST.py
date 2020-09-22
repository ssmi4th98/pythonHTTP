import requests
from pprint import pprint
import webbrowser
import os

company = input("Name of site to search in wikipedia: ")

r_post = requests.post('https://en.wikipedia.org/w/index.php',data = {'search': company})

print(r_post.status_code)

print(type(r_post))

## print(pprint(r_post.text))

with open(company+'.html','wb') as f:
    for chunk in r_post.iter_content(chunk_size=10000):
        f.write(chunk)

webbrowser.open('file://' + os.path.realpath(company + '.html'))
