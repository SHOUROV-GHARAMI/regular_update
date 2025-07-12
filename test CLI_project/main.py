
from manager import initialize, add_contact, view_contacts, search_contact, remove_contact, update_contact

def menu():
    print("\n========= MENU =========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Update Contact")
    print("6. Exit")
    print("=========================")

def main():
    print("Welcome to the Contact Book CLI System!")
    print("Loading contacts from contacts.csv... Done!")
    initialize()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            remove_contact()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == '__main__':
    main()