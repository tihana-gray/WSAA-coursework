import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

def updatebook(id, book):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

if __name__ == "__main__":
    # updating the book I created in lab03_createbook.py (ID 1681)
    bookdiff = {
        "author": "Tihana Updated",
        "price": 99
    }

    print(updatebook(1681, bookdiff))