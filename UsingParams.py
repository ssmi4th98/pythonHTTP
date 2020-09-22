import requests
import webbrowser

url = "https://wikipedia.org"

resp_obj = requests.get(url)

print(resp_obj.url)

#  webbrowser.open(resp_obj.url)  #opens up a browser to the url

search_term = input("Enter the term you want to search for: ")

endpoint = "https://www.youtube.com/search"
param = {'q' : search_term}

r_get = requests.get(url = endpoint, params=param)

print(r_get.status_code)

print(r_get.url)  # this returns the response url

#open up a web browser to see results

webbrowser.open(r_get.url)
