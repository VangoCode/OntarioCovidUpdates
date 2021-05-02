# https://data.ontario.ca/api/3/action/datastore_search
"""
JSON QUERY:
{
    "resource_id": "ed270bb8-340b-41f9-a7c6-e8ef587e6d11",
    "sort": "Reported Date desc",
    "limit": 1
}

{
    "resource_id": "ed270bb8-340b-41f9-a7c6-e8ef587e6d11",
    "sort": "_id desc",
    "limit": 1
}

https://data.ontario.ca/api/3/action/datastore_search?resource_id=ed270bb8-340b-41f9-a7c6-e8ef587e6d11&sort=Reported%20Date%20desc&limit=1
"""


import urllib.request, json
url = 'https://data.ontario.ca/api/3/action/datastore_search?resource_id=ed270bb8-340b-41f9-a7c6-e8ef587e6d11&sort=Reported%20Date%20desc&limit=2'
fileobj = urllib.request.urlopen(url)
text = fileobj.read()
parsed = json.loads(text)
print(parsed['result']["records"][0]['Total Cases']-parsed['result']["records"][1]['Total Cases'])