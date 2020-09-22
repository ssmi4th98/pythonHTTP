import requests
from pprint import pprint
import webbrowser

post_url = "http://pastebin.com/api/api_post.php"

payload = {'username': 'steve', 'email': 'steve@email.com'}

api_key = 'Ff_GoTpEqXfl25ylWqJ-cluZ8MGSEK6y'

parameters = {'api_dev_key':api_key,
              'api_option':'paste',
              'api_paste_code':payload,
              'api_paste_format':'python'}

r_post=requests.post(post_url,data=parameters)

if (r_post.status_code == 200):
    print("This was a sucessful post")
    print("You can find the link at {}.".format(r_post.text))
else:
    print("Post failed")

