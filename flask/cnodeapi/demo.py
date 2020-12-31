import requests

r = requests.get('http://49.233.108.117:3000/api/v1/topics')
print(r.json())