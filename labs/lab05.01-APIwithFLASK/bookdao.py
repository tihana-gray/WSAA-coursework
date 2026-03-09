class BookDAO:
    books = [
        {
            "id": 1,
            "title": "Harry Potter",
            "author": "J K Rowling",
            "price": 1000
        },
        {
            "id": 2,
            "title": "The Hobbit",
            "author": "J R R Tolkien",
            "price": 500
        }
    ]

    def getAll(self):
        return self.books

    def findByID(self, id):
        for book in self.books:
            if book["id"] == id:
                return book
        return None

    def create(self, book):
        newId = self.books[-1]["id"] + 1
        book["id"] = newId
        self.books.append(book)
        return book

    def update(self, id, book):
        foundBook = self.findByID(id)
        if not foundBook:
            return None

        foundBook["title"] = book["title"]
        foundBook["author"] = book["author"]
        foundBook["price"] = book["price"]

        return foundBook

    def delete(self, id):
        foundBook = self.findByID(id)
        if not foundBook:
            return None
        self.books.remove(foundBook)
        return {"deleted": True}


bookDAO = BookDAO()