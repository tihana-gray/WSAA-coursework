import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__ == "__main__":
    print(deletebook(1681))