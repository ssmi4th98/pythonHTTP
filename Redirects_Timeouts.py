import requests

resp = requests.get('https://gmail.com')

# to see if there are any redirects, use the history attribute
# you can see the status codes of 30X as redirect calls.

print(resp.history)

# to see the final endpoint url, use the url attribute

print(resp.url)

# write code to iterate through all of the urls in the response:

if resp.history:
    print("Redirect History:")
    for r_url in resp.history:
        print(r_url.status_code, r_url.url, r_url.is_redirect)  #added term is redirect to see intermediate response.

    print('\Final Destination: ')
    print(resp.status_code, resp.url)

else:
    print('Request not redirected.')


print(resp.is_redirect) #This queries the final destination.
print(resp.is_permanent_redirect) #determines if the response is a permanent redirect.

# disable redirect to hit only the first url

resp1 = requests.get('https://google.com',allow_redirects=False)
print(resp1.status_code)
print(resp1.history)
print(resp1.url)

#use head attribute and set the 'redirects' to True it becomes "False"

resp2 = requests.head('https://google.com',allow_redirects=True)
print(resp2.url)
print(resp2.status_code)
print(resp2.history)

#final piece is to check if the timeout function works

# t_repo = requests.get('https://github.com',timeout=0.001)# this reps the time to receive the "first response."

# to examine the time it takes to download a file and the first response:

t_repo1 = requests.get('https://github.com',timeout=(2, 10))
print(t_repo1.status_code)
print(t_repo1)

# to set an unlimited amount of time use 'None' as a timeout value.