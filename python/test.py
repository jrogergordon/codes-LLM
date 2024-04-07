

import requests

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer YOUR_YELP_API_KEY"
}

params = {
    "term": "tacos",
    "location": "90045"
}

response = requests.get(url, headers=headers, params=params)

data = response.json()
print(data) 
                 