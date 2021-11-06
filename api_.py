import requests
import json


show = 'Seinfeld'
url = 'https://api.tvmaze.com/singlesearch/shows'
params = {'q':show}

response = requests.get(url,params).json()


def get_all(obj, sel=None):
    want = ['name', 'genres', 'premiered', 'network', 'ended', 'summary']
    
    if sel == 'all':
        for r, v in response.items():
            print(r,v)
            print()

    else:
        want.append(sel)
        for r, v in response.items():
            if r in want:
                print(r,v)
                print()


get_all(response, 'all')



