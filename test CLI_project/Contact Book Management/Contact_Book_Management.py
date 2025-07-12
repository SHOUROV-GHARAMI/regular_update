#empty dictionary
contacts = {}
while True:
    print("\n Contact Book Management System")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contact")
    print("7. Exit contact Book")

    choice = int(input("Choose your option: "))
    if choice == 1:
        name = str(input("Enter your name: "))
        if name in contacts:
            print(f"Contract name {name} already exists!")
        else:
            age = input("Enter age = ")
            email = input("Enter email = ")
            mobile_number = int(input("Enter number = "))
            contacts[name] = {"age":int(age), "email": email, "mobile_number":mobile_number}
            print(f"Contract Name:{name} age:{age} Email:{email} number:{mobile_number} has been added to the database successfully!")

    elif choice == 2:
        name = str(input("Enter contract name to view = "))
        if name in contacts:
            contacts = contacts[name]
            print(f" Name:{name},\n age:{age},\n number:{mobile_number}")
        else:
            print("Contact not found")

    elif choice == 3:
        name = str(input("Enter name to update contact = "))
        if name in contacts:
            age = input("Enter update age = ")
            email = input("Enter update email = ")
            mobile_number = int(input("Enter update number = "))
            contacts[name] = {"age":int(age), "email": email, "mobile_number":mobile_number}
        else:
            print("Contact not found!")

    elif choice == 4:
        name = str(input("Enter contact name to delete contact information = "))
        if name in contacts:
            del contacts[name]
            print(f"Contact name:{name} has been deleted successfully!")
        else:
            print("Contact not found")

    elif choice == 5:
        search_name = str(input("Enter contact name to search = "))
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found Name:{name}, age:{age}, number:{mobile_number}, Email:{email} ")
                found = True
        if not found:
            print("No contact found with that name")

    elif choice == 6:
        print(f"Total contacts in your book: {len(contacts)}")

    elif choice == 7:
        print("*** Closing the program! ***")
        break
    
    else:
        print("Invalid input")
