import requests
import json
import secrets


url = f'https://accounts.spotify.com/authorize?client_id={secrets.client_id}&response_type=code$redirect_uri=https%3A%2F%2Fgithub.com%2FAudodido%0A%scope=playlist-modify-public%20-modify-public-private'

params = ''
response = requests.get(url, params).json()

print(response)