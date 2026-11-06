import requests

base_url = 'http://localhost:5000'

response1 = requests.get(f'{base_url}/cars/').json()
response2 = requests.get(f'{base_url}/manufacturers').json()