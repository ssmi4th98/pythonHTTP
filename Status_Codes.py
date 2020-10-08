import requests
from pprint import pprint

r_resp = requests.get('https://example.com')

print(r_resp.status_code)  # this returns the status code of the above

print(r_resp.ok)  # this uses a boolean for "ok" or 200

print(r_resp.raise_for_status())


r_resp1 = requests.get('https://yahoo.com/alf2adfd5')

print(r_resp1.ok)  # this is an invalid request.

print(type(r_resp1.headers))

print(r_resp.headers)

#retreival of a CaseInsensitiveDic can be done using the standard dictionary call(don't worry about case
#or you can run it through a 'get' call

print(r_resp.headers['Etag'])

print(r_resp.headers.get('etag'))

error = r_resp1.raise_for_status()  # this gives details about the error message.
print(error)