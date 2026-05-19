'''9. Mini Notepad

Create menu:

1. Write File
2. Append File
3. Read File
4. Exit

Use proper file modes for each option.
'''
try:
    while True:
        print("\nMini Notepad Menu:")
        print("1. Write File")
        print("2. Append File")
        print("3. Read File")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            filename = input("Enter filename to write: ")
            content = input("Enter content to write: ")
            with open(filename, 'w') as f:
                f.write(content)
            print(f"Content written to {filename}.")
        
        elif choice == '2':
            filename = input("Enter filename to append: ")
            content = input("Enter content to append: ")
            with open(filename, 'a') as f:
                f.write(content + '\n')
            print(f"Content appended to {filename}.")
        
        elif choice == '3':
            filename = input("Enter filename to read: ")
            try:
                with open(filename, 'r') as f:
                    file_content = f.read()
                    print(f"Content of {filename}:\n{file_content}")
            except FileNotFoundError:
                print(f"{filename} not found.")
        
        elif choice == '4':
            print("Exiting Mini Notepad. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
except Exception as e:
    print("An error occurred:", e)