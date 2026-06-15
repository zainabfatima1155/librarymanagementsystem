from books import *
from users import *
from transactions import *

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Student")
    print("4. View Students")
    print("5. Issue Book")
    print("6. View Issued Books")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        add_user()

    elif choice == "4":
        view_users()

    elif choice == "5":
        issue_book()

    elif choice == "6":
        view_issued()

    elif choice == "7":
        break
