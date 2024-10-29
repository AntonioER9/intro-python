import requests

url = "https://www.google.com"

r = requests.get(url, timeout=10)

print(r.status_code) # 200
r = r.json()

for user in r:
    print(user['name'])

r = requests.post(url, data={'key':'value'})
print(r.status_code) # 201