from lab03_readbooks_function import readbooks

books = readbooks()

total = 0
count = 0

for book in books:
    if book["price"] is not None:
        total += book["price"]
        count += 1

if count > 0:
    print("Average price of", count, "books is", total / count)
else:
    print("No books with valid price found.")