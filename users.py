users = []

def add_user():
    name = input("Enter student name: ")
    users.append(name)
    print("Student added successfully")

def view_users():
    for user in users:
        print(user)
