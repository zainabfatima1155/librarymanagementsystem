books = []

def add_book():
    title = input("Enter book title: ")
    books.append(title)
    print("Book added successfully")

def view_books():
    for book in books:
        print(book)
