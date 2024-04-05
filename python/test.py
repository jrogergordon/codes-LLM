I'm trying to make an API request to this URL:
https://api.yelp.com/v3/businesses/search?term=tacos&Location=90045

but getting this error:
"Please specify a location or a latitude and longitude"

How do I fix this error?

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
                 