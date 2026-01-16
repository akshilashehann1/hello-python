import requests

url = "https://raw.githubusercontent.com/akshilashehann1/hello-python/main/hello.py"
response = requests.get(url)

print(response.text)
