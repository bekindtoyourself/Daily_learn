import requests
import json

# r = requests.get('https://api.github.com/events')


# r = requests.post('http://httpbin.org/post', data = {'key':'value'})

# r = requests.put('http://httpbin.org/put', data = {'key':'value'})

# payload=  {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)

# r = requests.get('https://api.github.com/users/bekindtoyourself' , stream=True)

# url = 'https://api.github.com/users/bekindtoyourself'
# headers = {'user-agent': 'my-app/0.0.1'}

# r = requests.get(url, headers=headers)

# payload = (('key1', 'value1'), ('key1', 'value2'))
# r = requests.post("http://httpbin.org/post", data=payload)


# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}

# data = json.dumps(payload)
# print(data)
# r = requests.post(url, data)

# print(r.cookies)
# print(r.status_code)
# print(r.raw.read(10))


# s = requests.Session()

# s.get('http://httpbin.org/cookies/set/sessioncookie/1234789')
# r = s.get("http://httpbin.org/cookies")
# print(r.text)

proxy = {
    'https': 'https:127.0.0.1:1080',
}

r = requests.get('https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad', timeout=5)

# if (r.status_code == requests.codes.ok):
#     print(r.headers)

commit_data = r.json()
print(commit_data)


