issued_books = {}

def issue_book():
    student = input("Student Name: ")
    book = input("Book Name: ")

    issued_books[book] = student
    print("Book Issued")

def view_issued():
    print(issued_books)
