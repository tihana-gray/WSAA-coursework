from bookapidao import getAllBooks

books = getAllBooks()

# remove None or error rows
valid_books = [b for b in books if isinstance(b, dict) and "price" in b and b["price"] is not None]

total = sum(book["price"] for book in valid_books)
count = len(valid_books)

if count > 0:
    print("average of", count, "books is", total / count)
else:
    print("no valid books found")