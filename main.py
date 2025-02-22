from getpass import getpass
from auth_system.database import DatabaseManager
from auth_system.security import hash_password

def main_menu():
    print("\n=== Abdu Auth System ===")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit")
    return input("Choose option: ")

def login():
    username = input("Username: ")
    password = input("Password: ") 

    db = DatabaseManager()
    result = db.execute_query(
        "SELECT * FROM users WHERE username = %s AND password_hash = %s",
        (username, hash_password(password))
    )

    if result and result.fetchone():
        print("\n=== SECRET: The moon landing was real! ===")
    else:
        print("Invalid credentials!")
    db.close()

def create_account():
    username = input("New username: ")
    password = input("New password: ") 

    db = DatabaseManager()
    try:
        db.execute_query(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (username, hash_password(password))
        )
        print("Account created successfully!")
    except Exception as e:
        print("Username already exists or another error occurred!", e)
    finally:
        db.close()


if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == '1': login()
        elif choice == '2': create_account()
        elif choice == '3': break
        else: print("Invalid choice!")
