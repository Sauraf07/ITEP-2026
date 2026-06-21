from src.menus.author_menu import AuthorMenu
from src.menus.book_menu import BookMenu

while True:
    print("Press 1 for Author Works")
    print("Press 2 For Books")
    print("Press 0 To Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Welcome to the Authors Menu")
        AuthorMenu().show_menu()

    elif choice == 2:
        print("Welcome to the Books Menu")
        BookMenu().show_menu()

    elif choice == 0:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")