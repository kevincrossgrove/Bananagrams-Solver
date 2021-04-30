import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + '/api/bananas/kevincrossgroveismynamedawgwhatisyourslolxd')
response = response.json()
for row in response['data']:
    print(row)

print('Remaining Letters:', response['remaining'])