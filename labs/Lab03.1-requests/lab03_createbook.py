import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

def createbook(book):
    response = requests.post(URL, json=book)
    return response.json()

if __name__ == "__main__":
    # my test book
    book = {
        "author": "Tihana Test",
        "title": "Lab 03 Question 5 Test Book",
        "price": 42
    }
    print(createbook(book))