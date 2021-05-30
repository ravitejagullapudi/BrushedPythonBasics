import requests

import json

URL = "http://dummy.restapiexample.com/api/v1/employees"
response =  requests.get(URL)
# Response is a json formatted string so
#  string to object means use loads()
# If it is already a json object use load
# The json. load() is used to read the JSON document
#  from file and The json. loads() is used to convert 
# the JSON String document into the Python dictionary.
employees = json.loads(response.text)

print(employees['data'][0])
print(len(employees['data']))

