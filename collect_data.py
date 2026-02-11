# Wiktionary API Example
import requests

url = "https://en.wiktionary.org/w/api.php"
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url)
data = response.json()
print(data)