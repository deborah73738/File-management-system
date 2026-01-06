def create_file():
    filename = input("Enter file name: ")
    content = input("Enter file content: ")
    file = open(filename, "w")
    file.write(content)
    file.close()
    print("File created successfully")

def read_file():
    filename = input("Enter file name to read: ")
    file = open(filename, "r")
    print(file.read())
    file.close()

def main():
    while True:
        print("1. Create File")
        print("2. Read File")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
