import requests
from PIL import Image
from io import BytesIO
import webbrowser
import os

# this is uses Pillow images.

r_get = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Moon_and_Aurora.jpg/320px-Moon_and_Aurora.jpg')

print(r_get.status_code)
print(r_get.headers['content-type'])
print(type(r_get.content))

image = Image.open(BytesIO(r_get.content))
print(type(image))
image.save('aurora.png')  # here we are saving the image as a png file

webbrowser.open(('file://' + os.path.realpath('aurora.png')))