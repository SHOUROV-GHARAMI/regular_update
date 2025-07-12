
contacts = []

from contact import Contact
from storage import save_contacts, load_contacts

def initialize():
    global contacts
    contacts = load_contacts()

def is_duplicate(phone):
    return any(c.phone == phone for c in contacts)

# def add_contact():
#     name = input("Enter Name: ")
#     phone = input("Enter Phone Number: ")
#     if not phone.isdigit():
#         print("Error: The phone number must be an integer.")
#         return
#     if is_duplicate(phone):
#         print("Error: Phone number already exists for another contact.")
#         return
#     email = input("Enter Email: ")
#     address = input("Enter Address: ")

#     contact = Contact(name, phone, email, address)
#     contacts.append(contact)
#     save_contacts(contacts)
#     print("Contact added successfully!")

# def add_contact():
#     name = input("Enter Name: ")
#     phone = input("Enter Phone Number: ")
#     if not (phone.isdigit() and len(phone) == 10):
#         print("Error: The phone number must be exactly 10 digits.")
#         return
#     if is_duplicate(phone):
#         print("Error: Phone number already exists for another contact.")
#         return
#     email = input("Enter Email: ")
#     address = input("Enter Address: ")

#     contact = Contact(name, phone, email, address)
#     contacts.append(contact)
#     save_contacts(contacts)
#     print("Contact added successfully!")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    if not (phone.isdigit() and len(phone) == 10):
        print("Error: The phone number must be exactly 10 digits.")
        return
    if is_duplicate(phone):
        print("Error: Phone number already exists for another contact.")
        return
    email = input("Enter Email: ")
    if "@" not in email:
        print("Error: Email must contain '@'.")
        return
    address = input("Enter Address: ")

    contact = Contact(name, phone, email, address)
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. Name : {c.name}\n   Phone : {c.phone}\n   Email : {c.email}\n   Address: {c.address}\n")

def search_contact():
    term = input("Enter search term (name/email/phone): ").lower()
    found = False
    for c in contacts:
        if term in c.name.lower() or term in c.email.lower() or term in c.phone:
            print(f"\nName : {c.name}\nPhone : {c.phone}\nEmail : {c.email}\nAddress: {c.address}")
            found = True
    if not found:
        print("No contact found with that term.")

def remove_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    global contacts
    for c in contacts:
        if c.phone == phone:
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.remove(c)
                save_contacts(contacts)
                print("Contact deleted successfully!")
                return
    print("Contact not found.")

# def update_contact():
#     phone = input("Enter the phone number of the contact to update: ")
#     for c in contacts:
#         if c.phone == phone:
#             print(f"Updating contact: {c.name}")
#             c.name = input("Enter new Name (leave blank to keep current): ") or c.name
#             c.email = input("Enter new Email (leave blank to keep current): ") or c.email
#             c.address = input("Enter new Address (leave blank to keep current): ") or c.address
#             save_contacts(contacts)
#             print("Contact updated successfully!")
#             return
#     print("Contact not found.")

# def update_contact():
#     phone = input("Enter the phone number of the contact to update: ")
#     for c in contacts:
#         if c.phone == phone:
#             print(f"Updating contact: {c.name}")
#             new_name = input("Enter new Name (leave blank to keep current): ") or c.name
#             new_email = input("Enter new Email (leave blank to keep current): ") or c.email
#             new_address = input("Enter new Address (leave blank to keep current): ") or c.address
#             new_phone = input("Enter new Phone Number (leave blank to keep current): ") or c.phone
#             if new_phone != c.phone:
#                 if not (new_phone.isdigit() and len(new_phone) == 10):
#                     print("Error: The phone number must be exactly 10 digits.")
#                     return
#                 if is_duplicate(new_phone):
#                     print("Error: Phone number already exists for another contact.")
#                     return
#             c.name = new_name
#             c.email = new_email
#             c.address = new_address
#             c.phone = new_phone
#             save_contacts(contacts)
#             print("Contact updated successfully!")
#             return
#     print("Contact not found.")

def update_contact():
    phone = input("Enter the phone number of the contact to update: ")
    for c in contacts:
        if c.phone == phone:
            print(f"Updating contact: {c.name}")
            new_name = input("Enter new Name (leave blank to keep current): ") or c.name
            new_email = input("Enter new Email (leave blank to keep current): ") or c.email
            if new_email and "@" not in new_email:
                print("Error: Email must contain '@'.")
                return
            new_address = input("Enter new Address (leave blank to keep current): ") or c.address
            new_phone = input("Enter new Phone Number (leave blank to keep current): ") or c.phone
            if new_phone != c.phone:
                if not (new_phone.isdigit() and len(new_phone) == 10):
                    print("Error: The phone number must be exactly 10 digits.")
                    return
                if is_duplicate(new_phone):
                    print("Error: Phone number already exists for another contact.")
                    return
            c.name = new_name
            c.email = new_email
            c.address = new_address
            c.phone = new_phone
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")