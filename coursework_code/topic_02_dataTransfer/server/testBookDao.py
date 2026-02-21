from BookDao import bookDao

book1 = {
    'ISBN': 1234567,
    'price': 12,
    'author': 'jk',
    'title': 'some fantasy book'
}

book2 = {
    'ISBN': 1234567,
    'price': 999,
    'author': 'mary',
    'title': 'had a little lamb'
}

# INSERT a book
returnValue = bookDao.create(book1)
print("Created:", returnValue)

# GET ALL
returnValue = bookDao.getAll()
print("All books:", returnValue)

# FIND BY ID
returnValue = bookDao.findById(book2['ISBN'])
print("find By Id:", returnValue)

# UPDATE
returnValue = bookDao.update(book2)
print("Updated:", returnValue)

# FIND AGAIN
returnValue = bookDao.findById(book2['ISBN'])
print("After Update:", returnValue)

# DELETE
returnValue = bookDao.delete(book2['ISBN'])
print("Deleted:", returnValue)

# GET ALL AGAIN
returnValue = bookDao.getAll()
print("After Delete:", returnValue)