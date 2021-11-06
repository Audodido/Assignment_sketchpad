import requests
import json


url = 'https://api.twitter.com/2/tweets/search/stream'
params = ''
response = requests.get(url, params).json()

print(response)