import mysql.connector

class BookDao:

    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='datarepresentation'
        )

    def create(self, book):
        cursor = self.db.cursor()
        sql = "INSERT INTO books (ISBN, title, author, price) VALUES (%s, %s, %s, %s)"
        values = (book['ISBN'], book['title'], book['author'], book['price'])
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM books")
        results = cursor.fetchall()
        return [self.convertToDict(result) for result in results]

    def findById(self, ISBN):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM books WHERE ISBN = %s", (ISBN,))
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self, book):
        cursor = self.db.cursor()
        sql = "UPDATE books SET title=%s, author=%s, price=%s WHERE ISBN=%s"
        values = (book['title'], book['author'], book['price'], book['ISBN'])
        cursor.execute(sql, values)
        self.db.commit()
        return book

    def delete(self, ISBN):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM books WHERE ISBN = %s", (ISBN,))
        self.db.commit()   # IMPORTANT
        return cursor.rowcount

    def convertToDict(self, result):
        colnames = ['ISBN', 'title', 'author', 'price']
        if not result:
            return {}
        return {colnames[i]: result[i] for i in range(len(colnames))}


bookDao = BookDao()