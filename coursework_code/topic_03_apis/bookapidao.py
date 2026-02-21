# This is a module that provides a set of functions to interact with
# the demonstration book API hosted at PythonAnyhwere
# Author: Tihana Gray

import requests
import json

url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    return safeJson(response)

def getBookById(id):
    geturl = f"{url}/{id}"
    response = requests.get(geturl)
    return safeJson(response)

def createBook(book):
    response = requests.post(url, json=book)
    return safeJson(response)

def updateBook(id, bookdiff):
    updateurl = f"{url}/{id}"
    response = requests.put(updateurl, json=bookdiff)
    return safeJson(response)

def deleteBook(id):
    deleteurl = f"{url}/{id}"
    response = requests.delete(deleteurl)
    return safeJson(response)

def safeJson(response):
    """
    Returns JSON if present, otherwise returns:
    - None if empty response
    - A dict with error info if the status code is not OK
    """

    if response.status_code == 200:
        if response.text.strip() == "":
            return None  # Empty response
        try:
            return response.json()
        except:
            return None
    else:
        return {"error": response.status_code, "message": response.text}

if __name__ == "__main__":
    print(getBookById(22))
    bookdiff = {"price": 1234444}
    print(updateBook(22, bookdiff))