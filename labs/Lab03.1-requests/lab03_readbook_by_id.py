import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

if __name__ == "__main__":
    # random book id from the earlier output
    print(readbook(1660))