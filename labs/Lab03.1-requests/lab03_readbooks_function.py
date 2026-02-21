import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(URL)
    return response.json()

if __name__ == "__main__":
    print(readbooks())