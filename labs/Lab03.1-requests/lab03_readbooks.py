import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(URL)
print(response.json())